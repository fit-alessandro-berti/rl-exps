import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

# Define the process structure
loop_payload_assess = OperatorPOWL(operator=Operator.LOOP, children=[payload_assess])
xor_drone_configure = OperatorPOWL(operator=Operator.XOR, children=[drone_configure, skip])
xor_regulation_check = OperatorPOWL(operator=Operator.XOR, children=[regulation_check, skip])
xor_flight_simulate = OperatorPOWL(operator=Operator.XOR, children=[flight_simulate, skip])
xor_route_optimize = OperatorPOWL(operator=Operator.XOR, children=[route_optimize, skip])
xor_package_secure = OperatorPOWL(operator=Operator.XOR, children=[package_secure, skip])
xor_pre_flight_inspect = OperatorPOWL(operator=Operator.XOR, children=[pre_flight_inspect, skip])
xor_weather_monitor = OperatorPOWL(operator=Operator.XOR, children=[weather_monitor, skip])
xor_launch_drone = OperatorPOWL(operator=Operator.XOR, children=[launch_drone, skip])
xor_flight_track = OperatorPOWL(operator=Operator.XOR, children=[flight_track, skip])
xor_delivery_confirm = OperatorPOWL(operator=Operator.XOR, children=[delivery_confirm, skip])
xor_data_analyze = OperatorPOWL(operator=Operator.XOR, children=[data_analyze, skip])
xor_feedback_collect = OperatorPOWL(operator=Operator.XOR, children=[feedback_collect, skip])
xor_warranty_register = OperatorPOWL(operator=Operator.XOR, children=[warranty_register, skip])
xor_issue_resolve = OperatorPOWL(operator=Operator.XOR, children=[issue_resolve, skip])
xor_package_return = OperatorPOWL(operator=Operator.XOR, children=[package_return, skip])

root = StrictPartialOrder(nodes=[
    loop_payload_assess,
    xor_drone_configure,
    xor_regulation_check,
    xor_flight_simulate,
    xor_route_optimize,
    xor_package_secure,
    xor_pre_flight_inspect,
    xor_weather_monitor,
    xor_launch_drone,
    xor_flight_track,
    xor_delivery_confirm,
    xor_data_analyze,
    xor_feedback_collect,
    xor_warranty_register,
    xor_issue_resolve,
    xor_package_return
])

# Define the order of execution
root.order.add_edge(loop_payload_assess, xor_drone_configure)
root.order.add_edge(xor_drone_configure, xor_regulation_check)
root.order.add_edge(xor_regulation_check, xor_flight_simulate)
root.order.add_edge(xor_flight_simulate, xor_route_optimize)
root.order.add_edge(xor_route_optimize, xor_package_secure)
root.order.add_edge(xor_package_secure, xor_pre_flight_inspect)
root.order.add_edge(xor_pre_flight_inspect, xor_weather_monitor)
root.order.add_edge(xor_weather_monitor, xor_launch_drone)
root.order.add_edge(xor_launch_drone, xor_flight_track)
root.order.add_edge(xor_flight_track, xor_delivery_confirm)
root.order.add_edge(xor_delivery_confirm, xor_data_analyze)
root.order.add_edge(xor_data_analyze, xor_feedback_collect)
root.order.add_edge(xor_feedback_collect, xor_warranty_register)
root.order.add_edge(xor_warranty_register, xor_issue_resolve)
root.order.add_edge(xor_issue_resolve, xor_package_return)

print(root)