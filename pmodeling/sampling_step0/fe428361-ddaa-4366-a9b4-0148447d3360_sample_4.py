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

# Define the silent activities
skip = SilentTransition()

# Define the POWL model
loop = OperatorPOWL(operator=Operator.LOOP, children=[pre_flight_inspect, launch_drone])
xor = OperatorPOWL(operator=Operator.XOR, children=[package_secure, skip])
root = StrictPartialOrder(nodes=[loop, xor])

# Define the partial order
root.order.add_edge(loop, xor)
root.order.add_edge(xor, data_analyze)
root.order.add_edge(xor, feedback_collect)
root.order.add_edge(xor, warranty_register)
root.order.add_edge(xor, issue_resolve)
root.order.add_edge(xor, package_return)
root.order.add_edge(data_analyze, delivery_confirm)
root.order.add_edge(feedback_collect, delivery_confirm)
root.order.add_edge(warranty_register, delivery_confirm)
root.order.add_edge(issue_resolve, delivery_confirm)
root.order.add_edge(package_return, delivery_confirm)

# Define the exclusive choices
root.order.add_edge(client_consult, payload_assess)
root.order.add_edge(payload_assess, drone_configure)
root.order.add_edge(drone_configure, regulation_check)
root.order.add_edge(regulation_check, flight_simulate)
root.order.add_edge(flight_simulate, route_optimize)
root.order.add_edge(route_optimize, package_secure)
root.order.add_edge(package_secure, pre_flight_inspect)
root.order.add_edge(pre_flight_inspect, launch_drone)
root.order.add_edge(launch_drone, flight_track)
root.order.add_edge(flight_track, weather_monitor)

# Print the POWL model
print(root)