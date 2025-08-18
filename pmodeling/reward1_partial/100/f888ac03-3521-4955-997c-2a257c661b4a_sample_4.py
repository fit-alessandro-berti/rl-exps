import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define the control flow
xor1 = OperatorPOWL(operator=Operator.XOR, children=[order_validate, route_optimize])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[drone_assign, xor1])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[preflight_check, xor2])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[load_package, xor3])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[flight_launch, xor4])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[traffic_monitor, xor5])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[weather_assess, xor6])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[obstacle_avoid, xor7])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[battery_check, xor8])
xor10 = OperatorPOWL(operator=Operator.XOR, children=[delivery_verify, xor9])
xor11 = OperatorPOWL(operator=Operator.XOR, children=[biometric_scan, xor10])
xor12 = OperatorPOWL(operator=Operator.XOR, children=[package_release, xor11])
xor13 = OperatorPOWL(operator=Operator.XOR, children=[return_flight, xor12])
xor14 = OperatorPOWL(operator=Operator.XOR, children=[post_flight, xor13])
xor15 = OperatorPOWL(operator=Operator.XOR, children=[data_analyze, xor14])
xor16 = OperatorPOWL(operator=Operator.XOR, children=[feedback_collect, xor15])

# Define the partial order
root = StrictPartialOrder(nodes=[xor16])

# Add the edges to the partial order
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)
root.order.add_edge(xor8, xor9)
root.order.add_edge(xor9, xor10)
root.order.add_edge(xor10, xor11)
root.order.add_edge(xor11, xor12)
root.order.add_edge(xor12, xor13)
root.order.add_edge(xor13, xor14)
root.order.add_edge(xor14, xor15)
root.order.add_edge(xor15, xor16)

print(root)