from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define loop and XOR operators
loop_drone_assign = OperatorPOWL(operator=Operator.LOOP, children=[drone_assign])
xor_flight_launch = OperatorPOWL(operator=Operator.XOR, children=[flight_launch, return_flight])
xor_traffic_monitor = OperatorPOWL(operator=Operator.XOR, children=[traffic_monitor, skip])
xor_weather_assess = OperatorPOWL(operator=Operator.XOR, children=[weather_assess, skip])
xor_battery_check = OperatorPOWL(operator=Operator.XOR, children=[battery_check, skip])
xor_delivery_verify = OperatorPOWL(operator=Operator.XOR, children=[delivery_verify, skip])
xor_biometric_scan = OperatorPOWL(operator=Operator.XOR, children=[biometric_scan, skip])
xor_package_release = OperatorPOWL(operator=Operator.XOR, children=[package_release, skip])
xor_return_flight = OperatorPOWL(operator=Operator.XOR, children=[return_flight, skip])
xor_post_flight = OperatorPOWL(operator=Operator.XOR, children=[post_flight, skip])
xor_data_analyze = OperatorPOWL(operator=Operator.XOR, children=[data_analyze, skip])
xor_feedback_collect = OperatorPOWL(operator=Operator.XOR, children=[feedback_collect, skip])

# Construct the POWL model
root = StrictPartialOrder(
    nodes=[order_validate, route_optimize, loop_drone_assign, xor_flight_launch, xor_traffic_monitor,
           xor_weather_assess, xor_battery_check, xor_delivery_verify, xor_biometric_scan, xor_package_release,
           xor_return_flight, xor_post_flight, xor_data_analyze, xor_feedback_collect],
    order={
        (order_validate, route_optimize): None,
        (route_optimize, loop_drone_assign): None,
        (loop_drone_assign, xor_flight_launch): None,
        (xor_flight_launch, xor_traffic_monitor): None,
        (xor_traffic_monitor, xor_weather_assess): None,
        (xor_weather_assess, xor_battery_check): None,
        (xor_battery_check, xor_delivery_verify): None,
        (xor_delivery_verify, xor_biometric_scan): None,
        (xor_biometric_scan, xor_package_release): None,
        (xor_package_release, xor_return_flight): None,
        (xor_return_flight, xor_post_flight): None,
        (xor_post_flight, xor_data_analyze): None,
        (xor_data_analyze, xor_feedback_collect): None
    }
)

print(root)