(function () {
  'use strict';

  const mock = {
    tenants: [
      {id:'abc-manufacturing',name:'ABC Manufacturing',industry:'Manufacturing',environments:3,status:'ACTIVE'},
      {id:'hanbit-mobility',name:'Hanbit Mobility',industry:'Manufacturing',environments:2,status:'ACTIVE'},
      {id:'demo-finance',name:'Demo Finance',industry:'Finance',environments:1,status:'PILOT'},
      {id:'demo-public-agency',name:'Demo Public Agency',industry:'Public',environments:2,status:'PILOT'},
    ],
    requests: [
      {request_id:'REQ-00294',requester_id:'kim.manager',product_code:'Cloud Platform',environment:'PROD',status:'PENDING',purpose:'MES API production environment',updated_at:'2026-09-11T08:20:00+09:00'},
      {request_id:'REQ-00293',requester_id:'lee.dev',product_code:'Cloud Platform',environment:'DEV',status:'APPROVED',purpose:'Quality dashboard development',updated_at:'2026-09-11T07:45:00+09:00'},
      {request_id:'REQ-00290',requester_id:'park.dev',product_code:'Cloud Platform',environment:'STG',status:'REJECTED',purpose:'Integration test',rejection_reason:'PROD 수준의 백업 정책을 선택하고 예상 트래픽 근거를 추가해 다시 신청해 주세요.',feedback_source:'POLICY_ASSISTANT',updated_at:'2026-09-10T16:12:00+09:00'},
    ],
    jobs: [
      {job_id:'JOB-1042',operation:'APPLY',product_code:'Cloud Platform',module_name:'ktcloud-platform',module_version:'1.2.0',status:'APPLYING',attempts:1,runner_id:'runner-a',updated_at:'2026-09-11T08:31:00+09:00'},
      {job_id:'JOB-1041',operation:'APPLY',product_code:'Cloud Platform',module_name:'aws-platform',module_version:'1.2.0',status:'SUCCEEDED',attempts:1,runner_id:'runner-b',updated_at:'2026-09-11T08:05:00+09:00'},
      {job_id:'JOB-1038',operation:'DESTROY',product_code:'Cloud Platform',module_name:'ktcloud-platform',module_version:'1.1.4',status:'DESTROY_FAILED',attempts:2,runner_id:'runner-a',updated_at:'2026-09-10T19:42:00+09:00'},
    ],
    audits: [
      {at:'2026-09-11 08:32',actor:'terraform-runner',action:'PROVISIONING_STARTED',target:'REQ-00294',result:'SUCCESS'},
      {at:'2026-09-11 08:22',actor:'msp-admin',action:'REQUEST_APPROVED',target:'REQ-00294',result:'SUCCESS'},
      {at:'2026-09-10 19:42',actor:'runner-a',action:'DESTROY_CALLBACK',target:'JOB-1038',result:'FAILED'},
    ],
    grants: [
      {grant_id:'GRANT-00841',request_id:'REQ-00293',idempotency_key:'grant:REQ-00293:3',subject_id:'lee.dev',scopes:['resource:read','resource:operate'],status:'ACTIVE',issued_at:'2026-09-29T02:10:00Z',expires_at:'2026-10-06T02:10:00Z',event_version:3,callback_status:'DELIVERED',retry_count:0,last_error:null,updated_at:'2026-09-29T02:10:00Z'},
      {grant_id:'GRANT-00837',request_id:'REQ-00287',idempotency_key:'grant:REQ-00287:4',subject_id:'park.dev',scopes:['resource:read'],status:'EXPIRED',issued_at:'2026-09-20T01:00:00Z',expires_at:'2026-09-27T01:00:00Z',event_version:4,callback_status:'DELIVERED',retry_count:0,last_error:null,updated_at:'2026-09-27T01:00:00Z'},
      {grant_id:'GRANT-00832',request_id:'REQ-00280',idempotency_key:'grant:REQ-00280:4',subject_id:'kim.manager',scopes:['resource:read','resource:operate'],status:'REVOKED',issued_at:'2026-09-18T03:20:00Z',expires_at:'2026-10-02T03:20:00Z',revoked_at:'2026-09-22T06:15:00Z',event_version:4,callback_status:'DELIVERED',retry_count:0,last_error:null,updated_at:'2026-09-22T06:15:00Z'},
    ],
    users: [
      {name:'MSP Administrator',userId:'msp-admin',tenant:'Eclipse Cloud MSP',role:'MSP_ADMIN',scopes:'admin:write · audit:read · llm:invoke',status:'ACTIVE'},
      {name:'MSP Operator',userId:'msp-operator',tenant:'Eclipse Cloud MSP',role:'MSP_OPERATOR',scopes:'approval:manage · terraform:read',status:'ACTIVE'},
      {name:'Developer User',userId:'developer-user',tenant:'Eclipse Developer Demo',role:'CUSTOMER_USER',scopes:'developer:read · llm:invoke',status:'ACTIVE'},
      {name:'Factory User',userId:'factory-user',tenant:'Hanbit Mobility',role:'CUSTOMER_USER',scopes:'manufacturing:read · llm:invoke',status:'ACTIVE'},
      {name:'Finance User',userId:'finance-user',tenant:'Demo Finance',role:'CUSTOMER_USER',scopes:'finance:read · llm:invoke',status:'ACTIVE'},
      {name:'Public User',userId:'public-user',tenant:'Demo Public Agency',role:'CUSTOMER_USER',scopes:'public:read · llm:invoke',status:'ACTIVE'},
      {name:'LLM User',userId:'llm-user',tenant:'ABC Manufacturing',role:'LLM_USER',scopes:'llm:invoke · llm:usage:read',status:'ACTIVE'},
    ],
  };
  const store = {tenants:mock.tenants.slice(),requests:mock.requests.slice(),jobs:mock.jobs.slice(),audits:mock.audits.slice(),grants:mock.grants.slice(),users:mock.users.slice(),loading:false,error:''};
  const loadedPaths = new Set();
  let selectedTenant = null;
  let selectedGrant = null;
  let pendingDecision = null;
  let promotionMessage = '';
  const esc = value => String(value == null ? '' : value).replace(/[&<>"']/g, char => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[char]));
  const date = value => value ? new Date(value).toLocaleString('ko-KR') : '-';
  const badge = value => `<em class="domain-status ${esc(String(value).toLowerCase())}">${esc(value)}</em>`;
  const error = () => store.error ? `<div class="notice admin-error"><strong>API connection</strong><p>${esc(store.error)} · 표시된 항목은 DEMO DATA입니다.</p></div>` : '';

  function dashboard() {
    const pending=store.requests.filter(item=>item.status==='PENDING').length;
    const activeJobs=store.jobs.filter(item=>['QUEUED','PLANNING','APPLYING','DESTROYING'].includes(item.status)).length;
    const failed=store.jobs.filter(item=>String(item.status).includes('FAILED')).length;
    return `${error()}<div class="metric-grid"><article><span>Active tenants</span><strong>${store.tenants.filter(item=>item.status==='ACTIVE').length}</strong><small>Across MSP platform</small></article><article><span>Approval queue</span><strong>${pending}</strong><small>Awaiting operator decision</small></article><article><span>Active Terraform jobs</span><strong>${activeJobs}</strong><small>Runner queue</small></article><article><span>Failed operations</span><strong>${failed}</strong><small>${failed?'Action required':'All healthy'}</small></article></div><div class="domain-grid"><article class="data-card"><div class="card-head"><div><h3>Recent requests</h3><p>Approval and callback state</p></div><a href="#/admin/approvals">Open queue →</a></div>${requestRows(store.requests.slice(0,3),false)}</article><article class="data-card"><div class="card-head"><div><h3>Platform topology</h3><p>Tier 1 target architecture</p></div></div><div class="topology-list"><div><span>AWS</span><strong>MSP Platform</strong><small>Portal · API · Runner · Metadata DB</small></div><i>IPsec VPN</i><div><span>KT</span><strong>Tenant Workloads</strong><small>Compute · Kubernetes · Database · Storage</small></div></div></article></div>`;
  }
  function tenantRows() { return `<div class="admin-table"><div class="table-head"><span>Tenant</span><span>Industry</span><span>Environments</span><span>Status</span></div>${store.tenants.map(item=>`<div><span><strong>${esc(item.name)}</strong><small>${esc(item.id)}</small></span><span>${esc(item.industry)}</span><span>${esc(item.environments)}</span><span>${badge(item.status)}</span></div>`).join('')}</div>`; }
  function tenants() { return `${error()}<article class="data-card"><div class="card-head"><div><h3>Customer tenants</h3><p>MSP_ADMIN restricted · DEMO DATA</p></div></div>${tenantRows()}</article>`; }
  function users() {
    const customerUsers=store.users.filter(item=>item.role.startsWith('CUSTOMER_')).length;
    const mspUsers=store.users.filter(item=>item.role.startsWith('MSP_')).length;
    const candidates=store.users.filter(item=>item.role==='CUSTOMER_USER');
    const candidateOptions=candidates.map(item=>`<option value="${esc(item.userId)}">${esc(item.name)} · ${esc(item.tenant)}</option>`).join('');
    const promotionNotice=promotionMessage?`<p class="promotion-success" role="status">${esc(promotionMessage)}</p>`:'';
    return `<div class="request-stats identity-summary"><article><span>All identities</span><strong>${store.users.length}</strong></article><article><span>Customer users</span><strong>${customerUsers}</strong></article><article><span>MSP operators</span><strong>${mspUsers}</strong></article></div><article class="domain-promotion-card"><div><small>INDUSTRY ACCESS UPGRADE</small><h3>상담 완료 고객 권한 승격</h3><p>신규 회원은 Developer로 시작합니다. 상담이 끝난 고객만 MSP_ADMIN이 산업 도메인으로 변경할 수 있습니다.</p><div class="promotion-flow"><span>Developer signup</span><i>→</i><span>Consultation</span><i>→</i><span>MSP approval</span></div><small class="public-plan">Public 승격 시 공공 전용 포털과 정책 상품이 활성화됩니다.</small></div><form id="domain-promotion-form"><label><span>Customer identity</span><select name="userId" required>${candidateOptions}</select></label><label><span>Approved domain</span><select name="domain" required><option value="manufacturing">Manufacturing</option><option value="finance">Finance</option><option value="public">Public</option></select></label><label class="promotion-reason"><span>Consultation note</span><textarea name="reason" minlength="5" maxlength="300" placeholder="상담 완료 내용과 승인 근거를 입력하세요." required></textarea></label>${promotionNotice}<button class="button primary" type="submit">Apply domain access <span>→</span></button></form></article><article class="data-card"><div class="card-head"><div><h3>Portal identities</h3><p>MSP_ADMIN restricted · DEMO DATA</p></div><b>RBAC assignments</b></div><div class="identity-table admin-identity-table"><div class="table-head"><span>Identity</span><span>Tenant</span><span>Role</span><span>Effective scopes</span><span>Status</span></div>${store.users.map(item=>`<div><span><strong>${esc(item.name)}</strong><small>${esc(item.userId)}</small></span><span>${esc(item.tenant)}</span><span><code>${esc(item.role)}</code></span><span>${esc(item.scopes)}</span><span>${badge(item.status)}</span></div>`).join('')}</div></article><div class="role-contracts"><article><small>CUSTOMER</small><strong>Developer first</strong><p>회원가입은 developer:read만 발급하고 제조·금융·공공 권한은 상담 후 승격합니다.</p></article><article><small>MSP</small><strong>Admin approved</strong><p>산업 권한 승격과 관리자 전용 Tenant·User·Audit 화면은 MSP_ADMIN만 접근합니다.</p></article><article><small>LLM</small><strong>Explicit entitlement</strong><p>llm:invoke 또는 llm:usage:read scope가 있어야 메뉴와 API를 사용할 수 있습니다.</p></article></div>`;
  }
  function promoteDomain(form) {
    const values=new FormData(form);
    const user=store.users.find(item=>item.userId===values.get('userId'));
    const domain=String(values.get('domain'));
    const scopeByDomain={manufacturing:'manufacturing:read',finance:'finance:read',public:'public:read'};
    if(!user||!scopeByDomain[domain])return;
    const retainedScopes=user.scopes.split(' · ').filter(scope=>!['developer:read','manufacturing:read','finance:read','public:read'].includes(scope));
    user.scopes=[scopeByDomain[domain],...retainedScopes].join(' · ');
    user.domain=domain;
    user.consultation='COMPLETED';
    user.consultationNote=String(values.get('reason')).trim();
    store.audits.unshift({at:new Date().toLocaleString('ko-KR'),actor:'msp-admin',action:'DOMAIN_ACCESS_PROMOTED',target:`${user.userId} · ${domain}`,result:'SUCCESS'});
    promotionMessage=`${user.name}의 권한을 ${scopeByDomain[domain]}로 변경했습니다.`;
    window.EclipseApp.refresh();
  }
  function requestRows(items,actions=true) { return `<div class="admin-table approval-table"><div class="table-head"><span>Request</span><span>Requester / Purpose</span><span>Environment</span><span>Status</span>${actions?'<span>Action</span>':''}</div>${items.map(item=>`<div><span><strong>${esc(item.request_id)}</strong><small>${esc(item.product_code)}</small></span><span><strong>${esc(item.requester_id)}</strong><small>${esc(item.purpose)}</small>${item.rejection_reason?`<small class="decision-reason"><b>${esc(item.feedback_source||'OPERATOR')}</b> ${esc(item.rejection_reason)}</small>`:''}</span><span>${esc(item.environment || item.parameters?.environment || '-')}</span><span>${badge(item.status)}</span>${actions?`<span class="row-actions">${item.status==='PENDING'?`<button data-decision="approve" data-id="${esc(item.request_id)}">Approve</button><button class="danger" data-decision="reject" data-id="${esc(item.request_id)}">Reject</button>`:'-'}</span>`:''}</div>`).join('')}</div>`; }
  function decisionPanel() { if(!pendingDecision)return ''; const item=store.requests.find(request=>request.request_id===pendingDecision.id); if(!item)return ''; const approve=pendingDecision.action==='approve'; return `<article class="admin-decision"><div><small>REQUEST DECISION</small><h3>${approve?'Approve':'Reject'} ${esc(item.request_id)}</h3><p>${esc(item.requester_id)} · ${esc(item.environment)} · ${esc(item.purpose)}</p></div><form id="admin-decision-form"><label><span>Decision reason</span><textarea name="reason" minlength="5" maxlength="500" required>${approve?'Approved after policy and capacity review.':'Rejected after policy review.'}</textarea></label><div><button type="button" class="button" data-cancel-decision>Cancel</button><button type="submit" class="button ${approve?'primary':'danger-button'}">Confirm ${approve?'approval':'rejection'}</button></div></form></article>`; }
  function approvals() { const pending=store.requests.filter(item=>item.status==='PENDING'); return `${error()}${decisionPanel()}<article class="data-card"><div class="card-head"><div><h3>Approval queue</h3><p>Existing Approval API contract</p></div><b>${pending.length} PENDING</b></div>${requestRows(store.requests)}</article>`; }
  function tenantDetail(item,index) { const placement=index===2?'AWS':'KT Cloud'; const monthly=['₩754,000','₩398,000','₩132,000'][index]||'₩0'; const requests=store.requests.filter(request=>request.requester_id.includes(index===0?'kim':index===1?'lee':'park')).length; return `<article class="admin-tenant-detail"><div class="review-head"><div><small>TENANT CONTROL PLANE</small><h3>${esc(item.name)}</h3><p>${esc(item.id)} · ${esc(item.industry)}</p></div><button class="button" data-close-tenant>Close</button></div><div class="admin-detail-grid"><div><small>STATUS</small><strong class="auto">● ${esc(item.status)}</strong></div><div><small>CLOUD PLACEMENT</small><strong>${placement}</strong></div><div><small>ENVIRONMENTS</small><strong>${esc(item.environments)}</strong></div><div><small>OPEN REQUESTS</small><strong>${requests}</strong></div><div><small>MONTHLY COST</small><strong>${monthly}</strong></div><div><small>NETWORK</small><strong>Tenant subnet</strong></div><div><small>ACCESS</small><strong>RBAC + JIT grant</strong></div><div><small>DATA SCOPE</small><strong>Schema isolated</strong></div></div><div class="tenant-services"><span>Compute <b>Healthy</b></span><span>Kubernetes <b>${item.environments>1?'Active':'Standby'}</b></span><span>Database <b>Protected</b></span><span>Monitoring <b>Enabled</b></span></div></article>`; }
  function infrastructure() { const selectedIndex=store.tenants.findIndex(item=>item.id===selectedTenant); const detail=selectedIndex>=0?tenantDetail(store.tenants[selectedIndex],selectedIndex):''; return `${detail}<div class="resource-grid">${store.tenants.map((item,index)=>`<article><div><span>${esc(item.name.slice(0,1))}</span><h3>${esc(item.name)}</h3></div><p>${esc(item.id)} · ${esc(item.industry)}</p><dl><div><dt>Environments</dt><dd>${esc(item.environments)}</dd></div><div><dt>Cloud placement</dt><dd>${index===2?'AWS':'KT Cloud'}</dd></div><div><dt>Tenant isolation</dt><dd>Subnet · RBAC · Schema</dd></div><div><dt>Status</dt><dd class="auto">● ${esc(item.status)}</dd></div></dl><button class="button" data-tenant-detail="${esc(item.id)}">View tenant resources</button></article>`).join('')}</div>`; }
  function terraform() { return `${error()}<article class="data-card"><div class="card-head"><div><h3>Terraform jobs</h3><p>Approved modules and runner callbacks</p></div></div><div class="admin-table jobs-table"><div class="table-head"><span>Operation</span><span>Module</span><span>Status</span><span>Attempts</span><span>Runner / Updated</span></div>${store.jobs.map(item=>`<div><span><strong>${esc(item.operation)}</strong><small>${esc(item.product_code)}</small></span><span><strong>${esc(item.module_name)}</strong><small>v${esc(item.module_version)}</small></span><span>${badge(item.status)}</span><span>${esc(item.attempts)}</span><span><strong>${esc(item.runner_id||'-')}</strong><small>${esc(date(item.updated_at))}</small></span></div>`).join('')}</div></article>`; }
  function grantDetail() {
    if(!selectedGrant)return '';
    const item=selectedGrant;
    return `<article class="grant-detail"><div class="review-head"><div><small>GRANT DETAIL · READ ONLY</small><h3>${esc(item.grant_id)}</h3><p>${esc(item.subject_id)} · ${esc(item.request_id)}</p></div><div><span>${badge(item.status)}</span><button class="button" data-close-grant>Close</button></div></div><div class="grant-detail-grid"><div><small>SCOPES</small><strong>${(item.scopes||[]).map(esc).join(' · ')||'-'}</strong></div><div><small>ISSUED</small><strong>${esc(date(item.issued_at))}</strong></div><div><small>EXPIRES</small><strong>${esc(date(item.expires_at))}</strong></div><div><small>EVENT VERSION</small><strong>v${esc(item.event_version||'-')}</strong></div><div><small>CALLBACK</small><strong>${esc(item.callback_status||'PENDING')}</strong></div><div><small>RETRIES</small><strong>${esc(item.retry_count||0)}</strong></div><div><small>IDEMPOTENCY KEY</small><strong>${esc(item.idempotency_key||'-')}</strong></div><div><small>UPDATED</small><strong>${esc(date(item.updated_at))}</strong></div></div>${item.last_error?`<p class="grant-detail-error"><strong>Last error</strong>${esc(item.last_error)}</p>`:'<p class="grant-detail-ok">No delivery errors reported.</p>'}</article>`;
  }
  function grants() {
    const active=store.grants.filter(item=>item.status==='ACTIVE').length;
    const expired=store.grants.filter(item=>item.status==='EXPIRED').length;
    const revoked=store.grants.filter(item=>item.status==='REVOKED').length;
    const rows=store.grants.map(item=>`<div><span><strong>${esc(item.grant_id)}</strong><small>${esc(item.request_id)}</small></span><span><strong>${esc(item.subject_id)}</strong><small>${(item.scopes||[]).map(esc).join(' · ')}</small></span><span>${badge(item.status)}</span><span><strong>${esc(date(item.expires_at))}</strong><small>${item.revoked_at?`Revoked ${esc(date(item.revoked_at))}`:`Updated ${esc(date(item.updated_at))}`}</small></span><span><strong>${esc(item.callback_status||'PENDING')}</strong><small>${item.retry_count?`${esc(item.retry_count)} retries`:'No retries'}</small></span><span><button class="button grant-detail-button" data-grant-detail="${esc(item.grant_id)}">View</button></span></div>`).join('');
    return `${error()}${grantDetail()}<div class="request-stats grant-summary"><article><span>All grants</span><strong>${store.grants.length}</strong></article><article><span>Active</span><strong>${active}</strong></article><article><span>Expired / Revoked</span><strong>${expired+revoked}</strong></article></div><article class="grant-policy"><div><small>JIT ACCESS CONTROL</small><h3>승인된 요청에만 시간 제한 Grant 발급</h3><p>Grant API의 관리자 조회 계약을 사용합니다. 회수와 강제 만료는 리소스 정리까지 유발하므로 이 화면에서는 읽기 전용으로 유지합니다.</p></div><dl><div><dt>Active</dt><dd>Scope + expiry enforced</dd></div><div><dt>Expired</dt><dd>Automatic deprovision path</dd></div><div><dt>Revoked</dt><dd>Immediate access removal</dd></div></dl></article><article class="data-card"><div class="card-head"><div><h3>Access grants</h3><p>${isMock()?'DEMO DATA':'GRANT API'} · grant-admin restricted</p></div><b>${active} ACTIVE</b></div><div class="admin-table grants-table"><div class="table-head"><span>Grant / Request</span><span>Subject / Scopes</span><span>Status</span><span>Expires</span><span>Callback</span><span>Detail</span></div>${rows||'<p class="llm-usage-empty">No grants found.</p>'}</div></article>`;
  }
  function monitoring() { return `<div class="monitor-grid"><article class="service-gauge"><small>SERVICE STATUS</small><strong>● Healthy</strong><p>Portal and APIs · 2 replicas target</p></article><article class="service-gauge"><small>TERRAFORM RUNNER</small><strong>● Operational</strong><p>1 active · 1 standby target</p></article><article class="service-gauge"><small>VPN PATH</small><strong>● Connected</strong><p>IPsec primary · dedicated line planned</p></article></div><article class="data-card monitoring-preview"><div><small>CPU</small><strong>43%</strong></div><div><small>Memory</small><strong>61%</strong></div><div><small>API p95</small><strong>184ms</strong></div><div><small>Error rate</small><strong>0.08%</strong></div><a class="button" href="#/admin/monitoring">Open Grafana ↗</a><small class="demo-tag">DEMO DATA</small></article>`; }
  function finops() { return `<div class="metric-grid"><article><span>Tenant cloud cost</span><strong>₩1,284,000</strong><small>KT Cloud · DEMO DATA</small></article><article><span>MSP platform cost</span><strong>₩417,000</strong><small>AWS shared platform</small></article><article><span>Projected total</span><strong>₩2,341,000</strong><small>Current month forecast</small></article><article><span>Night shutdown saving</span><strong>₩188,000</strong><small>Estimated saving</small></article></div><article class="data-card cost-allocation"><div class="card-head"><div><h3>Cost allocation</h3><p>Tenant tagging rule · DEMO DATA</p></div></div>${store.tenants.map((item,index)=>`<div><span>${esc(item.name)}</span><i><b style="width:${[82,54,31][index]}%"></b></i><strong>${['₩754,000','₩398,000','₩132,000'][index]}</strong></div>`).join('')}</article>`; }
  function audit() { return `${error()}<article class="data-card"><div class="card-head"><div><h3>Audit events</h3><p>MSP_ADMIN restricted · immutable history</p></div></div><div class="admin-table audit-table"><div class="table-head"><span>Time</span><span>Actor</span><span>Action</span><span>Target</span><span>Result</span></div>${store.audits.map(item=>`<div><span>${esc(item.at || date(item.created_at))}</span><span>${esc(item.actor || item.actor_id)}</span><span>${esc(item.action || item.event_type)}</span><span>${esc(item.target || item.entity_id)}</span><span>${badge(item.result || 'SUCCESS')}</span></div>`).join('')}</div></article>`; }
  function render(path) { if(path==='/admin/dashboard')return dashboard();if(path==='/admin/tenants')return tenants();if(path==='/admin/users')return users();if(path==='/admin/approvals')return approvals();if(path==='/admin/grants')return grants();if(path==='/admin/infrastructure')return infrastructure();if(path==='/admin/terraform')return terraform();if(path==='/admin/monitoring')return monitoring();if(path==='/admin/finops')return finops();if(path==='/admin/audit')return audit();return ''; }

  async function decide(id,action,reason,button) {
    const item=store.requests.find(request=>request.request_id===id); if(!item)return;
    button.disabled=true;
    try { if(!isMock()) await window.EclipseAPI.post(`/admin-api/v1/requests/${encodeURIComponent(id)}/${action}`,{reason}); item.status=action==='approve'?'APPROVED':'REJECTED'; if(action==='reject'){item.rejection_reason=reason;item.feedback_source='MSP_OPERATOR';} store.error=''; pendingDecision=null; }
    catch (reason) { store.error=reason.message; }
    window.EclipseApp.refresh();
  }
  function isMock() { return (window.ECLIPSE_RUNTIME_CONFIG.mockDomains||[]).includes('admin'); }
  async function openGrant(id,button) {
    if(button)button.disabled=true;
    try {
      selectedGrant=isMock()?store.grants.find(item=>item.grant_id===id):await window.EclipseAPI.get(`/admin-api/v1/grants/${encodeURIComponent(id)}`);
      if(!selectedGrant)throw new Error('Grant not found');
      store.error='';
    } catch (reason) { store.error=reason.message; }
    finally { if(button)button.disabled=false; window.EclipseApp.refresh(); }
  }
  async function hydrate(path) {
    if(isMock() || store.loading || loadedPaths.has(path))return;
    loadedPaths.add(path);
    store.loading=true;
    try {
      if(path==='/admin/dashboard'||path==='/admin/approvals') store.requests=await window.EclipseAPI.get('/admin-api/v1/requests?status=ALL');
      if(path==='/admin/dashboard'||path==='/admin/terraform') store.jobs=await window.EclipseAPI.get('/admin-api/v1/provisioning/jobs?status=ALL');
      if(path==='/admin/grants') store.grants=await window.EclipseAPI.get('/admin-api/v1/grants?status=ALL');
      if(path==='/admin/audit') store.audits=await window.EclipseAPI.get('/admin-api/v1/audit-events');
      store.error='';
    } catch (reason) { store.error=reason.message; }
    finally { store.loading=false; window.EclipseApp.refresh(); }
  }
  function bind(root,path) {
    root.querySelectorAll('[data-decision]').forEach(button=>button.addEventListener('click',()=>{pendingDecision={id:button.dataset.id,action:button.dataset.decision};window.EclipseApp.refresh();}));
    const decisionForm=root.querySelector('#admin-decision-form');if(decisionForm)decisionForm.addEventListener('submit',event=>{event.preventDefault();const button=decisionForm.querySelector('[type="submit"]');const reason=new FormData(decisionForm).get('reason');if(decisionForm.checkValidity())decide(pendingDecision.id,pendingDecision.action,reason,button);else decisionForm.reportValidity();});
    const cancel=root.querySelector('[data-cancel-decision]');if(cancel)cancel.addEventListener('click',()=>{pendingDecision=null;window.EclipseApp.refresh();});
    root.querySelectorAll('[data-tenant-detail]').forEach(button=>button.addEventListener('click',()=>{selectedTenant=button.dataset.tenantDetail;window.EclipseApp.refresh();}));
    const closeTenant=root.querySelector('[data-close-tenant]');if(closeTenant)closeTenant.addEventListener('click',()=>{selectedTenant=null;window.EclipseApp.refresh();});
    root.querySelectorAll('[data-grant-detail]').forEach(button=>button.addEventListener('click',()=>openGrant(button.dataset.grantDetail,button)));
    const closeGrant=root.querySelector('[data-close-grant]');if(closeGrant)closeGrant.addEventListener('click',()=>{selectedGrant=null;window.EclipseApp.refresh();});
    const promotionForm=root.querySelector('#domain-promotion-form');if(promotionForm)promotionForm.addEventListener('submit',event=>{event.preventDefault();if(promotionForm.checkValidity())promoteDomain(promotionForm);else promotionForm.reportValidity();});
    hydrate(path);
  }
  function reload(path) { loadedPaths.delete(path); return hydrate(path); }
  window.EclipseAdmin={render,bind,reload,openGrant,store};
}());
