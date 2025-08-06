import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the silent transitions
skip = SilentTransition()

# Define the POWL model
loop_drone_assign = OperatorPOWL(operator=Operator.LOOP, children=[drone_assign, skip])
xor_preflight_check = OperatorPOWL(operator=Operator.XOR, children=[preflight_check, skip])
xor_battery_check = OperatorPOWL(operator=Operator.XOR, children=[battery_check, skip])
xor_weather_assess = OperatorPOWL(operator=Operator.XOR, children=[weather_assess, skip])
xor_traffic_monitor = OperatorPOWL(operator=Operator.XOR, children=[traffic_monitor, skip])
xor_obstacle_avoid = OperatorPOWL(operator=Operator.XOR, children=[obstacle_avoid, skip])
xor_return_flight = OperatorPOWL(operator=Operator.XOR, children=[return_flight, skip])
xor_post_flight = OperatorPOWL(operator=Operator.XOR, children=[post_flight, skip])
xor_data_analyze = OperatorPOWL(operator=Operator.XOR, children=[data_analyze, skip])
xor_feedback_collect = OperatorPOWL(operator=Operator.XOR, children=[feedback_collect, skip])

root = StrictPartialOrder(nodes=[loop_drone_assign, xor_preflight_check, xor_battery_check, xor_weather_assess, xor_traffic_monitor, xor_obstacle_avoid, xor_return_flight, xor_post_flight, xor_data_analyze, xor_feedback_collect])
root.order.add_edge(loop_drone_assign, xor_preflight_check)
root.order.add_edge(loop_drone_assign, xor_battery_check)
root.order.add_edge(loop_drone_assign, xor_weather_assess)
root.order.add_edge(loop_drone_assign, xor_traffic_monitor)
root.order.add_edge(loop_drone_assign, xor_obstacle_avoid)
root.order.add_edge(loop_drone_assign, xor_return_flight)
root.order.add_edge(loop_drone_assign, xor_post_flight)
root.order.add_edge(loop_drone_assign, xor_data_analyze)
root.order.add_edge(loop_drone_assign, xor_feedback_collect)

print(root)