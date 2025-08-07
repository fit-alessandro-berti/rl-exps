import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
client_consult = Transition(label='Client Consult')
payload_assess = Transition(label='Payload Assess')
drone_configure = Transition(label='Drone Configure')
regulation_check = Transition(label='Regulation Check')
flight_simulate = Transition(label='Flight Simulate')
route_optimize = Transition(label='Route Optimize')
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

# Define the loop for handling potential issues during flight
loop_body = StrictPartialOrder(nodes=[weather_monitor, launch_drone, flight_track])
loop_body.order.add_edge(weather_monitor, launch_drone)
loop_body.order.add_edge(launch_drone, flight_track)

loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, issue_resolve])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    client_consult,
    payload_assess,
    drone_configure,
    regulation_check,
    flight_simulate,
    route_optimize,
    pre_flight_inspect,
    loop,
    data_analyze,
    feedback_collect,
    warranty_register,
    delivery_confirm,
    package_return
])

# Define the control-flow dependencies
root.order.add_edge(client_consult, payload_assess)
root.order.add_edge(payload_assess, drone_configure)
root.order.add_edge(drone_configure, regulation_check)
root.order.add_edge(regulation_check, flight_simulate)
root.order.add_edge(flight_simulate, route_optimize)
root.order.add_edge(route_optimize, pre_flight_inspect)
root.order.add_edge(pre_flight_inspect, loop)
root.order.add_edge(loop, data_analyze)
root.order.add_edge(data_analyze, feedback_collect)
root.order.add_edge(feedback_collect, warranty_register)
root.order.add_edge(warranty_register, delivery_confirm)
root.order.add_edge(delivery_confirm, package_return)