(function () {
  'use strict';
  const store={models:[{id:'eclipse-fast',name:'Eclipse Fast',context:'64K',status:'AVAILABLE'},{id:'eclipse-large',name:'Eclipse Large',context:'128K',status:'AVAILABLE'},{id:'embedding-v3',name:'Embedding v3',context:'8K',status:'AVAILABLE'}]};
  const smallProfile={size:'small'};
  let activeSession=null;
  function sessionFor(account=window.EclipseAuth.user()){
    if(!account||!account.scopes.includes('llm:invoke'))return null;
    const key=JSON.stringify([account.tenantId,account.userId]);
    if(!activeSession||activeSession.key!==key)activeSession={key,model:'eclipse-fast',messages:[],usage:[],workspaceRequest:null,requestError:''};
    return activeSession;
  }
  function reset(){activeSession=null;}
  function requestCard(session){
    const account=window.EclipseAuth.user();
    if(account.role!=='LLM_USER')return `<section class="llm-workspace-card"><div><small>DEFAULT LLM ACCESS</small><h3>Developer부터 바로 사용</h3><p>기본 LLM 서비스가 제공됩니다. 개인용 Small 인스턴스 요청은 LLM_USER 전용입니다.</p></div><strong>SHARED SERVICE</strong></section>`;
    const request=session.workspaceRequest;
    return `<section class="llm-workspace-card"><div><small>PERSONAL WORKSPACE REQUEST · DEMO</small><h3>Small LLM workspace</h3><p>사용자별 전용 워크스페이스를 요청합니다. 승인·실제 컨테이너 생성은 백엔드 프로비저너 연동이 필요합니다.</p>${request?`<span class="llm-request-status">요청 ${esc(request.id)} · ${esc(request.status)}</span>`:''}${session.requestError?`<span class="llm-request-error" role="alert">${esc(session.requestError)}</span>`:''}</div>${request?`<strong>${esc(request.status)}</strong>`:'<button class="button primary" type="button" data-request-workspace>Request Small workspace →</button>'}</section>`;
  }
  const esc=value=>String(value==null?'':value).replace(/[&<>\"']/g,ch=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[ch]));
  function dashboard(){const session=sessionFor();return `${requestCard(session)}<div class="metric-grid"><article><span>Models available</span><strong>${store.models.length}</strong><small>scope: llm:invoke</small></article><article><span>Session requests</span><strong>${session.usage.length}</strong><small>Current user only</small></article><article><span>Estimated tokens</span><strong>${session.usage.reduce((sum,item)=>sum+item.tokens,0).toLocaleString()}</strong><small class="demo-tag">DEMO ESTIMATE</small></article><article><span>Workspace request</span><strong>${session.workspaceRequest?'1':'0'}</strong><small>Small · per-user request</small></article></div>`;}
  function service(){
    const session=sessionFor();
    return `<div class="llm-scope-bar"><span>✓ llm:invoke</span><span>User session isolated</span><span class="demo-tag">MOCK · No external transmission</span></div>${requestCard(session)}<div class="llm-layout"><form id="llm-chat" class="wizard-card llm-chat"><div class="card-head"><div><h3>LLM Service</h3><p>기본 Developer 계정부터 사용할 수 있습니다.</p></div><div class="llm-toolbar"><select name="model" aria-label="LLM model">${store.models.map(model=>`<option value="${esc(model.id)}" ${model.id===session.model?'selected':''}>${esc(model.name)}</option>`).join('')}</select>${session.messages.length?'<button class="button" type="button" data-clear-chat>Clear</button>':''}</div></div><div class="chat-stream" role="log" aria-live="polite">${session.messages.length?session.messages.map(message=>`<div class="${message.role}"><strong>${message.role==='user'?'You':`Eclipse AI · ${esc(message.model||session.model)}`}</strong><p>${esc(message.text)}</p></div>`).join(''):'<div class="empty-chat"><span>✦</span><h3>Ask Eclipse AI</h3><p>이 데모는 외부 모델로 데이터를 전송하지 않습니다.</p></div>'}</div><div class="chat-input"><label><textarea name="prompt" maxlength="2000" placeholder="Ask about your cloud operations…" aria-describedby="prompt-policy" required></textarea><span id="prompt-policy"><b id="prompt-count">0</b>/2000 · Do not enter secrets or personal data.</span></label><button class="button primary" type="submit">Send</button></div></form><aside class="data-card model-list"><div class="card-head"><div><h3>Models</h3><p>Available to this user</p></div></div>${store.models.map(model=>`<div class="${model.id===session.model?'selected':''}"><span>✦</span><p><strong>${esc(model.name)}</strong><small>${esc(model.context)} context</small></p><b>${esc(model.status)}</b></div>`).join('')}</aside></div>`;
  }
  function usage(){const session=sessionFor();const tokens=session.usage.reduce((sum,item)=>sum+item.tokens,0);return `${requestCard(session)}<div class="llm-scope-bar"><span>✓ llm:usage:read</span><span>Current user session only</span></div><div class="request-stats"><article><span>Estimated tokens</span><strong>${tokens.toLocaleString()}</strong></article><article><span>Requests</span><strong>${session.usage.length}</strong></article><article><span>Billing</span><strong>Not connected</strong></article></div><article class="data-card"><div class="card-head"><div><h3>Session usage</h3><p>Per-user memory only · DEMO DATA</p></div></div>${session.usage.length?`<div class="usage-bars">${session.usage.map(item=>`<div><span>${esc(item.time)}</span><i><b style="width:${Math.min(100,Math.max(5,item.tokens/10))}%"></b></i><strong>${item.tokens} estimated tokens</strong><em>${esc(item.model)}</em></div>`).join('')}</div>`:'<p class="llm-usage-empty">아직 이 사용자 세션의 LLM 요청이 없습니다.</p>'}</article>`;}
  function cost(){const session=sessionFor();return `${requestCard(session)}<div class="metric-grid"><article><span>Current billed cost</span><strong>—</strong><small>Billing adapter not connected</small></article><article><span>Session requests</span><strong>${session.usage.length}</strong><small>User session only</small></article><article><span>Estimated tokens</span><strong>${session.usage.reduce((sum,item)=>sum+item.tokens,0).toLocaleString()}</strong><small class="demo-tag">DEMO ESTIMATE</small></article><article><span>Price policy</span><strong>Pending</strong><small>No charge calculated in demo</small></article></div>`;}
  function render(path){if(path==='/llm/dashboard')return dashboard();if(path==='/llm/service')return service();if(path==='/llm/usage')return usage();if(path==='/llm/cost')return cost();return '';}
  async function requestWorkspace(button){
    const account=window.EclipseAuth.user();
    const session=sessionFor(account);
    if(!session||account.role!=='LLM_USER'||session.workspaceRequest)return;
    button.disabled=true;
    button.textContent='Requesting…';
    try{
      const request=await window.EclipseDomainAPI.post('llm','/llm/workspace-requests',{size:smallProfile.size},()=>({id:`LLM-REQ-${Date.now()}`,status:'REQUESTED',size:smallProfile.size}));
      if(!request||!request.id||!request.status)throw new Error('Invalid workspace request response.');
      session.workspaceRequest=request;
      session.requestError='';
    }catch(error){
      session.requestError=error.message;
    }
    if(activeSession===session&&window.EclipseAuth.user()===account)window.EclipseApp.refresh();
  }
  async function send(form){
    const session=sessionFor();
    const prompt=form.prompt.value.trim();
    if(!session||!prompt)return;
    const button=form.querySelector('[type="submit"]');
    button.disabled=true;
    button.textContent='Sending…';
    session.model=form.model.value;
    session.messages.push({role:'user',text:prompt,model:session.model});
    try{
      const response=await window.EclipseDomainAPI.post('llm','/llm/chat',{model:session.model,prompt},()=>({message:'Demo response: your request stayed inside this user-scoped LLM mock adapter.'}));
      session.messages.push({role:'assistant',text:response.message,model:session.model});
      session.usage.push({time:new Date().toLocaleTimeString('ko-KR',{hour:'2-digit',minute:'2-digit'}),model:session.model,tokens:Math.ceil((prompt.length+response.message.length)/4)});
    }catch(error){
      session.messages.push({role:'assistant',text:`Request failed: ${error.message}`,model:session.model});
    }
    if(activeSession===session&&window.EclipseAuth.user())window.EclipseApp.refresh();
  }
  function bind(root,path){
    if(!path.startsWith('/llm/'))return;
    const requestButton=root.querySelector('[data-request-workspace]');
    if(requestButton)requestButton.addEventListener('click',()=>requestWorkspace(requestButton));
    if(path!=='/llm/service')return;
    const form=root.querySelector('#llm-chat');
    const session=sessionFor();
    const stream=root.querySelector('.chat-stream');
    if(stream)stream.scrollTop=stream.scrollHeight;
    form.model.addEventListener('change',()=>{session.model=form.model.value;window.EclipseApp.refresh();});
    const prompt=form.prompt;
    const count=root.querySelector('#prompt-count');
    prompt.addEventListener('input',()=>{count.textContent=prompt.value.length;});
    const clear=root.querySelector('[data-clear-chat]');
    if(clear)clear.addEventListener('click',()=>{session.messages.length=0;window.EclipseApp.refresh();});
    form.addEventListener('submit',event=>{event.preventDefault();send(form);});
  }
  window.EclipseLLM={render,bind,reset,sessionFor,store};
}());
