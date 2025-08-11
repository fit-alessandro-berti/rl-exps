import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
Drone_Design = Transition(label='Drone Design')
Regulatory_Check = Transition(label='Regulatory Check')
Nav_System = Transition(label='Nav System')
Partner_Setup = Transition(label='Partner Setup')
Operator_Training = Transition(label='Operator Training')
Test_Flights = Transition(label='Test Flights')
Weather_Review = Transition(label='Weather Review')
Route_Optimize = Transition(label='Route Optimize')
Parts_Logistics = Transition(label='Parts Logistics')
Feedback_Loop = Transition(label='Feedback Loop')
Risk_Assess = Transition(label='Risk Assess')
Emergency_Plan = Transition(label='Emergency Plan')
Compliance_Audit = Transition(label='Compliance Audit')
Data_Sync = Transition(label='Data Sync')
Service_Launch = Transition(label='Service Launch')

# Define silent transitions
skip = SilentTransition()

# Define loops and XORs
loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[Nav_System, Regulatory_Check])
loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[Partner_Setup, Operator_Training])
loop_3 = OperatorPOWL(operator=Operator.LOOP, children=[Test_Flights, Weather_Review])
loop_4 = OperatorPOWL(operator=Operator.LOOP, children=[Route_Optimize, Parts_Logistics])
loop_5 = OperatorPOWL(operator=Operator.LOOP, children=[Feedback_Loop, Risk_Assess])
loop_6 = OperatorPOWL(operator=Operator.LOOP, children=[Emergency_Plan, Compliance_Audit])
loop_7 = OperatorPOWL(operator=Operator.LOOP, children=[Data_Sync, Service_Launch])

xor_1 = OperatorPOWL(operator=Operator.XOR, children=[loop_1, skip])
xor_2 = OperatorPOWL(operator=Operator.XOR, children=[loop_2, skip])
xor_3 = OperatorPOWL(operator=Operator.XOR, children=[loop_3, skip])
xor_4 = OperatorPOWL(operator=Operator.XOR, children=[loop_4, skip])
xor_5 = OperatorPOWL(operator=Operator.XOR, children=[loop_5, skip])
xor_6 = OperatorPOWL(operator=Operator.XOR, children=[loop_6, skip])
xor_7 = OperatorPOWL(operator=Operator.XOR, children=[loop_7, skip])

# Define root
root = StrictPartialOrder(nodes=[xor_1, xor_2, xor_3, xor_4, xor_5, xor_6, xor_7])
root.order.add_edge(xor_1, loop_1)
root.order.add_edge(xor_2, loop_2)
root.order.add_edge(xor_3, loop_3)
root.order.add_edge(xor_4, loop_4)
root.order.add_edge(xor_5, loop_5)
root.order.add_edge(xor_6, loop_6)
root.order.add_edge(xor_7, loop_7)

# Print the result
print(root)