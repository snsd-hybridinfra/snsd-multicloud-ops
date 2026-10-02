(function () {
  'use strict';
  const config = window.ECLIPSE_RUNTIME_CONFIG || {demoAuth: true};
  const DEMO_ACCOUNTS = {
    customer: { userId: 'demo-user', tenantId: 'developer-demo', tenantName: 'Eclipse Developer Demo', role: 'CUSTOMER_USER', scopes: ['cloud:read', 'cloud:request', 'developer:read', 'llm:invoke', 'llm:usage:read'], landingPath: '/developer/dashboard' },
    developer: { userId: 'developer-user', tenantId: 'developer-demo', tenantName: 'Eclipse Developer Demo', role: 'CUSTOMER_USER', scopes: ['cloud:read', 'cloud:request', 'developer:read', 'llm:invoke', 'llm:usage:read'], landingPath: '/developer/dashboard' },
    factory: { userId: 'factory-user', tenantId: 'hanbit-mobility', tenantName: 'Hanbit Mobility · Factory Demo', role: 'CUSTOMER_USER', scopes: ['cloud:read', 'cloud:request', 'manufacturing:read', 'llm:invoke', 'llm:usage:read'], landingPath: '/manufacturing/dashboard' },
    manager: { userId: 'demo-manager', tenantId: 'eclipse-msp', tenantName: 'Eclipse Cloud MSP', role: 'MSP_ADMIN', scopes: ['admin:read', 'admin:write', 'approval:manage', 'terraform:read', 'audit:read', 'finance:read', 'public:read', 'llm:invoke', 'llm:usage:read', 'monitoring:assist'], landingPath: '/admin/dashboard' },
    finance: { userId: 'finance-user', tenantId: 'demo-finance', tenantName: 'Demo Finance', role: 'CUSTOMER_USER', scopes: ['cloud:read', 'cloud:request', 'finance:read', 'llm:invoke', 'llm:usage:read'], landingPath: '/finance/dashboard' },
    public: { userId: 'public-user', tenantId: 'demo-public-agency', tenantName: 'Demo Public Agency', role: 'CUSTOMER_USER', scopes: ['cloud:read', 'cloud:request', 'public:read', 'llm:invoke', 'llm:usage:read'], landingPath: '/public/dashboard' },
    operator: { userId: 'msp-operator', tenantId: 'eclipse-msp', tenantName: 'Eclipse Cloud MSP', role: 'MSP_OPERATOR', scopes: ['admin:read', 'approval:manage', 'terraform:read', 'finance:read'] },
    admin: { userId: 'msp-admin', tenantId: 'eclipse-msp', tenantName: 'Eclipse Cloud MSP', role: 'MSP_ADMIN', scopes: ['admin:read', 'admin:write', 'approval:manage', 'terraform:read', 'audit:read', 'finance:read', 'public:read', 'llm:invoke', 'llm:usage:read', 'monitoring:assist'] },
    llm: { userId: 'llm-user', tenantId: 'llm-personal-demo', tenantName: 'Personal LLM Workspace Demo', role: 'LLM_USER', scopes: ['llm:invoke', 'llm:usage:read', 'monitoring:assist'], landingPath: '/llm/dashboard' },
  };
  const PORTAL_ROLES = ['CUSTOMER_USER', 'CUSTOMER_MANAGER', 'MSP_OPERATOR', 'MSP_ADMIN', 'LLM_USER'];
  let current = null;
  function isDemoEnabled() { return config.demoAuth !== false; }
  function safePath(value, fallback) {
    const configured = String(value || fallback).trim();
    const safe = configured.startsWith('/') && !configured.startsWith('//') && !configured.includes('\\') && !configured.includes('#') && !/[\u0000-\u001f\u007f]/.test(configured);
    return safe ? configured : fallback;
  }
  function addQuery(path, name, value) {
    if (!value) return path;
    return `${path}${path.includes('?') ? '&' : '?'}${encodeURIComponent(name)}=${encodeURIComponent(value)}`;
  }
  function returnUrl() {
    if (!window.location || !window.location.origin) return '';
    const href = String(window.location.href || `${window.location.origin}/`);
    const parts = href.split('#');
    const separator = parts[0].includes('?') ? '&' : '?';
    const base = /[?&]auth_return=/.test(parts[0]) ? parts[0] : `${parts[0]}${separator}auth_return=1`;
    return `${base}${parts[1] ? `#${parts[1]}` : '#/login'}`;
  }
  function loginUrl() {
    return addQuery(safePath(config.oidcLoginPath, '/auth/user/login'), 'return_to', returnUrl());
  }
  function logoutUrl() {
    const path = safePath(config.oidcLogoutPath, '/auth/logout');
    if (!window.location || !window.location.origin) return path;
    return addQuery(path, 'redirect_uri', `${window.location.origin}${window.location.pathname || '/'}#/login`);
  }
  function sessionUrl() { return safePath(config.oidcSessionPath, '/auth/session'); }
  function scopeList(value) {
    const values = Array.isArray(value) ? value : String(value || '').split(/[\s,]+/);
    return [...new Set(values.map(item => String(item).trim()).filter(Boolean))];
  }
  function defaultLanding(role, scopes) {
    if (role === 'LLM_USER') return '/llm/dashboard';
    if (role === 'MSP_OPERATOR' || role === 'MSP_ADMIN') return '/admin/dashboard';
    if (role === 'CUSTOMER_MANAGER' && scopes.includes('team:read')) return '/customer/team';
    if (scopes.includes('developer:read')) return '/developer/dashboard';
    if (scopes.includes('manufacturing:read')) return '/manufacturing/dashboard';
    if (scopes.includes('finance:read')) return '/finance/dashboard';
    if (scopes.includes('public:read')) return '/public/dashboard';
    return '/forbidden';
  }
  function normalizeSession(payload) {
    const identity = payload && (payload.user || payload.identity || payload);
    const roles = identity && (Array.isArray(identity.roles) ? identity.roles : [identity.role]);
    const role = (roles || []).map(value => String(value || '').toUpperCase()).find(value => PORTAL_ROLES.includes(value));
    const userId = identity && String(identity.userId || identity.user_id || identity.sub || identity.email || '').trim();
    const tenantId = identity && String(identity.tenantId || identity.tenant_id || '').trim();
    if (!userId || !tenantId || !role) throw new Error('Authenticated session is missing required portal identity claims.');
    const scopes = scopeList(identity.scopes || identity.scope);
    return {
      userId,
      tenantId,
      tenantName: String(identity.tenantName || identity.tenant_name || tenantId).trim(),
      role,
      scopes,
      landingPath: defaultLanding(role, scopes),
    };
  }
  async function bootstrap() {
    if (isDemoEnabled()) return current;
    const response = await window.fetch(sessionUrl(), {credentials: 'same-origin', cache: 'no-store', headers: {'Accept': 'application/json'}});
    if (response.status === 401 || response.status === 403) { current = null; return null; }
    if (!response.ok) throw new Error(`Session check failed (HTTP ${response.status})`);
    current = normalizeSession(await response.json());
    return current;
  }
  function login(account) {
    if (!isDemoEnabled()) return null;
    const identifier = String(account || '').trim().toLowerCase();
    const entry = Object.entries(DEMO_ACCOUNTS).find(([key, demo]) => key === identifier || demo.userId.toLowerCase() === identifier);
    current = entry ? {...entry[1], scopes: [...entry[1].scopes]} : null;
    return current;
  }
  function register(profile) {
    if (!isDemoEnabled()) return null;
    const tenantSlug = String(profile.company || 'self-service-tenant').toLowerCase().trim().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '') || 'self-service-tenant';
    current = {
      userId: String(profile.email || '').trim().toLowerCase(),
      tenantId: `signup-${tenantSlug}`,
      tenantName: String(profile.company || '').trim(),
      role: 'CUSTOMER_USER',
      scopes: ['cloud:read', 'cloud:request', 'developer:read', 'llm:invoke', 'llm:usage:read'],
      landingPath: '/developer/dashboard',
    };
    return current;
  }
  function logout() { if (window.EclipseLLM) window.EclipseLLM.reset(); current = null; }
  function user() { return current; }
  function isAuthenticated() { return Boolean(current); }
  function headers() {
    if (!current || !isDemoEnabled()) return {};
    // The MVP APIs use their established lowercase service roles; the portal keeps the business role names.
    const legacyRoles = {CUSTOMER_USER: 'user', CUSTOMER_MANAGER: 'user', MSP_OPERATOR: 'approver,auditor', MSP_ADMIN: 'approver,grant-admin,auditor', LLM_USER: 'llm-user'};
    const serviceRoles = legacyRoles[current.role] || current.role;
    return {'X-Dev-User': current.userId, 'X-Dev-Roles': `${serviceRoles},${current.role}`, 'X-Dev-Scopes': current.scopes.join(' '), 'X-Dev-Tenant': current.tenantId};
  }
  window.EclipseAuth = { DEMO_ACCOUNTS, isDemoEnabled, loginUrl, logoutUrl, sessionUrl, bootstrap, login, register, logout, user, isAuthenticated, headers };
}());
