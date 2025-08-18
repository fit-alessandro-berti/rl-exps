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

# Define the workflow
client_consult_to_payload_assess = OperatorPOWL(operator=Operator.XOR, children=[client_consult, payload_assess])
payload_assess_to_drone_configure = OperatorPOWL(operator=Operator.XOR, children=[payload_assess, drone_configure])
drone_configure_to_regulation_check = OperatorPOWL(operator=Operator.XOR, children=[drone_configure, regulation_check])
regulation_check_to_flight_simulate = OperatorPOWL(operator=Operator.XOR, children=[regulation_check, flight_simulate])
flight_simulate_to_route_optimize = OperatorPOWL(operator=Operator.XOR, children=[flight_simulate, route_optimize])
route_optimize_to_package_secure = OperatorPOWL(operator=Operator.XOR, children=[route_optimize, package_secure])
package_secure_to_pre_flight_inspect = OperatorPOWL(operator=Operator.XOR, children=[package_secure, pre_flight_inspect])
pre_flight_inspect_to_weather_monitor = OperatorPOWL(operator=Operator.XOR, children=[pre_flight_inspect, weather_monitor])
weather_monitor_to_launch_drone = OperatorPOWL(operator=Operator.XOR, children=[weather_monitor, launch_drone])
launch_drone_to_flight_track = OperatorPOWL(operator=Operator.XOR, children=[launch_drone, flight_track])
flight_track_to_delivery_confirm = OperatorPOWL(operator=Operator.XOR, children=[flight_track, delivery_confirm])
delivery_confirm_to_data_analyze = OperatorPOWL(operator=Operator.XOR, children=[delivery_confirm, data_analyze])
data_analyze_to_feedback_collect = OperatorPOWL(operator=Operator.XOR, children=[data_analyze, feedback_collect])
feedback_collect_to_warranty_register = OperatorPOWL(operator=Operator.XOR, children=[feedback_collect, warranty_register])
warranty_register_to_issue_resolve = OperatorPOWL(operator=Operator.XOR, children=[warranty_register, issue_resolve])
issue_resolve_to_package_return = OperatorPOWL(operator=Operator.XOR, children=[issue_resolve, package_return])

# Define the partial order
root = StrictPartialOrder(nodes=[
    client_consult_to_payload_assess,
    payload_assess_to_drone_configure,
    drone_configure_to_regulation_check,
    regulation_check_to_flight_simulate,
    flight_simulate_to_route_optimize,
    route_optimize_to_package_secure,
    package_secure_to_pre_flight_inspect,
    pre_flight_inspect_to_weather_monitor,
    weather_monitor_to_launch_drone,
    launch_drone_to_flight_track,
    flight_track_to_delivery_confirm,
    delivery_confirm_to_data_analyze,
    data_analyze_to_feedback_collect,
    feedback_collect_to_warranty_register,
    warranty_register_to_issue_resolve,
    issue_resolve_to_package_return
])

# Define the dependencies
root.order.add_edge(client_consult_to_payload_assess, payload_assess_to_drone_configure)
root.order.add_edge(payload_assess_to_drone_configure, drone_configure_to_regulation_check)
root.order.add_edge(drone_configure_to_regulation_check, regulation_check_to_flight_simulate)
root.order.add_edge(regulation_check_to_flight_simulate, flight_simulate_to_route_optimize)
root.order.add_edge(flight_simulate_to_route_optimize, route_optimize_to_package_secure)
root.order.add_edge(route_optimize_to_package_secure, package_secure_to_pre_flight_inspect)
root.order.add_edge(package_secure_to_pre_flight_inspect, pre_flight_inspect_to_weather_monitor)
root.order.add_edge(pre_flight_inspect_to_weather_monitor, weather_monitor_to_launch_drone)
root.order.add_edge(weather_monitor_to_launch_drone, launch_drone_to_flight_track)
root.order.add_edge(launch_drone_to_flight_track, flight_track_to_delivery_confirm)
root.order.add_edge(flight_track_to_delivery_confirm, delivery_confirm_to_data_analyze)
root.order.add_edge(delivery_confirm_to_data_analyze, data_analyze_to_feedback_collect)
root.order.add_edge(data_analyze_to_feedback_collect, feedback_collect_to_warranty_register)
root.order.add_edge(feedback_collect_to_warranty_register, warranty_register_to_issue_resolve)
root.order.add_edge(warranty_register_to_issue_resolve, issue_resolve_to_package_return)