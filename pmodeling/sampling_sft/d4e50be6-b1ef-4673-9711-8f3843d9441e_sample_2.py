import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
patent_scouting    = Transition(label='Patent Scouting')
technical_review   = Transition(label='Technical Review')
legal_audit        = Transition(label='Legal Audit')
market_analysis    = Transition(label='Market Analysis')
valuation_model    = Transition(label='Valuation Modeling')
risk_assessment    = Transition(label='Risk Assessment')
license_targeting  = Transition(label='License Targeting')
buyer_outreach     = Transition(label='Buyer Outreach')
negotiation_phase  = Transition(label='Negotiation Phase')
contract_drafting  = Transition(label='Contract Drafting')
approval_process   = Transition(label='Approval Process')
portfolio_tracking = Transition(label='Portfolio Tracking')
revenue_monitoring = Transition(label='Revenue Monitoring')
compliance_check   = Transition(label='Compliance Check')
innovation_scan    = Transition(label='Innovation Scan')
renewal_management = Transition(label='Renewal Management')

# Build the loop body: negotiation_phase -> contract_drafting -> approval_process
body = StrictPartialOrder(nodes=[negotiation_phase, contract_drafting, approval_process])
body.order.add_edge(negotiation_phase, contract_drafting)
body.order.add_edge(contract_drafting, approval_process)

# LOOP: perform the body, then optionally scan innovation and renew, then repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[body, innovation_scan])

# Build the root partial order
root = StrictPartialOrder(nodes=[
    patent_scouting,
    technical_review,
    legal_audit,
    market_analysis,
    valuation_model,
    risk_assessment,
    license_targeting,
    buyer_outreach,
    loop,
    portfolio_tracking,
    revenue_monitoring,
    compliance_check
])

# Add the control-flow edges
root.order.add_edge(patent_scouting, technical_review)
root.order.add_edge(technical_review, legal_audit)
root.order.add_edge(legal_audit, market_analysis)
root.order.add_edge(market_analysis, valuation_model)
root.order.add_edge(valuation_model, risk_assessment)
root.order.add_edge(risk_assessment, license_targeting)
root.order.add_edge(license_targeting, buyer_outreach)
root.order.add_edge(buyer_outreach, loop)
root.order.add_edge(loop, portfolio_tracking)
root.order.add_edge(portfolio_tracking, revenue_monitoring)
root.order.add_edge(revenue_monitoring, compliance_check)