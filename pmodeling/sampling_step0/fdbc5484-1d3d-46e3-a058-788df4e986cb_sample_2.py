import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
Asset_ID = Transition(label='Asset ID')
Value_Assess = Transition(label='Value Assess')
Risk_Scan = Transition(label='Risk Scan')
Market_Review = Transition(label='Market Review')
Initial_Offer = Transition(label='Initial Offer')
Counter_Offer = Transition(label='Counter Offer')
Negotiation = Transition(label='Negotiation')
Contract_Draft = Transition(label='Contract Draft')
Legal_Review = Transition(label='Legal Review')
Digital_Sign = Transition(label='Digital Sign')
Royalty_Setup = Transition(label='Royalty Setup')
Transfer_Record = Transition(label='Transfer Record')
Compliance_Check = Transition(label='Compliance Check')
Audit_Schedule = Transition(label='Audit Schedule')
Market_Feedback = Transition(label='Market Feedback')
Strategy_Update = Transition(label='Strategy Update')

skip = SilentTransition()

loop = OperatorPOWL(operator=Operator.LOOP, children=[Market_Review, Initial_Offer, Counter_Offer, Negotiation])
xor = OperatorPOWL(operator=Operator.XOR, children=[skip, Royalty_Setup, Digital_Sign, Legal_Review])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[skip, Transfer_Record, Compliance_Check])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[skip, Audit_Schedule, Market_Feedback])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[skip, Strategy_Update])

root = StrictPartialOrder(nodes=[loop, xor, xor2, xor3, xor4])
root.order.add_edge(loop, xor)
root.order.add_edge(loop, xor2)
root.order.add_edge(loop, xor3)
root.order.add_edge(loop, xor4)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor, xor3)
root.order.add_edge(xor, xor4)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor2, xor4)
root.order.add_edge(xor3, xor4)

# Print the root of the POWL model
print(root)