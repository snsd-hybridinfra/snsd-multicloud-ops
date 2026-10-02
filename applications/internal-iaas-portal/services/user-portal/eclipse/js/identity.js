(function () {
  'use strict';

  const membersByTenant = {
    'abc-manufacturing': [
      {name:'Quality Engineer',userId:'quality.engineer',role:'CUSTOMER_USER',access:'Pending activation',status:'INVITED'},
    ],
    'developer-demo': [
      {name:'Demo User',userId:'demo-user',role:'CUSTOMER_USER',access:'Developer · Requests · LLM',status:'ACTIVE'},
      {name:'Developer User',userId:'developer-user',role:'CUSTOMER_USER',access:'Developer · Requests · LLM',status:'ACTIVE'},
    ],
    'hanbit-mobility': [
      {name:'Factory User',userId:'factory-user',role:'CUSTOMER_USER',access:'Requests · Infrastructure · FinOps',status:'ACTIVE'},
      {name:'MES Engineer',userId:'mes.engineer',role:'CUSTOMER_USER',access:'Requests · Infrastructure',status:'ACTIVE'},
      {name:'Plant Operator',userId:'plant.operator',role:'CUSTOMER_USER',access:'Monitoring · Infrastructure',status:'ACTIVE'},
    ],
    'demo-finance': [
      {name:'Finance User',userId:'finance-user',role:'CUSTOMER_USER',access:'Requests · Infrastructure · Compliance',status:'ACTIVE'},
      {name:'Risk Analyst',userId:'risk.analyst',role:'CUSTOMER_USER',access:'Resources · Monitoring',status:'ACTIVE'},
      {name:'Settlement Operator',userId:'settlement.operator',role:'CUSTOMER_USER',access:'Requests · Infrastructure',status:'INVITED'},
    ],
  };
  const esc = value => String(value == null ? '' : value).replace(/[&<>"']/g, char => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[char]));

  function renderTeam(account) {
    const members = membersByTenant[account.tenantId] || [];
    const managers = members.filter(member => member.role === 'CUSTOMER_MANAGER').length;
    const active = members.filter(member => member.status === 'ACTIVE').length;
    return `<div class="request-stats identity-summary"><article><span>Company users</span><strong>${members.length}</strong></article><article><span>Managers</span><strong>${managers}</strong></article><article><span>Active</span><strong>${active}</strong></article></div><article class="identity-role-guide"><div><small>CUSTOMER_USER</small><strong>서비스 이용</strong><p>부여된 산업 영역에서 상품 조회·요청과 LLM 서비스를 이용합니다.</p></div><div><small>CUSTOMER_MANAGER</small><strong>회사 사용자 현황 조회</strong><p>일반 사용자 기능에 더해 같은 회사 구성원 목록을 조회합니다.</p></div><p>계정 초대·역할 변경·산업 권한 승격은 이 화면에서 할 수 없으며 MSP 관리자가 처리합니다.</p></article><article class="data-card"><div class="card-head"><div><h3>${esc(account.tenantName)} members</h3><p>Tenant-scoped identities · DEMO DATA</p></div><b>team:read</b></div><div class="identity-table"><div class="table-head"><span>Member</span><span>Role</span><span>Access</span><span>Status</span></div>${members.map(member => `<div><span><strong>${esc(member.name)}</strong><small>${esc(member.userId)}</small></span><span><code>${esc(member.role)}</code></span><span>${esc(member.access)}</span><span><em class="domain-status ${member.status.toLowerCase()}">${esc(member.status)}</em></span></div>`).join('')}</div></article>`;
  }

  window.EclipseIdentity = {renderTeam, membersByTenant};
}());
