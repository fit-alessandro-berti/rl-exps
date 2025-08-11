import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define the loop for flight launch and return flight
loop_flight = OperatorPOWL(operator=Operator.LOOP, children=[flight_launch, return_flight])

# Define the XOR for delivery verify and biometric scan
xor_delivery = OperatorPOWL(operator=Operator.XOR, children=[delivery_verify, biometric_scan])

# Define the root POWL model
root = StrictPartialOrder(nodes=[loop_flight, xor_delivery])
root.order.add_edge(loop_flight, xor_delivery)

# Print the root POWL model
print(root)