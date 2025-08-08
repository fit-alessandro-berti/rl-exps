from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define the process model
root = StrictPartialOrder(nodes=[
    Asset_ID, Value_Assess, Risk_Scan, Market_Review, Initial_Offer, Counter_Offer, Negotiation, 
    Contract_Draft, Legal_Review, Digital_Sign, Royalty_Setup, Transfer_Record, Compliance_Check, 
    Audit_Schedule, Market_Feedback, Strategy_Update
])

# Define the partial order dependencies
root.order.add_edge(Asset_ID, Value_Assess)
root.order.add_edge(Value_Assess, Risk_Scan)
root.order.add_edge(Risk_Scan, Market_Review)
root.order.add_edge(Market_Review, Initial_Offer)
root.order.add_edge(Initial_Offer, Counter_Offer)
root.order.add_edge(Counter_Offer, Negotiation)
root.order.add_edge(Negotiation, Contract_Draft)
root.order.add_edge(Contract_Draft, Legal_Review)
root.order.add_edge(Legal_Review, Digital_Sign)
root.order.add_edge(Digital_Sign, Royalty_Setup)
root.order.add_edge(Royalty_Setup, Transfer_Record)
root.order.add_edge(Transfer_Record, Compliance_Check)
root.order.add_edge(Compliance_Check, Audit_Schedule)
root.order.add_edge(Audit_Schedule, Market_Feedback)
root.order.add_edge(Market_Feedback, Strategy_Update)

# Print the root model
print(root)