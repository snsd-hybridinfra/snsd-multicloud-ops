(function () {
  'use strict';
  const app = document.getElementById('app');
  const Auth = window.EclipseAuth;
  const Router = window.EclipseRouter;
  const RBAC = window.EclipseRBAC;
  const Runtime = window.ECLIPSE_RUNTIME_CONFIG || {};
  let authReady = Auth.isDemoEnabled();
  let authError = '';

  const escapeHtml = value => String(value == null ? '' : value).replace(/[&<>\"']/g, char => ({'&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'}[char]));
  const roleLabel = role => ({CUSTOMER_USER: 'Customer User', CUSTOMER_MANAGER: 'Customer Manager', MSP_OPERATOR: 'MSP Operator', MSP_ADMIN: 'MSP Admin', LLM_USER: 'LLM User'}[role] || role);
  const quickDemoKeys = ['customer', 'manager'];
  const icon = name => ({dashboard: '▦', catalog: '◇', request: '+', requests: '▤', infra: '⬡', monitor: '⌁', finops: '₩', users: '♙', approval: '✓', grants: '◈', jobs: '⚙', audit: '◫', llm: '✦', usage: '◒'}[name] || '•');

  const customerNav = [
    ['Overview', [['/manufacturing/dashboard', 'Dashboard', 'dashboard']]],
    ['Manufacturing', [['/manufacturing/catalog', 'Service Catalog', 'catalog'], ['/manufacturing/configurator', 'New Request', 'request'], ['/manufacturing/requests', 'Requests', 'requests'], ['/manufacturing/infrastructure', 'Infrastructure', 'infra'], ['/manufacturing/services', 'Manufacturing SaaS', 'catalog']]],
    ['Operations', [['/manufacturing/monitoring', 'Monitoring', 'monitor'], ['/manufacturing/finops', 'FinOps', 'finops']]],
  ];
  const managerNav = [['Management', [['/customer/team', 'Company Users', 'users']]]];
  const financeNav = [['Finance', [['/finance/dashboard', 'Finance Dashboard', 'dashboard'], ['/finance/catalog', 'Finance Catalog', 'catalog'], ['/finance/configurator', 'Finance Request', 'request'], ['/finance/requests', 'Finance Requests', 'requests'], ['/finance/services', 'Finance Services', 'infra']]]];
  const publicNav = [['Public', [['/public/dashboard', 'Public Dashboard', 'dashboard'], ['/public/catalog', 'Public Catalog', 'catalog'], ['/public/configurator', 'Public Request', 'request'], ['/public/requests', 'Public Requests', 'requests'], ['/public/services', 'Public Services', 'infra']]]];
  const developerNav = [['Developer', [['/developer/dashboard', 'Developer Dashboard', 'dashboard'], ['/developer/catalog', 'Cloud Catalog', 'catalog'], ['/developer/configurator', 'New Environment', 'request'], ['/developer/requests', 'Requests', 'requests'], ['/developer/infrastructure', 'Infrastructure', 'infra'], ['/developer/monitoring', 'Monitoring', 'monitor'], ['/developer/finops', 'FinOps', 'finops']]]];
  const adminNav = [
    ['Overview', [['/admin/dashboard', 'Dashboard', 'dashboard']]],
    ['Operations', [['/admin/tenants', 'Tenants', 'users'], ['/admin/users', 'Users & Roles', 'users'], ['/admin/approvals', 'Approval Queue', 'approval'], ['/admin/grants', 'Access Grants', 'grants'], ['/admin/infrastructure', 'Infrastructure', 'infra'], ['/admin/terraform', 'Terraform Jobs', 'jobs'], ['/admin/monitoring', 'Monitoring', 'monitor'], ['/admin/finops', 'FinOps', 'finops'], ['/admin/audit', 'Audit', 'audit']]],
    ['Finance', [['/finance/dashboard', 'Finance Dashboard', 'dashboard'], ['/finance/requests', 'Finance Requests', 'requests']]],
    ['Public', [['/public/dashboard', 'Public Dashboard', 'dashboard'], ['/public/requests', 'Public Requests', 'requests']]],
  ];
  const operatorNav = [
    ['Overview', [['/admin/dashboard', 'Dashboard', 'dashboard']]],
    ['Operations', [['/admin/approvals', 'Approval Queue', 'approval'], ['/admin/infrastructure', 'Infrastructure', 'infra'], ['/admin/terraform', 'Terraform Jobs', 'jobs'], ['/admin/monitoring', 'Monitoring', 'monitor']]],
    ['Finance', [['/finance/dashboard', 'Finance Dashboard', 'dashboard'], ['/finance/requests', 'Finance Requests', 'requests']]],
  ];
  function llmNavigation(account) {
    const links = [['/llm/dashboard', 'LLM Dashboard', 'llm'], ['/llm/service', 'LLM Service', 'catalog']];
    if (account.scopes.includes('monitoring:assist')) links.push(['/llm/monitoring-assistant', 'Monitoring Assistant', 'monitor']);
    if (account.scopes.includes('llm:usage:read')) links.push(['/llm/usage', 'Usage', 'usage'], ['/llm/cost', 'Token Cost', 'finops']);
    return [['LLM Platform', links]];
  }
  const legacyCustomerRoutes = {'/customer/dashboard':'/manufacturing/dashboard','/customer/catalog':'/manufacturing/catalog','/customer/request':'/manufacturing/configurator','/customer/requests':'/manufacturing/requests','/customer/infrastructure':'/manufacturing/infrastructure','/customer/monitoring':'/manufacturing/monitoring','/customer/finops':'/manufacturing/finops'};

  function navFor(account) {
    if (account.role === 'LLM_USER') return llmNavigation(account);
    let base;
    if (account.role === 'MSP_ADMIN') base = adminNav;
    else if (account.role === 'MSP_OPERATOR') base = operatorNav;
    else {
      base = [];
      if (account.scopes.includes('manufacturing:read')) base = base.concat(customerNav);
      if (account.scopes.includes('finance:read')) base = base.concat(financeNav);
      if (account.scopes.includes('public:read')) base = base.concat(publicNav);
      if (account.scopes.includes('developer:read')) base = base.concat(developerNav);
      if (account.role === 'CUSTOMER_MANAGER' && account.scopes.includes('team:read')) base = base.concat(managerNav);
    }
    return account.scopes.includes('llm:invoke') ? base.concat(llmNavigation(account)) : base;
  }
  function sectionFor(path) { return path.startsWith('/admin') ? 'admin' : path.startsWith('/llm') ? 'llm' : path.startsWith('/finance') ? 'finance' : path.startsWith('/public') ? 'public' : path.startsWith('/developer') ? 'developer' : 'customer'; }
  function titleFor(path) { return path.split('/').filter(Boolean).pop()?.replace(/-/g, ' ').replace(/\b\w/g, char => char.toUpperCase()) || 'Login'; }
  function routeToDefault(account) { Router.navigate(account.landingPath || (account.role === 'LLM_USER' ? '/llm/dashboard' : ['MSP_OPERATOR', 'MSP_ADMIN'].includes(account.role) ? '/admin/dashboard' : '/manufacturing/dashboard')); }
  function signOut() {
    Auth.logout();
    if (Auth.isDemoEnabled()) Router.navigate('/login');
    else window.location.assign(Auth.logoutUrl());
  }
  function renderSessionLoading() {
    app.innerHTML = '<main class="login-shell"><section class="login-art"><img class="theme-emblem" src="assets/eclipse-theme.png" alt="Eclipse"><p>ONE PLATFORM<br>EVERY CLOUD</p></section><section class="login-card session-loading" aria-live="polite"><div class="brand"><span aria-hidden="true"></span><strong>ECLIPSE CLOUD</strong></div><div class="login-copy"><small>SECURE SESSION</small><h1>Checking your<br><em>organization access.</em></h1><p>보안 세션과 포털 권한을 확인하고 있습니다.</p></div><span class="session-spinner" aria-hidden="true"></span></section></main>';
  }

  function renderLogin(message) {
    if (!Auth.isDemoEnabled()) {
      app.innerHTML = `<main class="login-shell"><section class="login-art"><img class="theme-emblem" src="assets/eclipse-theme.png" alt="Eclipse"><p>ONE PLATFORM<br>EVERY CLOUD</p></section><section class="login-card"><div class="brand"><span aria-hidden="true"></span><strong>ECLIPSE CLOUD</strong></div><div class="login-copy"><small>SECURE ORGANIZATION ACCESS</small><h1>Cloud operations,<br><em>in one place.</em></h1><p>조직 계정과 MFA를 사용해 안전하게 로그인하세요.</p></div>${message ? `<p class="error-message" role="alert">${escapeHtml(message)}</p>` : ''}<a class="button primary production-login" href="${escapeHtml(Auth.loginUrl())}">Continue with organization account <span>→</span></a><small class="login-foot">OIDC · MFA · server-managed session</small></section></main>`;
      return;
    }
    app.innerHTML = `<main class="login-shell"><section class="login-art"><img class="theme-emblem" src="assets/eclipse-theme.png" alt="Eclipse"><p>ONE PLATFORM<br>EVERY CLOUD</p></section><section class="login-card"><div class="brand"><span aria-hidden="true"></span><strong>ECLIPSE CLOUD</strong></div><div class="login-copy"><small>CUSTOMER · MSP · LLM PORTAL</small><h1>Cloud operations,<br><em>in one place.</em></h1><p>멀티클라우드 셀프서비스 포털 데모 계정으로 접속하세요.</p></div><form id="login-form"><label>Demo account ID<input name="username" autocomplete="username" placeholder="demo-user 또는 demo-manager" required></label><p class="login-demo-note">아래 데모를 선택하거나 다른 테스트 계정 ID를 입력하세요. 실제 비밀번호 인증은 제공하지 않습니다.</p>${message ? `<p class="error-message" role="alert">${escapeHtml(message)}</p>` : ''}<button class="button primary" type="submit">Open demo <span>→</span></button></form><p class="auth-switch">처음 방문하셨나요? <a href="#/signup">일반 사용자 회원가입</a></p><details class="demo-accounts"><summary>Demo accounts <small>Developer · MSP Admin</small></summary><div>${quickDemoKeys.map(key => { const account = Auth.DEMO_ACCOUNTS[key]; return `<button type="button" data-demo="${escapeHtml(key)}"><strong>${escapeHtml(key === 'customer' ? 'Developer User' : 'MSP Manager')}</strong><small>${escapeHtml(account.userId)}</small><small>${escapeHtml(account.tenantName)}</small></button>`; }).join('')}</div></details><small class="login-foot">Demo session stays in memory · production sign-in requires OIDC</small></section></main>`;
    document.getElementById('login-form').addEventListener('submit', event => { event.preventDefault(); const value = event.currentTarget.elements.namedItem('username').value; const account = Auth.login(value); if (!account) { renderLogin('등록된 데모 계정 ID를 입력하거나 아래 데모 계정을 선택하세요.'); return; } routeToDefault(account); });
    document.querySelectorAll('[data-demo]').forEach(button => button.addEventListener('click', () => { Auth.login(button.dataset.demo); routeToDefault(Auth.user()); }));
  }

  function renderSignup() {
    if (!Auth.isDemoEnabled()) { Router.navigate('/login'); return; }
    app.innerHTML = `<main class="login-shell signup-shell"><section class="login-art"><img class="theme-emblem" src="assets/eclipse-theme.png" alt="Eclipse"><p>START SIMPLE<br>GROW SECURE</p></section><section class="login-card signup-card"><div class="brand"><span aria-hidden="true"></span><strong>ECLIPSE CLOUD</strong></div><div class="login-copy"><small>DEVELOPER SIGNUP</small><h1>Create your<br><em>cloud account.</em></h1><p>모든 신규 계정은 일반 개발자 권한으로 시작합니다.</p></div><form id="signup-form"><div class="signup-grid"><label>Company name<input name="company" autocomplete="organization" minlength="2" maxlength="80" placeholder="회사명을 입력하세요" required></label><label>Work email<input name="email" type="email" autocomplete="email" maxlength="120" placeholder="you@company.com" required></label></div><article class="signup-access-plan"><div><small>INITIAL ACCESS</small><strong>Developer</strong><code>developer:read</code></div><p>제조·금융·공공 권한은 상담 완료 후 <b>MSP 관리자</b>가 승인하고 변경합니다.</p></article><div class="signup-grid"><label>Password<input name="password" type="password" autocomplete="new-password" minlength="8" placeholder="8자 이상" required></label><label>Confirm password<input name="confirmPassword" type="password" autocomplete="new-password" minlength="8" placeholder="비밀번호 재입력" required></label></div><label class="terms-check"><input name="terms" type="checkbox" required><span>서비스 이용 및 데모 환경의 임시 세션 사용에 동의합니다.</span></label><p class="signup-note">DEMO · 입력 정보와 비밀번호는 서버 또는 브라우저 저장소에 저장되지 않습니다.</p><button class="button primary" type="submit">Create developer account <span>→</span></button></form><p class="auth-switch">이미 계정이 있나요? <a href="#/login">로그인</a></p></section></main>`;
    const form = document.getElementById('signup-form');
    const confirmPassword = form.elements.namedItem('confirmPassword');
    confirmPassword.addEventListener('input', () => confirmPassword.setCustomValidity(''));
    form.addEventListener('submit', event => {
      event.preventDefault();
      const password = form.elements.namedItem('password').value;
      if (password !== confirmPassword.value) {
        confirmPassword.setCustomValidity('비밀번호가 일치하지 않습니다.');
        confirmPassword.reportValidity();
        return;
      }
      confirmPassword.setCustomValidity('');
      Auth.register({
        company: form.elements.namedItem('company').value,
        email: form.elements.namedItem('email').value,
      });
      routeToDefault(Auth.user());
    });
  }

  function navMarkup(account, currentPath) {
    return navFor(account).map(([heading, links]) => `<div class="nav-group"><p>${heading}</p>${links.map(([path, label, glyph]) => `<a class="nav-link ${path === currentPath ? 'active' : ''}" href="#${path}"><span>${icon(glyph)}</span>${label}</a>`).join('')}</div>`).join('');
  }

  function pageCopy(path, account) {
    const route = path.replace(/^\//, '');
    const copy = {
      'customer/dashboard': ['Dashboard', 'Cloud environments and service usage', 'Your company cloud overview is ready.'],
      'customer/catalog': ['Service Catalog', 'Choose a managed cloud service', 'Standard packages for manufacturing workloads.'],
      'customer/request': ['New Request', 'Create a Cloud Platform', 'IaaS + PaaS, configured as one governed request.'],
      'customer/requests': ['Requests', 'Track your requests', 'Follow approval, provisioning and settlement in one timeline.'],
      'customer/infrastructure': ['Infrastructure', 'Your environments', 'Resources provisioned for your tenant.'],
      'customer/monitoring': ['Monitoring', 'Service health', 'Monitoring is included in every Cloud Platform package.'],
      'customer/finops': ['FinOps', 'Spend overview', 'See cost allocation and forecasts for your tenant.'],
      'manufacturing/dashboard': ['Dashboard', 'Manufacturing cloud overview', 'Environments, requests, cost and manufacturing service health.'],
      'manufacturing/catalog': ['Service Catalog', 'Manufacturing Cloud Platform', 'IaaS and PaaS delivered as one governed package.'],
      'manufacturing/configurator': ['New Request', 'Configure Cloud Platform', 'Build the complete manufacturing environment in six steps.'],
      'manufacturing/requests': ['Requests', 'Manufacturing requests', 'Track approval, provisioning and settlement in one lifecycle.'],
      'manufacturing/infrastructure': ['Infrastructure', 'Manufacturing environments', 'Tenant-isolated provisioned resources.'],
      'manufacturing/services': ['Manufacturing SaaS', 'PartnerHub Cloud', 'AI-powered SMT Lot quality management from risk detection to supplier history.'],
      'manufacturing/monitoring': ['Monitoring', 'Manufacturing service health', 'Metrics, logs and alerts included by default.'],
      'manufacturing/finops': ['FinOps', 'Manufacturing cloud spend', 'Current and projected tenant cost.'],
      'customer/team': ['Company Users', 'Tenant members and access', 'Customer Manager can review company members; MSP Admin manages role changes.'],
      'finance/dashboard': ['Finance Dashboard', 'Zero Trust finance overview', 'Private workloads, mandatory controls, protected cost and security reviews.'],
      'finance/catalog': ['Finance Catalog', 'Financial Zero Trust Platform', 'Choose a hardened profile; the mandatory security baseline cannot be disabled.'],
      'finance/configurator': ['Finance Request', 'Configure secure Finance Cloud', 'Build within a private-only network, HSM-backed policy and immutable audit context.'],
      'finance/requests': ['Finance Requests', 'Finance delivery lifecycle', 'Track only requests created in the finance context.'],
      'finance/services': ['Finance Services', '통합 금융 업무 서비스', '입출금·이체, 대출, 환전, 증권·주식투자를 하나의 금융 애플리케이션 패키지로 제공합니다.'],
      'public/dashboard': ['Public Dashboard', 'Public digital service overview', '기관별 공공서비스 환경과 상담·승인 현황을 확인합니다.'],
      'public/catalog': ['Public Catalog', 'Public Digital Service Platform', '공공서비스 정책이 적용된 IaaS와 PaaS 통합 상품입니다.'],
      'public/configurator': ['Public Request', 'Configure Public Digital Service Platform', '기관·데이터 등급·감사 정책을 선택해 공공 환경을 요청하세요.'],
      'public/requests': ['Public Requests', 'Public delivery lifecycle', '상담 검토부터 승인·프로비저닝까지 별도 수명주기로 추적합니다.'],
      'public/services': ['Public Services', '통합 디지털 공공서비스', '온라인 민원·업무 처리·대국민 알림을 하나의 패키지로 제공합니다.'],
      'developer/dashboard': ['Developer Dashboard', 'General developer workspace', '산업 특화 영역과 분리된 애플리케이션 개발 환경입니다.'],
      'developer/catalog': ['Cloud Catalog', 'Developer Cloud Platform', '일반 웹·API 개발용 IaaS와 PaaS를 하나의 패키지로 제공합니다.'],
      'developer/configurator': ['New Environment', 'Configure developer environment', '런타임과 데이터 계층을 선택해 개발 환경을 요청하세요.'],
      'developer/requests': ['Requests', 'Developer delivery lifecycle', '개발 환경 요청과 승인 상태를 확인합니다.'],
      'developer/infrastructure': ['Infrastructure', 'Developer environments', '일반 개발자 테넌트에 격리된 리소스입니다.'],
      'developer/monitoring': ['Monitoring', 'Developer service health', '애플리케이션 런타임과 배포 상태를 확인합니다.'],
      'developer/finops': ['FinOps', 'Developer cloud spend', '개발 환경 비용과 최적화 기회를 확인합니다.'],
      'admin/dashboard': ['Dashboard', 'MSP operations overview', 'A single view of tenant health and delivery.'],
      'admin/tenants': ['Tenants', 'Customer tenants', 'Manage tenant context and membership.'],
      'admin/users': ['Users & Roles', 'Identity and role assignments', 'Review portal access across customer and MSP tenants.'],
      'admin/approvals': ['Approval Queue', 'Requests awaiting review', 'Approve or reject within policy.'],
      'admin/grants': ['Access Grants', 'Time-bound access grants', 'Review active, expired and revoked resource access.'],
      'admin/infrastructure': ['Infrastructure', 'Tenant infrastructure', 'Cross-tenant resource placement and isolation status.'],
      'admin/terraform': ['Terraform Jobs', 'Provisioning activity', 'Runner state and delivery callbacks.'],
      'admin/monitoring': ['Monitoring', 'Platform health', 'Cross-tenant service health for operators.'],
      'admin/finops': ['FinOps', 'MSP cost controls', 'Allocation, margin and budget controls.'],
      'admin/audit': ['Audit', 'Audit events', 'Immutable operational history.'],
      'llm/dashboard': ['LLM Dashboard', 'Your LLM access', 'Developer accounts can use LLM; LLM_USER can request a personal Small workspace.'],
      'llm/service': ['LLM Service', 'Available models', 'User-scoped demo chat with a separate Small workspace request for LLM_USER.'],
      'llm/monitoring-assistant': ['Monitoring Assistant', 'Metric anomaly review', '정제된 수치 신호만 설명하며 판정과 복구 권한은 갖지 않습니다.'],
      'llm/usage': ['Usage', 'Token usage', 'Review your LLM consumption.'],
      'llm/cost': ['Token Cost', 'Token cost', 'Usage-based cost visibility.'],
    }[route] || ['Forbidden', '403 Forbidden', 'You do not have access to this route.'];
    return {title: copy[0], heading: copy[1], subtitle: copy[2], section: route.split('/')[0], account};
  }

  function dashboardCards(account) {
    if (account.role === 'LLM_USER') return `<div class="metric-grid"><article><span>Models available</span><strong>4</strong><small>scope: llm:invoke</small></article><article><span>Tokens this month</span><strong>248K</strong><small>within budget</small></article><article><span>Open alerts</span><strong>0</strong><small>All systems healthy</small></article></div>`;
    if (['MSP_OPERATOR', 'MSP_ADMIN'].includes(account.role)) return `<div class="metric-grid"><article><span>Active tenants</span><strong>12</strong><small>+2 this month</small></article><article><span>Approval queue</span><strong>5</strong><small>2 high priority</small></article><article><span>Terraform jobs</span><strong>8</strong><small>1 provisioning</small></article><article><span>Platform alerts</span><strong>0</strong><small>All systems healthy</small></article></div>`;
    return `<div class="metric-grid"><article><span>Active environments</span><strong>3</strong><small>2 production-ready</small></article><article><span>Pending requests</span><strong>1</strong><small>Awaiting approval</small></article><article><span>Monthly cost</span><strong>₩482,300</strong><small class="demo-tag">DEMO DATA</small></article><article><span>Open alerts</span><strong>0</strong><small>All systems healthy</small></article></div>`;
  }

  function renderShell(path, account) {
    const copy = pageCopy(path, account);
    const isDashboard = path.endsWith('/dashboard');
    const demoBanner = Runtime.showDemoBanner ? `<div class="demo-mode-ribbon" role="status"><strong>${Runtime.environment==='local-connected'?'LOCAL CONNECTED':'DEMO MODE'}</strong><span>${Runtime.environment==='local-connected'?'API + persisted data · synthetic runtime · NOT_VALIDATED':'Sample data · No real resources'}</span></div>` : '';
    app.innerHTML = `${demoBanner}<div class="portal"><aside class="sidebar"><div class="brand"><span aria-hidden="true"></span><strong>ECLIPSE CLOUD</strong></div><div class="tenant"><span>${escapeHtml(account.tenantName.slice(0, 2).toUpperCase())}</span><div><strong>${escapeHtml(account.tenantName)}</strong><small>${escapeHtml(roleLabel(account.role))}</small></div></div><nav>${navMarkup(account, path)}</nav><button id="logout" class="logout">↗ Sign out</button></aside><main class="main"><header><div><small>${escapeHtml(copy.section.toUpperCase())}</small><h1>${escapeHtml(copy.title)}</h1></div><div class="header-user"><span>${escapeHtml(account.userId)}</span><button id="refresh">↻ Refresh</button></div></header><div class="content"><div class="breadcrumb">Eclipse Cloud <span>/</span> ${escapeHtml(copy.title)}</div><section class="hero"><div><small>${escapeHtml(copy.section.toUpperCase())}</small><h2>${escapeHtml(copy.heading)}</h2><p>${escapeHtml(copy.subtitle)}</p></div>${path === '/manufacturing/catalog' ? '<a class="button primary" href="#/manufacturing/configurator">Configure Cloud Platform <span>→</span></a>' : path === '/developer/catalog' ? '<a class="button primary" href="#/developer/configurator">Configure Developer Platform <span>→</span></a>' : path === '/public/catalog' ? '<a class="button primary" href="#/public/configurator">Configure Public Platform <span>→</span></a>' : ''}</section>${pageBody(path, account)}</div></main></div>`;
    document.getElementById('logout').addEventListener('click', signOut);
    document.getElementById('refresh').addEventListener('click', async()=>{
      const module=path.startsWith('/admin/')?window.EclipseAdmin:path.startsWith('/finance/')?window.EclipseFinance:path.startsWith('/public/')?window.EclipsePublic:path.startsWith('/developer/')?window.EclipseDeveloper:path.startsWith('/llm/')?window.EclipseLLM:window.EclipseManufacturing;
      const button=document.getElementById('refresh');button.disabled=true;button.textContent='↻ Syncing';
      if(module?.reload)await module.reload(path);else window.EclipseApp.refresh();
    });
    if (window.EclipseManufacturing) window.EclipseManufacturing.bind(app, path);
    if (window.EclipseFinance) window.EclipseFinance.bind(app, path);
    if (window.EclipsePublic) window.EclipsePublic.bind(app, path);
    if (window.EclipseDeveloper) window.EclipseDeveloper.bind(app, path);
    if (window.EclipseLLM) window.EclipseLLM.bind(app, path);
    if (window.EclipseAdmin) window.EclipseAdmin.bind(app, path);
    const forbiddenLogout = document.querySelector('[data-forbidden-logout]');
    if (forbiddenLogout) forbiddenLogout.addEventListener('click', signOut);
  }

  function pageBody(path, account) {
    if (path === '/forbidden') {
      const home = account.landingPath || (account.role === 'LLM_USER' ? '/llm/dashboard' : ['MSP_OPERATOR', 'MSP_ADMIN'].includes(account.role) ? '/admin/dashboard' : '/manufacturing/dashboard');
      const guidance = Auth.isDemoEnabled() ? '현재 역할에 허용된 메뉴를 이용하거나 다른 데모 계정으로 다시 로그인하세요.' : '현재 역할에 허용된 메뉴를 이용하거나 조직 관리자에게 권한을 요청하세요.';
      return `<div class="placeholder-card forbidden-state"><small>ROLE · ${escapeHtml(account.role)}</small><h3>이 계정으로 접근할 수 없는 화면입니다.</h3><p>${guidance}</p><div><a class="button primary" href="#${home}">Go to my dashboard</a><button class="button" type="button" data-forbidden-logout>Sign out</button></div></div>`;
    }
    if (path === '/customer/team' && window.EclipseIdentity) return window.EclipseIdentity.renderTeam(account);
    if (path.startsWith('/manufacturing/') && window.EclipseManufacturing) return window.EclipseManufacturing.render(path, account);
    if (path.startsWith('/finance/') && window.EclipseFinance) return window.EclipseFinance.render(path);
    if (path.startsWith('/public/') && window.EclipsePublic) return window.EclipsePublic.render(path);
    if (path.startsWith('/developer/') && window.EclipseDeveloper) return window.EclipseDeveloper.render(path);
    if (path.startsWith('/llm/') && window.EclipseLLM) return window.EclipseLLM.render(path);
    if (path.startsWith('/admin/') && window.EclipseAdmin) return window.EclipseAdmin.render(path);
    if (path === '/customer/catalog') return `<div class="product-grid"><article class="product featured"><span class="product-art">☁</span><div><small>CORE PLATFORM · AVAILABLE</small><h3>Cloud Platform Package</h3><p>개발 및 서비스 운영에 필요한 IaaS와 PaaS 환경을 하나의 상품으로 제공합니다.</p><ul><li>Compute + Network</li><li>Kubernetes + Runtime</li><li>Database + Cache</li><li>Storage + Monitoring</li></ul><a class="button primary" href="#/customer/request">Configure <span>→</span></a></div></article><article class="product"><span class="product-art pale">▥</span><div><small>MANUFACTURING SERVICE · PLANNED</small><h3>Manufacturing SaaS</h3><p>생산·품질·설비 데이터를 위한 제조 특화 서비스를 준비하고 있습니다.</p><button class="button" disabled>Coming soon</button></div></article><article class="product"><span class="product-art lavender">✦</span><div><small>INTELLIGENCE · COMING SOON</small><h3>AI / LLM Service</h3><p>엔터프라이즈 AI와 LLM 워크로드를 위한 보안 영역입니다.</p><button class="button" disabled>Coming soon</button></div></article></div>`;
    if (path === '/customer/request') return `<div class="placeholder-card"><div class="stepper"><span class="active">1 Project</span><span>2 IaaS</span><span>3 PaaS</span><span>4 Policy</span><span>5 Cost</span><span>6 Review</span></div><h3>Cloud Platform configurator</h3><p>Phase 2에서 IaaS + PaaS 상세 설정 Wizard가 이 위치에 연결됩니다.</p><a class="button primary" href="#/customer/catalog">Back to catalog</a></div>`;
    if (path.includes('/requests') || path.includes('/approvals')) return `<div class="data-card"><div class="data-row"><strong>REQ-00291</strong><span>Cloud Platform · DEV</span><b class="status active">ACTIVE</b></div><div class="data-row"><strong>REQ-00290</strong><span>Cloud Platform · STG</span><b class="status pending">UNDER REVIEW</b></div><div class="data-row"><strong>REQ-00287</strong><span>Cloud Platform · DEV</span><b class="status closed">DESTROYED</b></div></div>`;
    if (path.startsWith('/admin') && account.role === 'MSP_OPERATOR') return `<div class="notice"><strong>Operator scope active</strong><p>Tenant and audit controls require MSP_ADMIN. API requests are denied server-side when the role is missing.</p></div>`;
    if (path.startsWith('/llm')) return `<div class="placeholder-card"><h3>LLM scope protected</h3><p>Only <code>LLM_USER</code> or an explicit <code>llm:invoke</code> scope can reach this portal.</p></div>`;
    return `<div class="placeholder-card"><h3>${escapeHtml(titleFor(path))}</h3><p>This Phase 1 route is ready for its domain module.</p></div>`;
  }

  function render(path) {
    if (!authReady) { renderSessionLoading(); return; }
    if (legacyCustomerRoutes[path]) { Router.navigate(legacyCustomerRoutes[path]); return; }
    const account = Auth.user();
    if (path === '/signup') { if (account) routeToDefault(account); else renderSignup(); return; }
    if (path === '/login' || !account) { if (path !== '/login' && !account) Router.navigate('/login'); else renderLogin(authError); return; }
    const policy = RBAC.routePolicy(path);
    if (!RBAC.canAccess(policy, account)) { renderShell('/forbidden', account); return; }
    renderShell(path, account);
  }
  Router.onChange(render);
  window.addEventListener('eclipse:auth-expired', () => {
    if (Auth.isDemoEnabled()) return;
    Auth.logout();
    authReady = true;
    authError = '조직 로그인 세션이 만료되었습니다. 다시 로그인해 주세요.';
    if (Router.path() === '/login') render('/login');
    else Router.navigate('/login');
  });
  window.EclipseApp = { refresh: () => render(Router.path()) };
  async function initialize() {
    if (!authReady) {
      renderSessionLoading();
      try { await Auth.bootstrap(); }
      catch (error) { authError = '보안 세션을 확인하지 못했습니다. 잠시 후 조직 계정으로 다시 로그인하세요.'; }
      authReady = true;
    }
    const account = Auth.user();
    if (account && ['/login', '/signup'].includes(Router.path())) routeToDefault(account);
    else render(Router.path());
  }
  initialize();
}());
