(function () {
  'use strict';
  window.ECLIPSE_RUNTIME_CONFIG = Object.freeze({
    environment: 'demo',
    apiBase: '/api',
    demoAuth: true,
    showDemoBanner: true,
    oidcLoginPath: '/auth/user/login',
    oidcSessionPath: '/auth/session',
    oidcLogoutPath: '/auth/logout',
    mockDomains: ['manufacturing', 'finance', 'public', 'developer', 'llm', 'admin'],
  });
}());
