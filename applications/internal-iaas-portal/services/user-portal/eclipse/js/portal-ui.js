(function () {
  'use strict';
  const esc = value => String(value ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const money = value => value == null ? '수집되지 않음' : `₩${Number(value).toLocaleString('ko-KR')}`;
  const badge = value => `<em class="domain-status">${esc(value)}</em>`;
  const card = (title, body, note='') => `<article class="data-card"><div class="card-head"><div><h3>${esc(title)}</h3><p>${esc(note)}</p></div></div>${body}</article>`;
  const metrics = items => `<div class="metric-grid">${items.map(([label,value])=>`<article><span>${esc(label)}</span><strong>${esc(value)}</strong></article>`).join('')}</div>`;
  const table = (heads, rows) => rows.length ? `<div class="portal-table-wrap"><table class="portal-table"><thead><tr>${heads.map(h=>`<th>${esc(h)}</th>`).join('')}</tr></thead><tbody>${rows.map(row=>`<tr>${row.map(cell=>`<td>${cell}</td>`).join('')}</tr>`).join('')}</tbody></table></div>` : '<p class="portal-empty">아직 저장된 항목이 없습니다.</p>';
  const notice = text => `<div class="notice"><p>${esc(text)}</p></div>`;
  const option = (values, selected) => values.map(v=>`<option value="${esc(v)}" ${v===selected?'selected':''}>${esc(v)}</option>`).join('');
  const key = () => window.crypto.randomUUID();
  const identity = () => JSON.stringify(window.EclipseAuth.user());
  async function post(path, body, idempotencyKey) {
    return window.EclipseAPI.request(path, {method:'POST', headers:{'Content-Type':'application/json', ...(idempotencyKey?{'Idempotency-Key':idempotencyKey}:{})}, body:JSON.stringify(body)});
  }
  function controller(load, draw, bindExtra) {
    const state = {identity:null, data:null, error:'', loading:false, loaded:false, epoch:0};
    function reset() {
      const id = identity();
      if (state.identity !== id) { state.identity=id;state.data=null;state.error='';state.loading=false;state.loaded=false;state.epoch++; }
    }
    async function reload() {
      reset(); if(state.loading)return;
      const epoch=state.epoch;state.loading=true;state.loaded=true;
      try { const data=await load();if(epoch===state.epoch){state.data=data;state.error='';} }
      catch(error){if(epoch===state.epoch){state.error=error.message;state.data=null;}}
      finally {if(epoch===state.epoch){state.loading=false;window.EclipseApp.refresh();}}
    }
    return {state,reload,resetCache(){state.identity=null;state.data=null;state.error="";state.loaded=false;state.loading=false;state.epoch++;},
      render(path){reset();return `${state.error?notice(state.error):''}${state.loading?notice('API 상태를 불러오는 중입니다.'):''}${state.data?draw(path,state.data):card('Backend connection',state.error?'데이터를 불러오지 못했습니다. 상단 Refresh로 다시 시도하세요.':'저장된 상태를 불러오는 중입니다.')}`;},
      bind(root,path){reset();if(!state.loaded)reload();if(state.data&&bindExtra)bindExtra(root,path,state.data);}
    };
  }
  function domain(domain) {
    let draft = null, selected = null, selectedRequest = null, actionPending = false;
    function newDraft(product) {return {step:1,project:`${domain}-lab`,blueprint_id:product.blueprint_id,environment:product.allowed_environments[0],size:product.allowed_sizes[0],duration_hours:product.allowed_duration_hours[0],purpose:'Synthetic non-production application lab',idempotency:key()};}
    const requestTable = rows => table(['Project / Request','Template','Status / Delivery','Lifecycle'], rows.map(r=>[
      `${esc(r.project)}<small>${esc(r.id)}</small>`,`${esc(r.blueprint_id)}<small>${esc(r.environment)} · ${r.duration_hours}h</small>`,`${badge(r.status)}<small>${esc(r.resource_status||r.delivery_status)}</small>`,
      `<button class="button" data-request="${esc(r.id)}">Details</button>${r.rejection_reason?`<small role="alert">${esc(r.rejection_reason)}</small>`:""}${r.status==='PENDING'&&r.requested_by===window.EclipseAuth.user()?.userId?`<button class="button" data-action="cancel" data-id="${esc(r.id)}">Cancel</button>`:''}${r.delivery_status==='FAILED'?`<button class="button" data-action="redeliver" data-id="${esc(r.id)}">Retry delivery</button>`:''}${r.resource_status==='RUNNING'?`<button class="button" data-action="destroy" data-id="${esc(r.id)}">Request recovery</button>`:''}`
    ]));
    function configurator(data) {
      if(!draft)draft=newDraft(data.catalog.find(p=>p.requestable)||data.catalog[0]);
      const product=data.catalog.find(p=>p.blueprint_id===draft.blueprint_id);
      const labels=['Project','Template','Size','Lifecycle','Cost','Review'];
      const field=(label,control)=>`<label class="config-field"><span>${esc(label)}</span>${control}</label>`;
      const payload={project:draft.project,blueprint_id:draft.blueprint_id,environment:draft.environment,size:draft.size,duration_hours:Number(draft.duration_hours),purpose:draft.purpose};
      let body='';
      if(draft.step===1)body=field('Project',`<input name="project" pattern="[a-z][a-z0-9-]{2,39}" value="${esc(draft.project)}" required>`)+field('Environment',`<select name="environment">${option(product.allowed_environments,draft.environment)}</select>`);
      if(draft.step===2)body=field('Approved template',`<select name="blueprint_id">${data.catalog.map(p=>`<option value="${esc(p.blueprint_id)}" ${p.blueprint_id===draft.blueprint_id?'selected':''}>${esc(p.display_name)} · ${p.requestable?'LOCAL PATH':'BLOCKED'}</option>`).join('')}</select>`)+notice(product.summary)+notice(`Readiness: ${product.resolution_status}. Live runtime: NOT_VALIDATED.`);
      if(draft.step===3)body=field('Approved size',`<select name="size">${option(product.allowed_sizes,draft.size)}</select>`)+notice('네트워크·보안·구성요소는 승인된 템플릿으로 고정됩니다.');
      if(draft.step===4)body=field('Duration (hours)',`<select name="duration_hours">${option(product.allowed_duration_hours.map(String),String(draft.duration_hours))}</select>`)+notice('회수는 접근 권한 폐기와 작업 큐를 거칩니다. 자원 제거 결과가 확인될 때 완료됩니다.');
      if(draft.step===5)body=metrics([['Monthly estimate',money(data.finops.rates_krw[draft.size])],['Billing source','LOCAL_ESTIMATE']])+notice('로컬 단가 모델의 월 추정치입니다. 실제 청구·사용량·절감액은 수집되지 않았습니다.');
      if(draft.step===6)body=table(['Field','Value'],Object.entries(payload).filter(([k])=>k!=='purpose').map(([k,v])=>[esc(k),esc(v)]))+field('Purpose',`<textarea name="purpose" minlength="5" maxlength="200" required>${esc(draft.purpose)}</textarea>`)+notice(product.requestable?'신청 후 운영자 승인이 필요합니다.':'이 템플릿은 미구현 의존성이 있어 신청할 수 없습니다.');
      return `<form id="portal-request" class="wizard-card"><ol class="wizard-progress">${labels.map((label,i)=>`<li class="${draft.step===i+1?'active':''}"><span>${i+1}</span><b>${label}</b></li>`).join('')}</ol><div class="wizard-step"><h3>${labels[draft.step-1]}</h3><div class="config-grid">${body}</div></div><p id="portal-form-error" role="alert"></p><div class="wizard-actions">${draft.step>1?'<button type="button" class="button" data-back>← Back</button>':'<span></span>'}<button class="button primary" type="submit" ${draft.step===6&&!product.requestable?'disabled':''}>${draft.step===6?'Submit request':'Continue →'}</button></div></form>`;
    }
    const ui=controller(()=>window.EclipseAPI.get(`/${domain}/workspace`),(path,data)=>{
      const page=path.split('/').pop();
      if(page==='configurator')return configurator(data);
      if(page==='catalog')return `<div class="product-grid">${data.catalog.map(p=>`<article class="product"><div><h3>${esc(p.display_name)}</h3><p>${esc(p.summary)}</p>${badge(p.resolution_status)}<p>Live runtime: NOT_VALIDATED</p><button class="button" data-template="${esc(p.blueprint_id)}">Review template</button></div></article>`).join('')}</div>`;
      if(page==='requests')return card('Requests',requestTable(data.requests),'Persisted request and callback state')+(selectedRequest?requestDetail(data):'');
      if(page==='infrastructure'||page==='services')return `${card('Resources',table(['Project','Resource','Status','Details'],data.resources.map(r=>[esc(r.project),esc(r.name),badge(r.status),`<button class="button" data-resource="${esc(r.id)}">Details</button>`])),'Synthetic/local callbacks · NOT_VALIDATED')}${selected?resourceDetail(data):''}${page==='services'?notice(domain==='manufacturing'?'Manufacturing SaaS: adapter not implemented.':'금융 업무는 합성 데이터 전용입니다. 외부 주문·거래소·브로커 어댑터는 연결되지 않았습니다.'):''}`;
      if(page==='monitoring')return card('Monitoring',notice('수집 파이프라인이 연결되지 않았습니다. CPU·메모리·알림 상태는 확인되지 않았습니다.'),'NOT_CONNECTED / NOT_VALIDATED');
      if(page==='finops')return card('FinOps',metrics([['Estimated monthly',money(data.finops.estimated_monthly_krw)],['Actual charges',money(data.finops.actual_krw)]]),'LOCAL_ESTIMATE · billing not connected');
      return metrics([['Resources',data.resources.length],['Pending requests',data.requests.filter(r=>r.status==='PENDING').length],['Monthly estimate',money(data.finops.estimated_monthly_krw)],['Monitoring','NOT_CONNECTED']])+card('Recent requests',requestTable(data.requests.slice(0,5)),data.tenant_id)+notice('Hybrid-Ready · bounded non-production lab · runtime NOT_VALIDATED');
    },(root,path,data)=>{
      root.querySelectorAll('[data-request]').forEach(button=>button.onclick=()=>{selectedRequest=button.dataset.request;if(window.EclipseRouter.path()!==`/${domain}/requests`)window.EclipseRouter.navigate(`/${domain}/requests`);else window.EclipseApp.refresh();});
      root.querySelectorAll('[data-template]').forEach(button=>button.onclick=()=>{draft=newDraft(data.catalog.find(p=>p.blueprint_id===button.dataset.template));window.EclipseRouter.navigate(`/${domain}/configurator`);});
      root.querySelectorAll('[data-resource]').forEach(button=>button.onclick=()=>{selected={id:button.dataset.resource,tab:'Overview'};window.EclipseApp.refresh();});
      root.querySelectorAll('[data-resource-tab]').forEach(button=>button.onclick=()=>{selected.tab=button.dataset.resourceTab;window.EclipseApp.refresh();});
      root.querySelectorAll('[data-action]').forEach(button=>button.onclick=async()=>{
        if(actionPending)return;let body={};
        if(button.dataset.action==='destroy'){const reason=window.prompt('회수 사유를 입력하세요. 접근 권한을 폐기하고 회수 작업을 요청합니다.');if(!reason)return;if(reason.trim().length<5){ui.state.error='회수 사유는 5자 이상이어야 합니다.';window.EclipseApp.refresh();return;}body={reason:reason.trim()};}
        actionPending=true;button.disabled=true;
        try{await post(`/${domain}/requests/${encodeURIComponent(button.dataset.id)}/${button.dataset.action}`,body);await ui.reload();}
        catch(error){ui.state.error=error.message;window.EclipseApp.refresh();}finally{actionPending=false;}
      });
      const form=root.querySelector('#portal-request');if(!form)return;
      function capture(){for(const [name,value] of new FormData(form)){if(name in draft)draft[name]=value;}draft.duration_hours=Number(draft.duration_hours);}
      const back=form.querySelector('[data-back]');if(back)back.onclick=()=>{capture();draft.step--;window.EclipseApp.refresh();};
      const template=form.querySelector('[name="blueprint_id"]');if(template)template.onchange=()=>{capture();const product=data.catalog.find(p=>p.blueprint_id===draft.blueprint_id);draft.environment=product.allowed_environments[0];draft.size=product.allowed_sizes[0];draft.duration_hours=product.allowed_duration_hours[0];draft.idempotency=key();window.EclipseApp.refresh();};
      form.onsubmit=async event=>{event.preventDefault();if(!form.reportValidity())return;capture();if(draft.step<6){draft.step++;window.EclipseApp.refresh();return;}const button=form.querySelector('[type="submit"]');button.disabled=true;
        try{await post(`/${domain}/requests`,{project:draft.project,blueprint_id:draft.blueprint_id,environment:draft.environment,size:draft.size,duration_hours:draft.duration_hours,purpose:draft.purpose.trim()},draft.idempotency);draft=null;await ui.reload();window.EclipseRouter.navigate(`/${domain}/requests`);}
        catch(error){form.querySelector('#portal-form-error').textContent=error.message;button.disabled=false;}
      };
    });
    function requestDetail(data){const r=data.requests.find(item=>item.id===selectedRequest);if(!r)return '';return card('Request detail',table(['Field','Value'],Object.entries(r).map(([k,v])=>[esc(k),esc(v)])),'Persisted authority · rejection and grant state');}
    function resourceDetail(data){const r=data.resources.find(r=>r.id===selected.id);if(!r)return '';const req=data.requests.find(q=>q.id===r.request_id);const tabs=['Overview','Resources','Network','Access','Monitoring','Cost','Lifecycle'];let body='';
      if(['Overview','Resources'].includes(selected.tab))body=table(['Field','Value'],Object.entries(r).map(([k,v])=>[esc(k),esc(v)]));
      if(selected.tab==='Network')body=notice('Private application template. Actual network inventory has not been validated.');
      if(selected.tab==='Access')body=notice('GRANT_REQUIRED. 접근 토큰은 화면에 저장·표시하지 않습니다. 실제 접속 연동은 검증되지 않았습니다.');
      if(selected.tab==='Monitoring')body=notice('NOT_CONNECTED / NOT_VALIDATED');
      if(selected.tab==='Cost')body=notice(`LOCAL_ESTIMATE: ${money(req?.estimated_monthly_krw)} / month. 실제 청구 미수집.`);
      if(selected.tab==='Lifecycle')body=notice(`Request ${req?.status}; resource ${r.status}. 회수 완료는 결과 콜백으로 확인합니다.`);
      return card(r.project,`<div class="wizard-actions">${tabs.map(t=>`<button class="button" data-resource-tab="${t}" aria-pressed="${selected.tab===t}">${t}</button>`).join('')}</div>${body}`);
    }
    const originalRender=ui.render;ui.render=path=>{if(ui.state.identity!==identity()){draft=null;selected=null;selectedRequest=null;}return originalRender(path);};
    return ui;
  }
  window.EclipsePortalUI={esc,money,badge,card,metrics,table,notice,post,key,controller,domain};
}());
