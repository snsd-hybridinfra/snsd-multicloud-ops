(function(){
  'use strict';
  if(window.EclipseDomainAPI.isMock('admin'))return;
  const U=window.EclipsePortalUI;
  let pending=null;
  const ui=U.controller(async()=>{
    const data=await window.EclipseAPI.get('/admin/workspace');
    const path=window.EclipseRouter.path();
    if(path==='/admin/audit')data.audit=await window.EclipseAPI.get('/admin/audit');
    if(path==='/admin/grants')data.grants=await window.EclipseAPI.get('/admin/grants');
    if(path==='/admin/users')data.users=await window.EclipseAPI.get('/admin/users');
    return data;
  },(path,data)=>{
    const requestRows=data.requests.map(r=>[`${U.esc(r.project)}<small>${U.esc(r.id)}</small>`,`${U.esc(r.tenant_id)}<small>${U.esc(r.requested_by)}</small>`,U.esc(r.blueprint_id),U.badge(r.approval_status||r.status),
      (r.approval_status||r.status)==='PENDING'&&data.approval_connection==='CONNECTED'?`<button class="button" data-decision="approve" data-id="${U.esc(r.id)}">Approve</button> <button class="button" data-decision="reject" data-id="${U.esc(r.id)}">Reject</button>`:'-']);
    const queue=()=>U.card('Approval queue',U.table(['Project / Request','Tenant / Requester','Template','Approval','Action'],requestRows),data.approval_connection);
    if(path.endsWith('/approvals'))return `${pending?U.card('Decision',`<form id="admin-decision-form"><p>${U.esc(pending.action)} · ${U.esc(pending.id)}</p><label class="config-field"><span>Reason</span><textarea name="reason" minlength="5" maxlength="500" required></textarea></label><button type="submit" class="button primary">Confirm decision</button><button type="button" class="button" data-cancel>Cancel</button><p id="decision-error" role="alert"></p></form>`):''}${queue()}`;
    if(path.endsWith('/terraform'))return U.card('Provisioning jobs',U.table(['Job / Request','Operation','Status','Attempts','Action'],data.jobs.map(j=>[`${U.esc(j.job_id)}<small>${U.esc(j.request_id)}</small>`,U.esc(j.operation),U.badge(j.status),U.esc(j.attempts),String(j.status).includes('FAILED')?`<button class="button" data-retry="${U.esc(j.job_id)}">Retry approved job</button>`:'-'])),'Existing runner queue · runtime NOT_VALIDATED');
    if(path.endsWith('/grants'))return U.card('Grants',U.table(['Grant','Request','Subject','Status','Expiry'],(data.grants?.items||[]).map(g=>[U.esc(g.grant_id),U.esc(g.request_id),U.esc(g.subject_id),U.badge(g.status),U.esc(g.expires_at)])),'GRANT_DATABASE · read-only · recovery uses the resource lifecycle');
    if(path.endsWith('/users'))return U.card('Users',U.table(['Observed requester','Tenant','Source'],(data.users?.items||[]).map(u=>[U.esc(u.user_id),U.esc(u.tenant_id),U.esc(u.source)])),'Identity directory / role management NOT_CONNECTED');
    if(path.endsWith('/infrastructure'))return U.card('Resource callbacks',U.table(['Project','Tenant','Resource','Status'],data.requests.filter(r=>r.resource_id).map(r=>[U.esc(r.project),U.esc(r.tenant_id),U.esc(r.resource_id),U.badge(r.resource_status)])),'No live infrastructure discovery · runtime NOT_VALIDATED');
    if(path.endsWith('/tenants'))return U.card('Tenant inventory',U.table(['Tenant','Requests','Running callback resources','Local estimate'],data.tenants.map(t=>[U.esc(t.id),U.esc(t.requests),U.esc(t.environments),U.esc(U.money(t.estimated_monthly_krw))])),'Persisted portal metadata · private OpenStack target');
    if(path.endsWith('/monitoring'))return U.card('Monitoring',U.notice('NOT_CONNECTED. CPU, memory, VPN and Grafana runtime evidence have not been collected.'));
    if(path.endsWith('/finops'))return U.card('FinOps',U.table(['Tenant','Estimated monthly'],data.tenants.map(t=>[U.esc(t.id),U.esc(U.money(t.estimated_monthly_krw))])),'LOCAL_ESTIMATE · billing not connected');
    if(path.endsWith('/audit'))return U.card('Audit events',U.table(['Time','Actor','Action','Target'],(data.audit?.items||[]).map(e=>[U.esc(e.created_at),U.esc(e.actor_id),U.esc(e.event_type),U.esc(e.aggregate_id)])),'APPROVAL_DATABASE · no raw event payload');
    return U.metrics([['Requests',data.requests.length],['Pending',data.requests.filter(r=>(r.approval_status||r.status)==='PENDING').length],['Jobs',data.jobs.length],['Approval API',data.approval_connection]])+queue()+U.notice('Hybrid-Ready. Public cloud, production and live runtime remain unconnected.');
  },(root)=>{
    root.querySelectorAll('[data-decision]').forEach(b=>b.onclick=()=>{pending={id:b.dataset.id,action:b.dataset.decision};if(window.EclipseRouter.path()!=='/admin/approvals')window.EclipseRouter.navigate('/admin/approvals');else window.EclipseApp.refresh();});
    const cancel=root.querySelector('[data-cancel]');if(cancel)cancel.onclick=()=>{pending=null;window.EclipseApp.refresh();};
    const form=root.querySelector('#admin-decision-form');if(form)form.onsubmit=async e=>{e.preventDefault();if(!form.reportValidity())return;const button=form.querySelector('[type="submit"]');button.disabled=true;try{const result=await U.post(`/admin/requests/${encodeURIComponent(pending.id)}/${pending.action}`,{reason:form.reason.value.trim()});pending=null;await ui.reload();if(result.callback_status==='FAILED'){ui.state.error='Decision saved; callback delivery failed. Existing retry-sync operation is required.';window.EclipseApp.refresh();}}catch(error){form.querySelector('#decision-error').textContent=error.message;button.disabled=false;}};
    root.querySelectorAll('[data-retry]').forEach(b=>b.onclick=async()=>{b.disabled=true;try{await U.post(`/admin/jobs/${encodeURIComponent(b.dataset.retry)}/retry`,{});await ui.reload();}catch(error){ui.state.error=error.message;window.EclipseApp.refresh();}});
  });
  window.EclipseAdmin={render:path=>{if(ui.state.identity!==JSON.stringify(window.EclipseAuth.user()))pending=null;return ui.render(path);},bind:(root,path)=>{if(path.startsWith('/admin/')){const needed={'/admin/audit':'audit','/admin/grants':'grants','/admin/users':'users'}[path];if(ui.state.data&&needed&&!ui.state.data[needed]&&!ui.state.loading)ui.reload();ui.bind(root,path);}},reset:()=>{pending=null;ui.resetCache();},reload:()=>{pending=null;return ui.reload();}};
}());
