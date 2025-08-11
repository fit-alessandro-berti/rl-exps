import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

# Stage 1: Client Consult
client_consult_choice = OperatorPOWL(operator=Operator.XOR, children=[payload_assess, skip])

# Stage 2: Payload Assess and Drone Configure
payload_assess_choice = OperatorPOWL(operator=Operator.XOR, children=[drone_configure, skip])

# Stage 3: Regulation Check
regulation_check_choice = OperatorPOWL(operator=Operator.XOR, children=[flight_simulate, skip])

# Stage 4: Flight Simulate and Route Optimize
flight_simulate_choice = OperatorPOWL(operator=Operator.XOR, children=[route_optimize, skip])

# Stage 5: Package Secure, Pre-Flight Inspect, Weather Monitor, Launch Drone, Flight Track, Delivery Confirm
package_secure_loop = OperatorPOWL(operator=Operator.LOOP, children=[pre_flight_inspect, weather_monitor, launch_drone, flight_track, delivery_confirm])

# Stage 6: Data Analyze, Feedback Collect, Warranty Register, Issue Resolve, Package Return
data_analyze_choice = OperatorPOWL(operator=Operator.XOR, children=[warranty_register, issue_resolve, package_return])

# Root
root = StrictPartialOrder(nodes=[client_consult_choice, payload_assess_choice, regulation_check_choice, flight_simulate_choice, package_secure_loop, data_analyze_choice])
root.order.add_edge(client_consult_choice, payload_assess_choice)
root.order.add_edge(payload_assess_choice, drone_configure)
root.order.add_edge(drone_configure, regulation_check)
root.order.add_edge(regulation_check, flight_simulate)
root.order.add_edge(flight_simulate, route_optimize)
root.order.add_edge(route_optimize, pre_flight_inspect)
root.order.add_edge(pre_flight_inspect, weather_monitor)
root.order.add_edge(weather_monitor, launch_drone)
root.order.add_edge(launch_drone, flight_track)
root.order.add_edge(flight_track, delivery_confirm)
root.order.add_edge(delivery_confirm, package_secure_loop)
root.order.add_edge(package_secure_loop, warranty_register)
root.order.add_edge(package_secure_loop, issue_resolve)
root.order.add_edge(package_secure_loop, package_return)
root.order.add_edge(data_analyze_choice, warranty_register)
root.order.add_edge(data_analyze_choice, issue_resolve)
root.order.add_edge(data_analyze_choice, package_return)