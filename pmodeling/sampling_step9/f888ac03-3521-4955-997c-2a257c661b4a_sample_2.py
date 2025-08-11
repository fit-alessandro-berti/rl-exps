import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define silent activities
skip = SilentTransition()

# Define loops
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[flight_launch, post_flight, data_analyze, feedback_collect])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[return_flight])

# Define choices
xor1 = OperatorPOWL(operator=Operator.XOR, children=[traffic_monitor, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[weather_assess, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[obstacle_avoid, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[battery_check, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[delivery_verify, skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[biometric_scan, skip])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[package_release, skip])

# Define root model
root = StrictPartialOrder(nodes=[loop1, loop2, xor1, xor2, xor3, xor4, xor5, xor6, xor7])
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop1, xor2)
root.order.add_edge(loop1, xor3)
root.order.add_edge(loop1, xor4)
root.order.add_edge(loop1, xor5)
root.order.add_edge(loop1, xor6)
root.order.add_edge(loop1, xor7)
root.order.add_edge(loop2, xor7)
root.order.add_edge(xor1, flight_launch)
root.order.add_edge(xor2, flight_launch)
root.order.add_edge(xor3, flight_launch)
root.order.add_edge(xor4, flight_launch)
root.order.add_edge(xor5, flight_launch)
root.order.add_edge(xor6, flight_launch)
root.order.add_edge(xor7, return_flight)

print(root)