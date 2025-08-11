import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Client_Consult = Transition(label='Client Consult')
Payload_Assess = Transition(label='Payload Assess')
Drone_Configure = Transition(label='Drone Configure')
Regulation_Check = Transition(label='Regulation Check')
Flight_Simulate = Transition(label='Flight Simulate')
Route_Optimize = Transition(label='Route Optimize')
Package_Secure = Transition(label='Package Secure')
Pre_Flight_Inspect = Transition(label='Pre-Flight Inspect')
Weather_Monitor = Transition(label='Weather Monitor')
Launch_Drone = Transition(label='Launch Drone')
Flight_Track = Transition(label='Flight Track')
Delivery_Confirm = Transition(label='Delivery Confirm')
Data_Analyze = Transition(label='Data Analyze')
Feedback_Collect = Transition(label='Feedback Collect')
Warranty_Register = Transition(label='Warranty Register')
Issue_Resolve = Transition(label='Issue Resolve')
Package_Return = Transition(label='Package Return')

skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[Pre_Flight_Inspect, Weather_Monitor])
xor = OperatorPOWL(operator=Operator.XOR, children=[Launch_Drone, skip])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)