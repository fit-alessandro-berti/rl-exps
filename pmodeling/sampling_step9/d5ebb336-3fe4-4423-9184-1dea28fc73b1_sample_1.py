import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
Data_Collection = Transition(label='Data Collection')
Point_Aggregation = Transition(label='Point Aggregation')
Conflict_Check = Transition(label='Conflict Check')
Fraud_Scan = Transition(label='Fraud Scan')
Reward_Adjust = Transition(label='Reward Adjust')
Redemption_Verify = Transition(label='Redemption Verify')
Partner_Sync = Transition(label='Partner Sync')
Behavior_Analyze = Transition(label='Behavior Analyze')
Async_Update = Transition(label='Async Update')
Rollback_Trigger = Transition(label='Rollback Trigger')
Compliance_Check = Transition(label='Compliance Check')
Notification_Send = Transition(label='Notification Send')
User_Feedback = Transition(label='User Feedback')
Report_Generate = Transition(label='Report Generate')
System_Audit = Transition(label='System Audit')

# Define silent transitions
skip = SilentTransition()

# Define the loop nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[Point_Aggregation, Conflict_Check])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[Fraud_Scan, Reward_Adjust])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[Redemption_Verify, Partner_Sync])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[Behavior_Analyze, Async_Update])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[Rollback_Trigger, Compliance_Check])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[Notification_Send, User_Feedback])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[Report_Generate, System_Audit])

# Define the XOR nodes
xor1 = OperatorPOWL(operator=Operator.XOR, children=[loop1, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[loop2, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[loop3, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[loop4, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[loop5, skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[loop6, skip])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[loop7, skip])

# Create the root POWL model
root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5, xor6, xor7])

# Define the dependencies
root.order.add_edge(xor1, loop1)
root.order.add_edge(xor2, loop2)
root.order.add_edge(xor3, loop3)
root.order.add_edge(xor4, loop4)
root.order.add_edge(xor5, loop5)
root.order.add_edge(xor6, loop6)
root.order.add_edge(xor7, loop7)