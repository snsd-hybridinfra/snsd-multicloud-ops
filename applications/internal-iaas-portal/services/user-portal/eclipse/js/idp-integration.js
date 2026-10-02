(function(){
  'use strict';
  const U=window.EclipsePortalUI;
  for(const [domain,name] of [['developer','Developer'],['manufacturing','Manufacturing'],['finance','Finance'],['public','Public']]){
    if(window.EclipseDomainAPI.isMock(domain))continue;
    const upstream=window[`Eclipse${name}`];
    const ui=U.domain(domain);
    window[`Eclipse${name}`]={
      render(path){
        const live=ui.render(path);
        if(path===`/${domain}/services`&&upstream)return U.notice('서비스 설계 미리보기입니다. 업무 어댑터와 실제 런타임은 연결되지 않았습니다.')+upstream.render(path);
        return live;
      },
      bind(root,path){if(path.startsWith(`/${domain}/`))ui.bind(root,path);},
      reload:()=>ui.reload(),reset:()=>ui.resetCache()
    };
  }
  const logout=window.EclipseAuth.logout;
  window.EclipseAuth.logout=()=>{logout();for(const name of ['Developer','Manufacturing','Finance','Public','Admin','LLM'])window[`Eclipse${name}`]?.reset?.();};
  if(!window.EclipseDomainAPI.isMock('admin')){
    const team=U.controller(()=>window.EclipseAPI.get('/portal/team'),(_,data)=>U.card('Team directory',U.notice(data.message),data.source));
    const original=window.EclipseIdentity;
    window.EclipseIdentity={...original,renderTeam:()=>{const html=team.render('/customer/team');if(!team.state.loaded)team.reload();return html;}};
  }
}());
