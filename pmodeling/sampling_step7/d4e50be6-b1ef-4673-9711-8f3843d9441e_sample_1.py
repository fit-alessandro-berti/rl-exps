from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
patent_scouting = Transition(label='Patent Scouting')
technical_review = Transition(label='Technical Review')
legal_audit = Transition(label='Legal Audit')
market_analysis = Transition(label='Market Analysis')
valuation_modeling = Transition(label='Valuation Modeling')
risk_assessment = Transition(label='Risk Assessment')
license_targeting = Transition(label='License Targeting')
buyer_outreach = Transition(label='Buyer Outreach')
negotiation_phase = Transition(label='Negotiation Phase')
contract_drafting = Transition(label='Contract Drafting')
approval_process = Transition(label='Approval Process')
portfolio_tracking = Transition(label='Portfolio Tracking')
revenue_monitoring = Transition(label='Revenue Monitoring')
compliance_check = Transition(label='Compliance Check')
innovation_scan = Transition(label='Innovation Scan')
renewal_management = Transition(label='Renewal Management')

# Define the partial order
root = StrictPartialOrder(nodes=[
    patent_scouting, technical_review, legal_audit, market_analysis, valuation_modeling,
    risk_assessment, license_targeting, buyer_outreach, negotiation_phase, contract_drafting,
    approval_process, portfolio_tracking, revenue_monitoring, compliance_check, innovation_scan,
    renewal_management
])

# Define the dependencies between activities
root.order.add_edge(patent_scouting, technical_review)
root.order.add_edge(technical_review, legal_audit)
root.order.add_edge(legal_audit, market_analysis)
root.order.add_edge(market_analysis, valuation_modeling)
root.order.add_edge(valuation_modeling, risk_assessment)
root.order.add_edge(risk_assessment, license_targeting)
root.order.add_edge(license_targeting, buyer_outreach)
root.order.add_edge(buyer_outreach, negotiation_phase)
root.order.add_edge(negotiation_phase, contract_drafting)
root.order.add_edge(contract_drafting, approval_process)
root.order.add_edge(approval_process, portfolio_tracking)
root.order.add_edge(portfolio_tracking, revenue_monitoring)
root.order.add_edge(revenue_monitoring, compliance_check)
root.order.add_edge(compliance_check, innovation_scan)
root.order.add_edge(innovation_scan, renewal_management)

# Print the root POWL model
print(root)