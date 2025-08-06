from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities
client_consult = Transition(label='Client Consult')
payload_assess = Transition(label='Payload Assess')
drone_configure = Transition(label='Drone Configure')
regulation_check = Transition(label='Regulation Check')
flight_simulate = Transition(label='Flight Simulate')
route_optimize = Transition(label='Route Optimize')
package_secure = Transition(label='Package Secure')
pre_flight_inspect = Transition(label='Pre-Flight Inspect')
weather_monitor = Transition(label='Weather Monitor')
launch_drone = Transition(label='Launch Drone')
flight_track = Transition(label='Flight Track')
delivery_confirm = Transition(label='Delivery Confirm')
data_analyze = Transition(label='Data Analyze')
feedback_collect = Transition(label='Feedback Collect')
warranty_register = Transition(label='Warranty Register')
issue_resolve = Transition(label='Issue Resolve')
package_return = Transition(label='Package Return')

# Define silent transitions
skip = SilentTransition()

# Define the workflow
loop = OperatorPOWL(operator=Operator.LOOP, children=[flight_simulate, pre_flight_inspect, weather_monitor, launch_drone, flight_track, delivery_confirm])
xor = OperatorPOWL(operator=Operator.XOR, children=[route_optimize, skip])
root = StrictPartialOrder(nodes=[loop, xor])

# Define the dependencies
root.order.add_edge(loop, xor)

# Print the result
print(root)