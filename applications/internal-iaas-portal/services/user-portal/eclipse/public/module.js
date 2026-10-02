(function () {
  'use strict';
  // Public context owns its own request store and never imports another industry domain.
  const store = {requests:[
    {id:'PUB-REQ-00042',project:'citizen-portal',sku:'PUB-CP-STD',profile:'agency-standard',environment:'STG',status:'UNDER_REVIEW',cost:498000},
    {id:'PUB-REQ-00038',project:'welfare-notice',sku:'PUB-CP-MISSION',profile:'public-mission',environment:'PROD',status:'ACTIVE',cost:890000},
  ]};
  const state={agency:'Demo Public Agency',project:'citizen-portal',environment:'STG',profile:'agency-standard',networkZone:'Dedicated Public VPC',dataClass:'Personal',encryption:'Customer Managed Key',retention:'3 years'};
  const profiles={
    'department-pilot':{sku:'PUB-CP-PILOT',name:'Department Pilot',copy:'부서 단위 디지털 서비스 검증 환경',cost:286000,networkZone:'Shared Public Zone',dataClass:'Public',encryption:'Provider Managed Key',retention:'1 year',features:['Private service endpoint','Standard audit trail','Daily backup']},
    'agency-standard':{sku:'PUB-CP-STD',name:'Agency Standard',copy:'기관 업무와 대민서비스를 위한 표준 환경',cost:498000,networkZone:'Dedicated Public VPC',dataClass:'Personal',encryption:'Customer Managed Key',retention:'3 years',features:['Dedicated Public VPC','Personal data encryption','Immutable audit']},
    'public-mission':{sku:'PUB-CP-MISSION',name:'Public Mission',copy:'중요 공공서비스를 위한 고가용성 환경',cost:890000,networkZone:'Isolated Public Segment',dataClass:'Sensitive',encryption:'HSM Backed Key',retention:'5 years',features:['Isolated public segment','Multi-zone recovery','HSM-backed encryption']},
  };
  const serviceSkus=[{sku:'PUB-SVC-ONE',category:'DIGITAL PUBLIC SERVICE SUITE',name:'Digital Public Service',copy:'대민 접수부터 기관 처리와 결과 안내까지 하나의 공공서비스 패키지로 제공합니다.',requires:'PUB-CP-STD 이상',owner:'Public Service Delivery',status:'PLANNED',features:[
    {name:'온라인 민원',copy:'신청·본인확인·서류 제출 접점'},
    {name:'업무 처리',copy:'담당 부서 배정·검토·승인 워크플로'},
    {name:'대국민 알림',copy:'처리 상태와 결과를 채널별로 안내'},
  ]}];
  const lifecycle=['REQUESTED','CONSULTATION_REVIEW','APPROVED','PROVISIONING','ACTIVE'];
  const esc=value=>String(value==null?'':value).replace(/[&<>"']/g,ch=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[ch]));
  const money=value=>`₩${Number(value).toLocaleString('ko-KR')}`;
  const estimate=()=>profiles[state.profile]?.cost||498000;
  const options=(values,current)=>values.map(value=>`<option ${value===current?'selected':''}>${esc(value)}</option>`).join('');

  function applyProfile(profile) {
    const policy=profiles[profile];
    if(!policy)return;
    state.profile=profile;
    state.networkZone=policy.networkZone;
    state.dataClass=policy.dataClass;
    state.encryption=policy.encryption;
    state.retention=policy.retention;
    if(profile==='public-mission')state.environment='PROD';
  }
  function rows(items) {
    return `<div class="domain-rows">${items.map(item=>`<div><strong>${esc(item.id)}</strong><span><b>${esc(item.project)}</b><small>${esc(item.sku)} · ${esc(item.environment)}</small></span><time>${money(item.cost)}</time><em class="domain-status ${item.status.toLowerCase()}">${esc(item.status)}</em></div>`).join('')}</div>`;
  }
  function dashboard() {
    return `<div class="metric-grid public-metrics"><article><span>Active services</span><strong>2</strong><small>Public context only</small></article><article><span>Consultation review</span><strong>1</strong><small>Agency policy review</small></article><article><span>Monthly estimate</span><strong>${money(1388000)}</strong><small class="demo-tag">DEMO DATA</small></article><article><span>Service availability</span><strong>99.97%</strong><small>Current month</small></article></div><div class="domain-grid"><article class="data-card"><div class="card-head"><div><h3>Public service environments</h3><p>Agency-isolated delivery context</p></div><a href="#/public/requests">View requests →</a></div>${rows(store.requests)}</article><article class="notice public-assurance"><strong>Public assurance</strong><p>개인정보 암호화와 감사 기록이 표준 정책으로 적용됩니다.</p><span>POLICY ACTIVE</span></article></div>`;
  }
  function catalog() {
    return `<div class="finance-profiles public-profiles">${Object.entries(profiles).map(([id,profile])=>`<article class="${id===state.profile?'selected':''}"><small>${esc(profile.sku)} · ${id===state.profile?'SELECTED':'AVAILABLE'}</small><h3>${esc(profile.name)}</h3><p>${esc(profile.copy)}</p><ul>${profile.features.map(feature=>`<li>${esc(feature)}</li>`).join('')}</ul><div class="profile-price"><span>Estimated monthly</span><strong>${money(profile.cost)}</strong></div><a class="button primary" href="#/public/configurator" data-public-profile="${id}">Configure ${esc(profile.name)}</a></article>`).join('')}</div>`;
  }
  function configurator() {
    const policy=profiles[state.profile];
    return `<form id="public-config" class="wizard-card finance-config public-config"><div class="step-title"><span>P</span><div><h3>Public Digital Service Platform</h3><p>${esc(policy.sku)} · 기관별 공공서비스 정책으로 구성합니다.</p></div></div><div class="finance-policy-summary public-policy-summary"><div><small>${esc(policy.sku)} · ACTIVE POLICY</small><strong>${esc(policy.name)}</strong><span>${esc(policy.copy)}</span></div>${policy.features.map(feature=>`<b>✓ ${esc(feature)}</b>`).join('')}</div><div class="config-grid"><label class="config-field"><span>Agency</span><input name="agency" value="${esc(state.agency)}" minlength="2" maxlength="80" required></label><label class="config-field"><span>Project</span><input name="project" value="${esc(state.project)}" required pattern="[a-z][a-z0-9-]{2,39}"></label><label class="config-field"><span>Environment</span><select name="environment">${options(['DEV','STG','PROD'],state.environment)}</select></label><label class="config-field"><span>Policy profile</span><select name="profile">${options(Object.keys(profiles),state.profile)}</select></label><label class="config-field"><span>Network zone</span><select name="networkZone">${options(['Shared Public Zone','Dedicated Public VPC','Isolated Public Segment'],state.networkZone)}</select></label><label class="config-field"><span>Data classification</span><select name="dataClass">${options(['Public','Personal','Sensitive'],state.dataClass)}</select></label><label class="config-field"><span>Encryption</span><select name="encryption">${options(['Provider Managed Key','Customer Managed Key','HSM Backed Key'],state.encryption)}</select></label><label class="config-field"><span>Audit retention</span><select name="retention">${options(['1 year','3 years','5 years'],state.retention)}</select></label></div><div class="switch-list"><label class="switch-row"><div><strong>Immutable audit</strong><small>기관별 변경 이력과 관리자 활동 기록</small></div><b>REQUIRED</b><input type="checkbox" checked disabled><i></i></label><label class="switch-row"><div><strong>Accessibility baseline</strong><small>대민서비스 접근성 검토 항목 포함</small></div><b>INCLUDED</b><input type="checkbox" checked disabled><i></i></label></div><div class="finance-estimate public-estimate"><span>${esc(policy.sku)} · Estimated monthly cost · DEMO DATA</span><strong>${money(estimate())}</strong></div><div class="wizard-actions"><a class="button" href="#/public/catalog">← Back</a><button class="button primary" type="submit">Submit Public Request →</button></div></form>`;
  }
  function requests() {
    return `<div class="request-stats"><article><span>Public requests</span><strong>${store.requests.length}</strong></article><article><span>Consultation review</span><strong>${store.requests.filter(item=>item.status==='CONSULTATION_REVIEW'||item.status==='UNDER_REVIEW').length}</strong></article><article><span>Active</span><strong>${store.requests.filter(item=>item.status==='ACTIVE').length}</strong></article></div><article class="data-card"><div class="card-head"><div><h3>Public service requests</h3><p>Separate public-sector data context</p></div><a href="#/public/configurator">New request →</a></div>${rows(store.requests)}<div class="lifecycle-strip">${lifecycle.map(status=>`<span>${status}</span>`).join('<i>→</i>')}</div></article>`;
  }
  function render(path) {
    if(path==='/public/dashboard')return dashboard();
    if(path==='/public/catalog')return catalog();
    if(path==='/public/configurator')return configurator();
    if(path==='/public/requests')return requests();
    if(path==='/public/services')return window.EclipseCatalog.renderServiceSkus({eyebrow:'PUBLIC SERVICE · ONE PACKAGE',title:'하나의 흐름으로 연결하는 디지털 공공서비스',copy:'온라인 민원, 기관 업무 처리, 대국민 알림을 하나의 서비스 수명주기로 관리합니다.',items:serviceSkus});
    return '';
  }
  function payload() {
    return {sku:profiles[state.profile].sku,agency:state.agency,project:state.project,environment:state.environment,profile:state.profile,configuration:{network_zone:state.networkZone,data_classification:state.dataClass,encryption:state.encryption,audit_retention:state.retention,immutable_audit:true,accessibility_baseline:true,cost_estimate_krw:estimate()}};
  }
  async function submit(form) {
    const button=form.querySelector('[type="submit"]');
    button.disabled=true;
    button.textContent='Submitting…';
    try {
      const item=await window.EclipseDomainAPI.post('public','/public/requests',payload(),()=>({id:`PUB-REQ-${String(43+store.requests.length).padStart(5,'0')}`,sku:profiles[state.profile].sku,project:state.project,environment:state.environment,status:'CONSULTATION_REVIEW',configuration:{cost_estimate_krw:estimate()}}));
      store.requests.unshift({id:item.id,sku:item.sku||profiles[state.profile].sku,project:item.project,profile:state.profile,environment:item.environment,status:item.status,cost:item.configuration?.cost_estimate_krw||estimate()});
      window.EclipseRouter.navigate('/public/requests');
    } catch(error) {
      let message=form.querySelector('.wizard-message');
      if(!message){message=document.createElement('p');message.className='wizard-message';message.setAttribute('role','alert');form.append(message);}
      message.textContent=error.message;
      button.disabled=false;
      button.textContent='Submit Public Request →';
    }
  }
  function syncForm(form) {
    const values=new FormData(form);
    const nextProfile=values.get('profile');
    if(nextProfile!==state.profile){applyProfile(nextProfile);return;}
    values.forEach((value,key)=>{if(key in state)state[key]=value;});
  }
  function bind(root,path) {
    if(path==='/public/catalog')root.querySelectorAll('[data-public-profile]').forEach(link=>link.addEventListener('click',()=>applyProfile(link.dataset.publicProfile)));
    if(path!=='/public/configurator')return;
    const form=root.querySelector('#public-config');
    if(!form)return;
    form.addEventListener('change',()=>{syncForm(form);window.EclipseApp.refresh();});
    form.addEventListener('submit',event=>{event.preventDefault();syncForm(form);if(form.checkValidity())submit(form);else form.reportValidity();});
  }
  window.EclipsePublic={render,bind,store,state,profiles,serviceSkus,applyProfile};
}());
