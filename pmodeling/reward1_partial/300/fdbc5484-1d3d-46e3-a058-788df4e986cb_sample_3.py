import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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
loop = OperatorPOWL(operator=Operator.LOOP, children=[market_review, initial_offer, counter_offer, negotiation])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[contract_draft, legal_review])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[digital_sign, royalty_setup])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[transfer_record, compliance_check])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[audit_schedule, market_feedback])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[strategy_update, skip])

# Connect the nodes in the POWL model
root = StrictPartialOrder(nodes=[loop, xor1, xor2, xor3, xor4, xor5])
root.order.add_edge(loop, xor1)
root.order.add_edge(loop, xor2)
root.order.add_edge(loop, xor3)
root.order.add_edge(loop, xor4)
root.order.add_edge(loop, xor5)

print(root)