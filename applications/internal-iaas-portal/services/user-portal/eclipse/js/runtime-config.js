(function () {
  'use strict';
  // Safe default: an unspecified deployment never enables demo identities or mock data.
  window.ECLIPSE_RUNTIME_CONFIG = window.ECLIPSE_RUNTIME_CONFIG || {
    environment: 'production',
    apiBase: '/api',
    demoAuth: false,
    showDemoBanner: false,
    oidcLoginPath: '/auth/user/login',
    oidcSessionPath: '/auth/session',
    oidcLogoutPath: '/auth/logout',
    mockDomains: [],
  };
}());
