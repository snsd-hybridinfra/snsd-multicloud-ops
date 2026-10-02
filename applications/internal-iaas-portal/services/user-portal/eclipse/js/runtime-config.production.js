(function () {
  'use strict';
  window.ECLIPSE_RUNTIME_CONFIG = Object.freeze({
    environment: 'production',
    apiBase: '/api',
    demoAuth: false,
    showDemoBanner: false,
    oidcLoginPath: '/auth/user/login',
    oidcSessionPath: '/auth/session',
    oidcLogoutPath: '/auth/logout',
    mockDomains: [],
  });
}());
