import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities)
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

# Define silent transitions (for no-operation)
skip = SilentTransition()

# Define the partial order for the process
root = StrictPartialOrder(
    nodes=[order_validate, route_optimize, drone_assign, preflight_check, load_package, flight_launch, traffic_monitor,
           weather_assess, obstacle_avoid, battery_check, delivery_verify, biometric_scan, package_release, return_flight,
           post_flight, data_analyze, feedback_collect],
    order=[
        (order_validate, route_optimize),
        (route_optimize, drone_assign),
        (drone_assign, preflight_check),
        (preflight_check, load_package),
        (load_package, flight_launch),
        (flight_launch, traffic_monitor),
        (traffic_monitor, weather_assess),
        (weather_assess, obstacle_avoid),
        (obstacle_avoid, battery_check),
        (battery_check, delivery_verify),
        (delivery_verify, biometric_scan),
        (biometric_scan, package_release),
        (package_release, return_flight),
        (return_flight, post_flight),
        (post_flight, data_analyze),
        (data_analyze, feedback_collect)
    ]
)

print(root)