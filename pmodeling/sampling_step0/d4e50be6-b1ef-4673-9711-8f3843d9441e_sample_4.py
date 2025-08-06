import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define silent transitions (empty labels)
skip = SilentTransition()

# Define control flow
patent_scouting_next = OperatorPOWL(operator=Operator.AND, children=[patent_scouting, technical_review, legal_audit, market_analysis, valuation_modeling, risk_assessment])
license_targeting_next = OperatorPOWL(operator=Operator.AND, children=[license_targeting, buyer_outreach, negotiation_phase, contract_drafting, approval_process])
portfolio_tracking_next = OperatorPOWL(operator=Operator.AND, children=[portfolio_tracking, revenue_monitoring, compliance_check, renewal_management])
innovation_scan_next = OperatorPOWL(operator=Operator.AND, children=[innovation_scan])

# Define loop nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[patent_scouting_next, license_targeting_next, portfolio_tracking_next, innovation_scan_next])

# Define partial order
root = StrictPartialOrder(nodes=[loop1])
root.order.add_edge(loop1, innovation_scan_next)