import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL nodes
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

# Define the POWL operators
xor = OperatorPOWL(operator=Operator.XOR, children=[license_targeting, buyer_outreach])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[negotiation_phase, contract_drafting])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[approval_process, compliance_check])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[portfolio_tracking, revenue_monitoring])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[innovation_scan, renewal_management])

# Create the POWL model
root = StrictPartialOrder(nodes=[patent_scouting, technical_review, legal_audit, market_analysis, valuation_modeling, risk_assessment, xor, xor2, xor3, xor4, xor5])
root.order.add_edge(patent_scouting, technical_review)
root.order.add_edge(technical_review, legal_audit)
root.order.add_edge(legal_audit, market_analysis)
root.order.add_edge(market_analysis, valuation_modeling)
root.order.add_edge(valuation_modeling, risk_assessment)
root.order.add_edge(risk_assessment, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)