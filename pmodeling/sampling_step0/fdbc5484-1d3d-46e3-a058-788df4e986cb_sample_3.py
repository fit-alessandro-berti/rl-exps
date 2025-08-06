import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define silent transitions
skip = SilentTransition()

# Define the POWL model
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[negotiation, counter_offer, initial_offer])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[market_review, risk_scan, value_assess, asset_id])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[skip, loop1])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[skip, loop2])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[xor1, xor2])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[royalty_setup, digital_sign])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[legal_review, contract_draft])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[transfer_record, compliance_check])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[audit_schedule, market_feedback])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[strategy_update, xor7])

# Create the root of the POWL model
root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)

print(root)