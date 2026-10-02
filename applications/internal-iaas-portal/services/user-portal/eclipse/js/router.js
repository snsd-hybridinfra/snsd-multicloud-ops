(function () {
  'use strict';
  let listener = function () {};
  function path() { return window.location.hash.replace(/^#/, '') || '/login'; }
  function navigate(next) { window.location.hash = next; }
  function onChange(callback) { listener = callback; window.addEventListener('hashchange', () => listener(path())); }
  window.EclipseRouter = { path, navigate, onChange };
}());
