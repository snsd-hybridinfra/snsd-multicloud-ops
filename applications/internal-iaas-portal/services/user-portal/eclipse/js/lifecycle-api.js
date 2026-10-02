(function () {
  'use strict';

  const resourceStatus = {
    RUNNING: 'ACTIVE',
    PROVISION_FAILED: 'PROVISION_FAILED',
    TERMINATING: 'DESTROYING',
    TERMINATED: 'DESTROYED',
    TERMINATION_FAILED: 'DESTROY_FAILED',
  };

  function clone(value) { return value == null ? value : JSON.parse(JSON.stringify(value)); }
  function idempotencyKey(domain) {
    const random = window.crypto && window.crypto.randomUUID ? window.crypto.randomUUID() : `${Date.now()}-${Math.random().toString(16).slice(2)}`;
    return `portal-${domain}-${random}`.slice(0, 128);
  }
  function normalize(item, context) {
    const source = item || {};
    const extra = context || {};
    const blueprint = source.blueprint_id || source.blueprint || extra.blueprint || source.product_code || source.sku || extra.sku || 'MANAGED-BLUEPRINT';
    const status = resourceStatus[source.resource_status || source.resourceStatus] || source.status || 'PENDING';
    return {
      id: source.request_id || source.id,
      project: extra.project || source.project || source.parameters?.project_name || blueprint.toLowerCase().replace(/_/g, '-'),
      sku: extra.sku || source.sku || blueprint,
      blueprint,
      environment: source.environment || source.blueprint_environment || extra.environment || 'DEV',
      status,
      requestStatus: source.request_status || source.requestStatus || source.status || status,
      deliveryStatus: source.delivery_status || source.deliveryStatus || 'PENDING',
      resourceStatus: source.resource_status || source.resourceStatus || null,
      size: source.size || source.blueprint_size || null,
      purpose: source.purpose || null,
      grantId: source.grant_id || source.grantId || null,
      grantExpiresAt: source.grant_expires_at || source.grantExpiresAt || null,
      resourceId: source.resource_id || source.resourceId || null,
      rejectionReason: source.rejection_reason || source.rejectionReason || null,
      lastError: source.last_error || source.lastError || null,
      retryCount: source.retry_count || source.retryCount || 0,
      created: String(source.created_at || source.created || new Date().toISOString()).slice(0, 10),
      updated: String(source.updated_at || source.created_at || source.created || new Date().toISOString()),
    };
  }
  function normalizeResource(item) {
    const source = item || {};
    return {
      id: source.resource_id || source.id,
      requestId: source.request_id || source.requestId || null,
      status: resourceStatus[source.status] || source.status || 'PROVISIONING',
      rawStatus: source.rawStatus || source.status || 'PROVISIONING',
      endpoint: source.endpoint || null,
      type: source.resource_type || source.type || 'MANAGED_RESOURCE',
      name: source.display_name || source.name || source.resource_id || source.id || 'Managed resource',
      details: source.details || {},
      updated: String(source.updated_at || source.updated || new Date().toISOString()),
    };
  }
  async function list(domain, mockValue) {
    if (window.EclipseDomainAPI.isMock(domain)) return clone(typeof mockValue === 'function' ? mockValue() : mockValue || []);
    const items = await window.EclipseAPI.get('/v1/requests');
    return items.map(item => normalize(item));
  }
  async function submitBlueprint(domain, payload, context, mockFactory) {
    if (window.EclipseDomainAPI.isMock(domain)) {
      const value = typeof mockFactory === 'function' ? mockFactory(payload) : mockFactory;
      return normalize(clone(value), context);
    }
    const item = await window.EclipseAPI.post('/v1/blueprint-requests', payload, {'Idempotency-Key': idempotencyKey(domain)});
    return normalize(item, context);
  }
  async function getRequest(domain, requestId, mockValue) {
    if (window.EclipseDomainAPI.isMock(domain)) {
      const item = typeof mockValue === 'function' ? mockValue(requestId) : mockValue;
      return normalize(clone(item));
    }
    return normalize(await window.EclipseAPI.get(`/v1/requests/${encodeURIComponent(requestId)}`));
  }
  async function cancelRequest(domain, requestId, mockValue) {
    if (window.EclipseDomainAPI.isMock(domain)) {
      const item = typeof mockValue === 'function' ? mockValue(requestId) : mockValue;
      return normalize(Object.assign({}, clone(item), {status: 'CANCELLED', requestStatus: 'CANCELLED'}));
    }
    return normalize(await window.EclipseAPI.post(`/v1/requests/${encodeURIComponent(requestId)}/cancel`, {}));
  }
  async function listResources(domain, mockValue) {
    const items = window.EclipseDomainAPI.isMock(domain)
      ? clone(typeof mockValue === 'function' ? mockValue() : mockValue || [])
      : await window.EclipseAPI.get('/v1/resources');
    return items.map(item => normalizeResource(item));
  }

  window.EclipseLifecycleAPI = {list, submitBlueprint, getRequest, cancelRequest, listResources, normalize, normalizeResource};
}());
