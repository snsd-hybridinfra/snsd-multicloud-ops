(function () {
  'use strict';
  const esc = value => String(value == null ? '' : value).replace(/[&<>"']/g, char => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[char]));

  function renderServiceSkus(config) {
    const single = config.items.length === 1;
    const intro = single ? '' : `<section class="service-sku-intro"><small>${esc(config.eyebrow)}</small><h3>${esc(config.title)}</h3><p>${esc(config.copy)}</p></section>`;
    return `${intro}<div class="service-sku-grid${single?' single':''}">${config.items.map(item => `<article><div><code>${esc(item.sku)}</code><em>${esc(item.status)}</em></div><small>${esc(item.category)}</small><h3>${esc(item.name)}</h3><p>${esc(item.copy)}</p>${item.features?.length?`<ul class="service-module-list${item.features.length===4?' four':''}">${item.features.map((feature,index)=>`<li><span>0${index+1}</span><div><strong>${esc(feature.name)}</strong><small>${esc(feature.copy)}</small></div></li>`).join('')}</ul>`:''}<dl><div><dt>Platform dependency</dt><dd>${esc(item.requires)}</dd></div><div><dt>Delivery owner</dt><dd>${esc(item.owner)}</dd></div></dl>${single?'':`<button class="button" type="button" disabled>Development track</button>`}</article>`).join('')}</div>`;
  }

  window.EclipseCatalog = {renderServiceSkus};
}());
