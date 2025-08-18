from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

# Define the operators
xor = OperatorPOWL(operator=Operator.XOR, children=[package_secure, weather_monitor])
loop = OperatorPOWL(operator=Operator.LOOP, children=[pre_flight_inspect, launch_drone, flight_track, delivery_confirm, data_analyze, feedback_collect])
partial_order = StrictPartialOrder(nodes=[client_consult, payload_assess, drone_configure, regulation_check, flight_simulate, route_optimize, xor, loop])

# Define the partial order dependencies
partial_order.order.add_edge(client_consult, payload_assess)
partial_order.order.add_edge(payload_assess, drone_configure)
partial_order.order.add_edge(drone_configure, regulation_check)
partial_order.order.add_edge(regulation_check, flight_simulate)
partial_order.order.add_edge(flight_simulate, route_optimize)
partial_order.order.add_edge(route_optimize, xor)
partial_order.order.add_edge(xor, loop)
partial_order.order.add_edge(loop, xor)

# Define the final root
root = partial_order