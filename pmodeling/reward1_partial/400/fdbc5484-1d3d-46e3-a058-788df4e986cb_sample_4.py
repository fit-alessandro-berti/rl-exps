import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
asset_id = Transition(label='Asset ID')
value_assess = Transition(label='Value Assess')
risk_scan = Transition(label='Risk Scan')
market_review = Transition(label='Market Review')
initial_offer = Transition(label='Initial Offer')
counter_offer = Transition(label='Counter Offer')
negotiation = Transition(label='Negotiation')
contract_draft = Transition(label='Contract Draft')
legal_review = Transition(label='Legal Review')
digital_sign = Transition(label='Digital Sign')
royalty_setup = Transition(label='Royalty Setup')
transfer_record = Transition(label='Transfer Record')
compliance_check = Transition(label='Compliance Check')
audit_schedule = Transition(label='Audit Schedule')
market_feedback = Transition(label='Market Feedback')
strategy_update = Transition(label='Strategy Update')

# Define the POWL model
xor1 = OperatorPOWL(operator=Operator.XOR, children=[initial_offer, counter_offer])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[negotiation, contract_draft])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[legal_review, digital_sign])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[royalty_setup, transfer_record])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, audit_schedule])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[market_feedback, strategy_update])

root = StrictPartialOrder(nodes=[asset_id, value_assess, risk_scan, market_review, xor1, xor2, xor3, xor4, xor5, xor6])
root.order.add_edge(asset_id, value_assess)
root.order.add_edge(value_assess, risk_scan)
root.order.add_edge(risk_scan, market_review)
root.order.add_edge(market_review, xor1)
root.order.add_edge(market_review, xor2)
root.order.add_edge(xor1, xor3)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)

print(root)