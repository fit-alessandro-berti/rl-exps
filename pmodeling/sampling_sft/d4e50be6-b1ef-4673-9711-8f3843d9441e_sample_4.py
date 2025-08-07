import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
patent_scouting   = Transition(label='Patent Scouting')
technical_review  = Transition(label='Technical Review')
legal_audit       = Transition(label='Legal Audit')
market_analysis   = Transition(label='Market Analysis')
risk_assessment   = Transition(label='Risk Assessment')
valuation_model   = Transition(label='Valuation Modeling')
license_targeting = Transition(label='License Targeting')
buyer_outreach    = Transition(label='Buyer Outreach')
negotiation_phase = Transition(label='Negotiation Phase')
contract_drafting = Transition(label='Contract Drafting')
approval_process  = Transition(label='Approval Process')
portfolio_track   = Transition(label='Portfolio Tracking')
compliance_check  = Transition(label='Compliance Check')
innovation_scan   = Transition(label='Innovation Scan')
renewal_manage    = Transition(label='Renewal Management')
revenue_monitor   = Transition(label='Revenue Monitoring')

# Loop for ongoing innovation monitoring
innovation_loop = OperatorPOWL(operator=Operator.LOOP, children=[innovation_scan, renewal_manage])

# Build the partial order
root = StrictPartialOrder(nodes=[
    patent_scouting, technical_review, legal_audit, market_analysis, risk_assessment,
    valuation_model, license_targeting, buyer_outreach, negotiation_phase, contract_drafting,
    approval_process, portfolio_track, compliance_check, innovation_loop, revenue_monitor
])

# Define the control-flow dependencies
root.order.add_edge(patent_scouting, technical_review)
root.order.add_edge(patent_scouting, legal_audit)
root.order.add_edge(technical_review, market_analysis)
root.order.add_edge(technical_review, risk_assessment)
root.order.add_edge(legal_audit, market_analysis)
root.order.add_edge(legal_audit, risk_assessment)
root.order.add_edge(market_analysis, valuation_model)
root.order.add_edge(risk_assessment, valuation_model)
root.order.add_edge(valuation_model, license_targeting)
root.order.add_edge(license_targeting, buyer_outreach)
root.order.add_edge(buyer_outreach, negotiation_phase)
root.order.add_edge(negotiation_phase, contract_drafting)
root.order.add_edge(contract_drafting, approval_process)
root.order.add_edge(approval_process, portfolio_track)
root.order.add_edge(portfolio_track, compliance_check)
root.order.add_edge(compliance_check, innovation_loop)
root.order.add_edge(innovation_loop, revenue_monitor)