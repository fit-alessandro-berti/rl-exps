import pm4py
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

# Define silent transitions
skip = SilentTransition()

# Define loop nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[patent_scouting, technical_review, legal_audit, market_analysis, valuation_modeling, risk_assessment])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[license_targeting, buyer_outreach, negotiation_phase, contract_drafting, approval_process, portfolio_tracking, revenue_monitoring, compliance_check, innovation_scan, renewal_management])

# Define exclusive choice nodes
xor1 = OperatorPOWL(operator=Operator.XOR, children=[skip, loop1])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[skip, loop2])

# Define root POWL model
root = StrictPartialOrder(nodes=[xor1, xor2])
root.order.add_edge(xor1, xor2)

print(root)