import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define transitions (activities)
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

# Define the workflow structure
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[payload_assess, drone_configure, regulation_check, flight_simulate, route_optimize])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[pre_flight_inspect, weather_monitor, launch_drone, flight_track])
choice = OperatorPOWL(operator=Operator.XOR, children=[delivery_confirm, data_analyze, feedback_collect])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[warranty_register, issue_resolve])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[package_secure, package_return])

# Initialize the root node as a strict partial order
root = StrictPartialOrder(nodes=[loop1, loop2, choice, loop3, loop4])

# Add dependencies between nodes
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, choice)
root.order.add_edge(choice, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, loop1)

print("POWL model generated successfully.")