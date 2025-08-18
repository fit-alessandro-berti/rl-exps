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

# Define the POWL model
root = StrictPartialOrder(nodes=[
    order_validate,
    route_optimize,
    drone_assign,
    preflight_check,
    load_package,
    flight_launch,
    traffic_monitor,
    weather_assess,
    obstacle_avoid,
    battery_check,
    delivery_verify,
    biometric_scan,
    package_release,
    return_flight,
    post_flight,
    data_analyze,
    feedback_collect
])

# Define the dependencies
root.order.add_edge(order_validate, route_optimize)
root.order.add_edge(route_optimize, drone_assign)
root.order.add_edge(drone_assign, preflight_check)
root.order.add_edge(preflight_check, load_package)
root.order.add_edge(load_package, flight_launch)
root.order.add_edge(flight_launch, traffic_monitor)
root.order.add_edge(traffic_monitor, weather_assess)
root.order.add_edge(weather_assess, obstacle_avoid)
root.order.add_edge(obstacle_avoid, battery_check)
root.order.add_edge(battery_check, delivery_verify)
root.order.add_edge(delivery_verify, biometric_scan)
root.order.add_edge(biometric_scan, package_release)
root.order.add_edge(package_release, return_flight)
root.order.add_edge(return_flight, post_flight)
root.order.add_edge(post_flight, data_analyze)
root.order.add_edge(data_analyze, feedback_collect)

# Print the root model
print(root)