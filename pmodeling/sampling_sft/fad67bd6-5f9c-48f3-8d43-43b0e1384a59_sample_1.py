import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
reg_check = Transition(label='Regulatory Check')
path_design = Transition(label='Path Design')
weather_sync = Transition(label='Weather Sync')
traffic_align = Transition(label='Traffic Align')
package_secure = Transition(label='Package Secure')
customer_alert = Transition(label='Customer Alert')
drone_assemble = Transition(label='Drone Assemble')
flight_test = Transition(label='Flight Test')
data_monitor = Transition(label='Data Monitor')
safety_audit = Transition(label='Safety Audit')
emergency_plan = Transition(label='Emergency Plan')
maintenance_plan = Transition(label='Maintenance Plan')
battery_cycle = Transition(label='Battery Cycle')
route_update = Transition(label='Route Update')
performance_review = Transition(label='Performance Review')
impact_study = Transition(label='Impact Study')
compliance_review = Transition(label='Compliance Review')

# Build the partial order
root = StrictPartialOrder(nodes=[
    reg_check,
    path_design,
    weather_sync,
    traffic_align,
    package_secure,
    customer_alert,
    drone_assemble,
    flight_test,
    data_monitor,
    safety_audit,
    emergency_plan,
    maintenance_plan,
    battery_cycle,
    route_update,
    performance_review,
    impact_study,
    compliance_review
])

# Sequence: Regulatory Check -> Path Design -> Weather Sync -> Traffic Align
root.order.add_edge(reg_check, path_design)
root.order.add_edge(path_design, weather_sync)
root.order.add_edge(weather_sync, traffic_align)

# Parallel: Package Secure and Customer Alert
root.order.add_edge(traffic_align, package_secure)
root.order.add_edge(traffic_align, customer_alert)

# After alignment, assemble and test the drone
root.order.add_edge(package_secure, drone_assemble)
root.order.add_edge(customer_alert, drone_assemble)
root.order.add_edge(drone_assemble, flight_test)

# Monitor data and audit after flight
root.order.add_edge(flight_test, data_monitor)
root.order.add_edge(flight_test, safety_audit)

# Sequence: Emergency Plan after safety audit
root.order.add_edge(safety_audit, emergency_plan)

# After emergency, maintenance and battery cycle
root.order.add_edge(emergency_plan, maintenance_plan)
root.order.add_edge(emergency_plan, battery_cycle)

# Loop: Route Update, Performance Review, Impact Study, Compliance Review
loop_body = StrictPartialOrder(nodes=[
    route_update,
    performance_review,
    impact_study,
    compliance_review
])
loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, loop_body])

# After battery cycle, start the loop
root.order.add_edge(battery_cycle, loop)

# The loop has no exit condition, so we don't need to add an edge from loop to anywhere