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

# Create the POWL model
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[Asset_ID, Value_Assess, Risk_Scan, Market_Review, Initial_Offer, Counter_Offer, Negotiation])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[Royalty_Setup, Digital_Sign])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[Legal_Review, Compliance_Check, Audit_Schedule, Market_Feedback])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[Strategy_Update, Transfer_Record])

root = StrictPartialOrder(nodes=[loop1, xor1, loop2, xor2])
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop2, xor2)

print(root)