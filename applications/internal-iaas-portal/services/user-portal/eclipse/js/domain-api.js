(function () {
  'use strict';

  const config = window.ECLIPSE_RUNTIME_CONFIG || {};

  function isMock(domain) {
    return Array.isArray(config.mockDomains) && config.mockDomains.includes(domain);
  }

  function clone(value) {
    return value == null ? value : JSON.parse(JSON.stringify(value));
  }

  async function get(domain, path, mockValue) {
    if (isMock(domain)) {
      return clone(typeof mockValue === 'function' ? mockValue() : mockValue);
    }
    return window.EclipseAPI.get(path);
  }

  async function post(domain, path, body, mockFactory) {
    if (isMock(domain)) {
      const value = typeof mockFactory === 'function' ? mockFactory(body) : mockFactory;
      return clone(value);
    }
    return window.EclipseAPI.post(path, body);
  }

  window.EclipseDomainAPI = { get, post, isMock };
}());
