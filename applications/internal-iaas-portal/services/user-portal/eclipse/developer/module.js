(function () {
  'use strict';
  const esc = value => String(value == null ? '' : value).replace(/[&<>"']/g, char => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[char]));
  const money = value => `₩${Number(value).toLocaleString('ko-KR')}`;
  const packages = {
    'DEV-CP-START': {name:'Starter', cost:149000, size:'SMALL', duration:72, copy:'개인 개발과 PoC를 위한 관리형 시작 환경', specs:['2 vCPU · 4 GB','Container runtime','PostgreSQL Basic','7-day logs']},
    'DEV-CP-TEAM': {name:'Team', cost:379000, size:'STANDARD', duration:168, copy:'협업 개발팀을 위한 표준 애플리케이션 환경', specs:['4 vCPU · 8 GB','Managed Kubernetes','PostgreSQL HA','CI/CD · Monitoring']},
    'DEV-CP-SCALE': {name:'Scale', cost:729000, size:'LARGE', duration:168, copy:'확장형 서비스 운영을 위한 확장 환경', specs:['8 vCPU · 16 GB','Auto scaling','Database HA · Redis','30-day observability']},
  };
  const state = {sku:'DEV-CP-TEAM', project:'developer-api', environment:'DEV', runtime:'Managed Kubernetes', database:'PostgreSQL'};
  const runtimeBlueprints = {'Managed Kubernetes':'API_DEVELOPMENT_STACK','Container Runtime':'WEB_APPLICATION_STACK','Virtual Machine':'VM_APPLICATION_STACK'};
  const demoMode = window.EclipseDomainAPI.isMock('developer');
  const requests = demoMode ? [
    {id:'DEV-REQ-00104',project:'commerce-api',sku:'DEV-CP-TEAM',blueprint:'API_DEVELOPMENT_STACK',environment:'DEV',status:'ACTIVE',requestStatus:'GRANTED',deliveryStatus:'DELIVERED',resourceStatus:'RUNNING',resourceId:'DEV-RES-00031',grantId:'DEV-GRANT-0021',grantExpiresAt:'2026-10-05T09:00:00Z',purpose:'Developer environment for commerce-api',created:'2026-09-26'},
    {id:'DEV-REQ-00103',project:'preview-web',sku:'DEV-CP-START',blueprint:'WEB_APPLICATION_STACK',environment:'DEV',status:'PENDING',requestStatus:'PENDING',deliveryStatus:'DELIVERED',purpose:'Developer environment for preview-web',created:'2026-09-28'},
  ] : [];
  const resources = demoMode ? [{id:'DEV-RES-00031',requestId:'DEV-REQ-00104',status:'ACTIVE',rawStatus:'RUNNING',endpoint:'https://commerce-api.demo.internal',type:'API_DEVELOPMENT_STACK',name:'commerce-api',details:{runtime:'Managed Kubernetes',database:'PostgreSQL HA',exposure:'Private'},updated:'2026-09-28T08:30:00Z'}] : [];
  const lifecycle = ['PENDING','APPROVED','GRANTED','PROVISIONING','ACTIVE','EXPIRED','DESTROYING','DESTROYED'];
  let requestLoadState = demoMode ? 'ready' : 'idle';
  let requestLoadError = '';
  let selectedRequest = null;
  let detailLoadState = 'idle';
  let detailError = '';
  let resourceLoadState = 'idle';
  let resourceLoadError = '';

  function dashboard() {
    return `<div class="metric-grid"><article><span>Active workspaces</span><strong>2</strong><small>Developer scope only</small></article><article><span>Open requests</span><strong>1</strong><small>Awaiting approval</small></article><article><span>Monthly estimate</span><strong>${money(528000)}</strong><small class="demo-tag">DEMO DATA</small></article><article><span>Service alerts</span><strong>0</strong><small>All systems healthy</small></article></div><div class="domain-grid"><article class="data-card"><div class="card-head"><div><h3>Developer environments</h3><p>Application delivery overview</p></div><a href="#/developer/infrastructure">View infrastructure →</a></div><div class="domain-rows"><div><strong>commerce-api</strong><span><b>Team · Kubernetes</b><small>DEV · PostgreSQL HA</small></span><time>Updated today</time><em class="domain-status active">ACTIVE</em></div><div><strong>preview-web</strong><span><b>Starter · Container</b><small>DEV · PostgreSQL Basic</small></span><time>Reviewing</time><em class="domain-status under_review">UNDER REVIEW</em></div></div></article><article class="data-card"><div class="card-head"><div><h3>LLM ready</h3><p>Included entitlement</p></div></div><div class="service-health"><span>✦</span><div><strong>Eclipse AI workspace</strong><small>llm:invoke · usage visibility</small></div><b>AVAILABLE</b></div></article></div>`;
  }

  function catalog() {
    return `<div class="product-grid developer-catalog"><article class="product featured package-product"><span class="product-art">⌘</span><div><small>DEVELOPER · CLOUD PLATFORM</small><h3>Developer Cloud Platform</h3><p>산업 특화 정책과 분리된 일반 웹·API 개발용 IaaS + PaaS 통합 패키지입니다.</p><div class="package-columns"><div><b>IaaS Configuration</b><span>Compute · Network · Storage · Load Balancer</span></div><div><b>PaaS Configuration</b><span>Container · Kubernetes · Database · CI/CD · Monitoring</span></div></div><div class="sku-grid">${Object.entries(packages).map(([code,item])=>`<article class="sku-card ${code===state.sku?'selected':''}"><small>DEVELOPER</small><code>${code}</code><h4>${item.name}</h4><p>${item.copy}</p><ul>${item.specs.map(spec=>`<li>${spec}</li>`).join('')}</ul><div><span>월 예상</span><strong>${money(item.cost)}</strong></div><a class="button ${code===state.sku?'primary':''}" href="#/developer/configurator" data-dev-sku="${code}">${code===state.sku?'Continue':'Select'} ${item.name}</a></article>`).join('')}</div></div></article><article class="product"><span class="product-art lavender">✦</span><div><small>AI / LLM · AVAILABLE</small><h3>Eclipse AI</h3><p>일반 개발자 계정에는 모델 실행과 사용량·비용 조회 권한이 기본 제공됩니다.</p><ul><li>Tenant-isolated prompt workspace</li><li>Model selection</li><li>Usage and token cost</li></ul><a class="button" href="#/llm/service">Open LLM Service <span>→</span></a></div></article></div>`;
  }

  function configurator() {
    const selected = packages[state.sku];
    const options=(values,current)=>values.map(value=>`<option ${value===current?'selected':''}>${value}</option>`).join('');
    return `<div class="wizard-layout"><form id="developer-config" class="wizard-card"><div class="wizard-step"><div class="step-title"><span>01</span><div><h3>Configure developer environment</h3><p>승인된 Blueprint와 제한된 입력으로 개발 환경을 요청합니다.</p></div></div><div class="config-grid"><label class="config-field"><span>Project name</span><input name="project" value="${esc(state.project)}" pattern="[a-z0-9-]{3,30}" maxlength="30" required><small>Lowercase letters, numbers and hyphens</small></label><label class="config-field"><span>Environment</span><select name="environment">${options(['DEV','TEST','STG'],state.environment)}</select></label><label class="config-field"><span>Runtime</span><select name="runtime">${options(Object.keys(runtimeBlueprints),state.runtime)}</select></label><label class="config-field"><span>Database</span><select name="database">${options(['PostgreSQL','MySQL','None'],state.database)}</select></label></div><h4>Included controls</h4><div class="switch-list"><label class="switch-row"><div><strong>CI/CD pipeline</strong><small>Build and deployment workflow</small></div><b>INCLUDED</b><input type="checkbox" checked><i></i></label><label class="switch-row"><div><strong>Monitoring</strong><small>Metrics, logs and alert baseline</small></div><b>INCLUDED</b><input type="checkbox" checked><i></i></label></div></div><div class="wizard-actions"><a class="button" href="#/developer/catalog">← Catalog</a><button class="button primary" type="submit">Submit Request →</button></div></form><aside class="live-summary"><small>DEVELOPER PACKAGE · ${state.sku}</small><h3>${selected.name}</h3><p>${esc(state.project)}</p><dl><div><dt>Environment</dt><dd>${state.environment}</dd></div><div><dt>Blueprint</dt><dd>${runtimeBlueprints[state.runtime]}</dd></div><div><dt>Runtime</dt><dd>${state.runtime}</dd></div><div><dt>Database</dt><dd>${state.database}</dd></div><div><dt>Lifecycle</dt><dd class="auto">● AUTO</dd></div></dl><div><span>Estimated Cost <b>DEMO</b></span><strong>${money(selected.cost)}<small>/ month</small></strong></div></aside></div>`;
  }

  function requestDetail() {
    if(detailLoadState==='loading')return '<article class="request-detail-card"><p>Loading request details…</p></article>';
    if(detailError)return `<article class="request-detail-card"><p class="detail-error" role="alert">${esc(detailError)}</p></article>`;
    if(!selectedRequest)return '';
    const item=selectedRequest;
    const cancellable=item.requestStatus==='PENDING';
    const reason=item.rejectionReason||item.lastError;
    return `<article class="request-detail-card"><div class="request-detail-head"><div><small>REQUEST DETAIL</small><h3>${esc(item.project)}</h3><p>${esc(item.id)} · ${esc(item.blueprint)}</p></div><em class="domain-status ${item.status.toLowerCase()}">${esc(item.status)}</em></div><dl class="request-detail-grid"><div><dt>Request status</dt><dd>${esc(item.requestStatus)}</dd></div><div><dt>Delivery</dt><dd>${esc(item.deliveryStatus)}</dd></div><div><dt>Environment / Size</dt><dd>${esc(item.environment)}${item.size?` / ${esc(item.size)}`:''}</dd></div><div><dt>Created</dt><dd>${esc(item.created)}</dd></div><div><dt>Grant</dt><dd>${esc(item.grantId||'Not issued')}</dd></div><div><dt>Grant expires</dt><dd>${esc(item.grantExpiresAt||'—')}</dd></div><div><dt>Resource</dt><dd>${esc(item.resourceId||'Not provisioned')}</dd></div><div><dt>Resource status</dt><dd>${esc(item.resourceStatus||'—')}</dd></div></dl>${item.purpose?`<p class="request-purpose">${esc(item.purpose)}</p>`:''}${reason?`<p class="detail-error" role="alert">${esc(reason)}</p>`:''}<div class="request-detail-actions"><button type="button" class="button" data-request-close>Close</button>${cancellable?'<button type="button" class="button danger-button" data-request-cancel>Cancel pending request</button>':''}</div></article>`;
  }

  function requestList() {
    const stateNotice=requestLoadState==='loading'?'<p class="wizard-message">Loading authenticated request lifecycle…</p>':requestLoadError?`<p class="wizard-message" role="alert">${esc(requestLoadError)} <button type="button" data-request-retry>Retry</button></p>`:'';
    return `<div class="request-stats"><article><span>Total requests</span><strong>${requests.length}</strong></article><article><span>Active</span><strong>${requests.filter(item=>item.status==='ACTIVE').length}</strong></article><article><span>In review</span><strong>${requests.filter(item=>item.requestStatus==='PENDING').length}</strong></article></div>${stateNotice}<article class="data-card"><div class="card-head"><div><h3>Developer requests</h3><p>${demoMode?'DEMO DATA':'REQUEST → APPROVAL → TERRAFORM → GRANT'} · tenant isolated</p></div><a href="#/developer/configurator">New request →</a></div><div class="domain-rows request-rows">${requests.length?requests.map(item=>`<div><button type="button" class="request-id" data-request-id="${esc(item.id)}">${esc(item.id)}</button><span><b>${esc(item.project)}</b><small>${esc(item.sku)} · ${esc(item.environment)}</small></span><time>${esc(item.deliveryStatus||'Developer')}</time><em class="domain-status ${item.status.toLowerCase()}">${esc(item.status)}</em><button type="button" class="row-detail" data-request-id="${esc(item.id)}">Details →</button></div>`).join(''):'<p class="llm-usage-empty">No requests found for this authenticated user.</p>'}</div><div class="lifecycle-strip">${lifecycle.map(status=>`<span>${status}</span>`).join('<i>→</i>')}</div></article>${requestDetail()}`;
  }

  function safeEndpoint(value) { return /^https?:\/\//i.test(value||'') ? value : ''; }
  function resourceDetails(item) {
    const detailRows=Object.entries(item.details||{}).slice(0,4).map(([key,value])=>`<div><dt>${esc(key.replace(/_/g,' '))}</dt><dd>${esc(value)}</dd></div>`).join('');
    const endpoint=safeEndpoint(item.endpoint);
    return `<article><div><span>⌘</span><h3>${esc(item.name)}</h3></div><p>${esc(item.type)} · request ${esc(item.requestId||'—')}</p><dl>${detailRows||'<div><dt>Resource ID</dt><dd>'+esc(item.id)+'</dd></div>'}<div><dt>Updated</dt><dd>${esc(item.updated.slice(0,10))}</dd></div></dl><div class="resource-card-foot"><em class="domain-status ${item.status.toLowerCase()}">${esc(item.status)}</em>${endpoint?`<a href="${esc(endpoint)}" target="_blank" rel="noopener noreferrer">Open endpoint ↗</a>`:''}</div></article>`;
  }

  function infrastructure() {
    const notice=resourceLoadState==='loading'?'<p class="wizard-message resource-notice">Loading tenant resources…</p>':resourceLoadError?`<p class="wizard-message resource-notice" role="alert">${esc(resourceLoadError)} <button type="button" data-resource-retry>Retry</button></p>`:'';
    const content=resources.length?resources.map(resourceDetails).join(''):'<article class="resource-empty"><span>◇</span><h3>No provisioned resources</h3><p>Approved requests appear here after provisioning starts.</p><a class="button primary" href="#/developer/requests">View requests</a></article>';
    return `${notice}<div class="resource-grid">${content}</div>`;
  }

  function monitoring() { return `<article class="data-card"><div class="card-head"><div><h3>Developer service health</h3><p>Runtime and delivery signals</p></div><b class="domain-status active">ALL HEALTHY</b></div><div class="domain-rows"><div><strong>Runtime</strong><span><b>Application workloads</b><small>CPU · memory · restart count</small></span><time>Live</time><em class="domain-status active">NORMAL</em></div><div><strong>Delivery</strong><span><b>CI/CD pipelines</b><small>Build · deploy · rollback</small></span><time>5m ago</time><em class="domain-status active">NORMAL</em></div></div></article>`; }
  function finops() { return `<div class="metric-grid"><article><span>Current month</span><strong>${money(528000)}</strong><small class="demo-tag">DEMO DATA</small></article><article><span>Forecast</span><strong>${money(552000)}</strong><small>+4.5%</small></article><article><span>Budget used</span><strong>66%</strong><small>₩800,000 limit</small></article><article><span>Optimization</span><strong>${money(42000)}</strong><small>Potential savings</small></article></div>`; }

  function render(path) {
    if(path==='/developer/dashboard')return dashboard();
    if(path==='/developer/catalog')return catalog();
    if(path==='/developer/configurator')return configurator();
    if(path==='/developer/requests')return requestList();
    if(path==='/developer/infrastructure')return infrastructure();
    if(path==='/developer/monitoring')return monitoring();
    if(path==='/developer/finops')return finops();
    return '';
  }

  function blueprintPayload() {
    const selected=packages[state.sku];
    const blueprint=runtimeBlueprints[state.runtime];
    const size=blueprint==='VM_APPLICATION_STACK'?selected.size:(selected.size==='LARGE'?'STANDARD':selected.size);
    return {blueprint_id:blueprint,environment:state.environment,size,duration_hours:selected.duration,purpose:`Developer environment for ${state.project}`};
  }
  async function submit(form) {
    const button=form.querySelector('[type="submit"]');
    button.disabled=true;
    button.textContent='Submitting…';
    try {
      const selected=packages[state.sku];
      const context={project:state.project,sku:state.sku,blueprint:runtimeBlueprints[state.runtime],environment:state.environment};
      const item=await window.EclipseLifecycleAPI.submitBlueprint('developer',blueprintPayload(),context,()=>({request_id:`DEV-REQ-${String(105+requests.length).padStart(5,'0')}`,blueprint_id:context.blueprint,environment:state.environment,status:'PENDING',delivery_status:'DELIVERED',created_at:new Date().toISOString()}));
      requests.unshift(item);
      requestLoadState='ready';
      window.EclipseRouter.navigate('/developer/requests');
    } catch(error) {
      let message=form.querySelector('.wizard-message');
      if(!message){message=document.createElement('p');message.className='wizard-message';message.setAttribute('role','alert');form.append(message);}
      message.textContent=error.message;
      button.disabled=false;
      button.textContent='Submit Request →';
    }
  }
  async function loadRequests() {
    if(demoMode||requestLoadState==='loading'||requestLoadState==='ready')return;
    requestLoadState='loading';
    window.EclipseApp.refresh();
    try {
      const items=await window.EclipseLifecycleAPI.list('developer',requests);
      requests.splice(0,requests.length,...items);
      requestLoadState='ready';
      requestLoadError='';
    } catch(error) {
      requestLoadState='error';
      requestLoadError=error.message;
    }
    window.EclipseApp.refresh();
  }
  async function loadRequestDetail(requestId) {
    detailLoadState='loading';
    detailError='';
    selectedRequest=null;
    window.EclipseApp.refresh();
    try {
      selectedRequest=await window.EclipseLifecycleAPI.getRequest('developer',requestId,()=>requests.find(item=>item.id===requestId));
      detailLoadState='ready';
    } catch(error) {
      detailLoadState='error';
      detailError=error.message;
    }
    window.EclipseApp.refresh();
  }
  async function cancelSelectedRequest() {
    if(!selectedRequest||selectedRequest.requestStatus!=='PENDING')return;
    if(!window.confirm(`Cancel pending request ${selectedRequest.id}?`))return;
    const requestId=selectedRequest.id;
    detailLoadState='loading';
    window.EclipseApp.refresh();
    try {
      const cancelled=await window.EclipseLifecycleAPI.cancelRequest('developer',requestId,()=>requests.find(item=>item.id===requestId));
      const index=requests.findIndex(item=>item.id===requestId);
      if(index>=0)requests.splice(index,1,cancelled);
      selectedRequest=cancelled;
      detailLoadState='ready';
      detailError='';
    } catch(error) {
      detailLoadState='error';
      detailError=error.message;
    }
    window.EclipseApp.refresh();
  }
  async function loadResources(force) {
    if(resourceLoadState==='loading'||(!force&&resourceLoadState==='ready'))return;
    resourceLoadState='loading';
    resourceLoadError='';
    window.EclipseApp.refresh();
    try {
      const items=await window.EclipseLifecycleAPI.listResources('developer',resources);
      resources.splice(0,resources.length,...items);
      resourceLoadState='ready';
    } catch(error) {
      resourceLoadState='error';
      resourceLoadError=error.message;
    }
    window.EclipseApp.refresh();
  }

  function bind(root, path) {
    if(path==='/developer/catalog') {
      root.querySelectorAll('[data-dev-sku]').forEach(link=>link.addEventListener('click',()=>{state.sku=link.dataset.devSku;}));
      return;
    }
    if(path==='/developer/requests'){
      root.querySelectorAll('[data-request-id]').forEach(button=>button.addEventListener('click',()=>loadRequestDetail(button.dataset.requestId)));
      const close=root.querySelector('[data-request-close]');
      if(close)close.addEventListener('click',()=>{selectedRequest=null;detailLoadState='idle';detailError='';window.EclipseApp.refresh();});
      const cancel=root.querySelector('[data-request-cancel]');
      if(cancel)cancel.addEventListener('click',cancelSelectedRequest);
      const retry=root.querySelector('[data-request-retry]');
      if(retry)retry.addEventListener('click',()=>{requestLoadState='idle';requestLoadError='';loadRequests();});
      loadRequests();
      return;
    }
    if(path==='/developer/infrastructure'){
      const retry=root.querySelector('[data-resource-retry]');
      if(retry)retry.addEventListener('click',()=>loadResources(true));
      loadResources(false);
      return;
    }
    if(path!=='/developer/configurator')return;
    const form = root.querySelector('#developer-config');
    form.addEventListener('change',()=>{
      state.project=form.project.value;
      state.environment=form.environment.value;
      state.runtime=form.runtime.value;
      state.database=form.database.value;
      window.EclipseApp.refresh();
    });
    form.addEventListener('submit', event => {
      event.preventDefault();
      if(!form.checkValidity()){form.reportValidity();return;}
      state.project=form.project.value;
      state.environment=form.environment.value;
      state.runtime=form.runtime.value;
      state.database=form.database.value;
      submit(form);
    });
  }

  window.EclipseDeveloper = {render,bind,requests,resources,state,blueprintPayload,loadRequests,loadRequestDetail,loadResources};
}());
