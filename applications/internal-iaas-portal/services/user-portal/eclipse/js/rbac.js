(function () {
  'use strict';
  const routeRoles = {
    customer: ['CUSTOMER_USER', 'CUSTOMER_MANAGER'],
    customerManager: ['CUSTOMER_MANAGER'],
    admin: ['MSP_OPERATOR', 'MSP_ADMIN'],
    adminSystem: ['MSP_ADMIN'],
    manufacturing: ['CUSTOMER_USER', 'CUSTOMER_MANAGER'],
    finance: ['CUSTOMER_USER', 'CUSTOMER_MANAGER', 'MSP_OPERATOR', 'MSP_ADMIN'],
    public: ['CUSTOMER_USER', 'CUSTOMER_MANAGER', 'MSP_ADMIN'],
    developer: ['CUSTOMER_USER', 'CUSTOMER_MANAGER'],
    llm: ['LLM_USER', 'CUSTOMER_USER', 'CUSTOMER_MANAGER', 'MSP_ADMIN'],
    llmUsage: ['LLM_USER', 'CUSTOMER_USER', 'CUSTOMER_MANAGER', 'MSP_ADMIN'],
    llmMonitoring: ['LLM_USER', 'MSP_OPERATOR', 'MSP_ADMIN'],
  };
  const routeScopes = {
    customerManager: ['team:read'],
    manufacturing: ['manufacturing:read'],
    finance: ['finance:read'],
    public: ['public:read'],
    developer: ['developer:read'],
    llm: ['llm:invoke'],
    llmUsage: ['llm:usage:read'],
    llmMonitoring: ['llm:invoke', 'monitoring:assist'],
  };
  function canAccess(route, account) {
    if (!account) return false;
    const roles = routeRoles[route] || [];
    const scopes = routeScopes[route] || [];
    return roles.includes(account.role) && scopes.every(scope => account.scopes.includes(scope));
  }
  function routePolicy(path) {
    if (path.startsWith('/admin/system') || path === '/admin/tenants' || path === '/admin/users' || path === '/admin/grants' || path === '/admin/audit') return 'adminSystem';
    if (path.startsWith('/admin')) return 'admin';
    if (path === '/llm/monitoring-assistant') return 'llmMonitoring';
    if (path === '/llm/usage' || path === '/llm/cost') return 'llmUsage';
    if (path.startsWith('/llm')) return 'llm';
    if (path.startsWith('/finance')) return 'finance';
    if (path.startsWith('/public')) return 'public';
    if (path.startsWith('/developer')) return 'developer';
    if (path === '/customer/team') return 'customerManager';
    if (path.startsWith('/manufacturing')) return 'manufacturing';
    return 'customer';
  }
  window.EclipseRBAC = { canAccess, routePolicy, routeRoles, routeScopes };
}());
