(function () {
  'use strict';
  const config = window.ECLIPSE_RUNTIME_CONFIG || { apiBase: '/api' };
  function apiErrorMessage(body, status) {
    const detail = body && body.detail;
    if (typeof detail === 'string') return detail;
    if (Array.isArray(detail)) return detail.map(item => item.msg || 'Please check the input.').join(' / ');
    if (detail && typeof detail === 'object') return detail.message || JSON.stringify(detail);
    return `Request failed (HTTP ${status})`;
  }
  function notifyExpiredSession(status) {
    const auth = window.EclipseAuth;
    if (status !== 401 || !auth || !auth.isDemoEnabled || auth.isDemoEnabled()) return;
    window.dispatchEvent(new CustomEvent('eclipse:auth-expired'));
  }
  async function request(path, options) {
    const authHeaders = window.EclipseAuth && window.EclipseAuth.headers ? window.EclipseAuth.headers() : {};
    const url = path.startsWith('/admin-api/') ? path : `${config.apiBase}${path}`;
    const response = await fetch(url, Object.assign({}, options || {}, { credentials: 'same-origin', headers: Object.assign({'Accept': 'application/json'}, authHeaders, (options || {}).headers || {}) }));
    if (!response.ok) { notifyExpiredSession(response.status); const body = await response.json().catch(() => ({})); const error = new Error(apiErrorMessage(body, response.status)); error.status = response.status; throw error; }
    return response.status === 204 ? null : response.json();
  }
  window.EclipseAPI = { request, get: path => request(path), post: (path, body, headers) => request(path, { method: 'POST', headers: Object.assign({'Content-Type': 'application/json'}, headers || {}), body: JSON.stringify(body) }) };
}());
