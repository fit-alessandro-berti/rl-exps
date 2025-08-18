import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

order_validate = Transition(label='Order Validate')
route_optimize = Transition(label='Route Optimize')
drone_assign = Transition(label='Drone Assign')
preflight_check = Transition(label='Preflight Check')
load_package = Transition(label='Load Package')
flight_launch = Transition(label='Flight Launch')
traffic_monitor = Transition(label='Traffic Monitor')
weather_assess = Transition(label='Weather Assess')
obstacle_avoid = Transition(label='Obstacle Avoid')
battery_check = Transition(label='Battery Check')
delivery_verify = Transition(label='Delivery Verify')
biometric_scan = Transition(label='Biometric Scan')
package_release = Transition(label='Package Release')
return_flight = Transition(label='Return Flight')
post_flight = Transition(label='Post Flight')
data_analyze = Transition(label='Data Analyze')
feedback_collect = Transition(label='Feedback Collect')

loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[preflight_check, load_package, flight_launch])
loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[traffic_monitor, weather_assess, obstacle_avoid, battery_check, delivery_verify, biometric_scan, package_release, return_flight])
xor = OperatorPOWL(operator=Operator.XOR, children=[post_flight, data_analyze, feedback_collect])

root = StrictPartialOrder(nodes=[order_validate, route_optimize, drone_assign, loop_1, loop_2, xor])
root.order.add_edge(order_validate, route_optimize)
root.order.add_edge(route_optimize, drone_assign)
root.order.add_edge(drone_assign, loop_1)
root.order.add_edge(loop_1, loop_2)
root.order.add_edge(loop_2, xor)