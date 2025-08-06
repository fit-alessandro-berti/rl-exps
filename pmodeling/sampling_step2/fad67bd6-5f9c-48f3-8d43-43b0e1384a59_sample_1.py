import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
regulatory_check = Transition(label='Regulatory Check')
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

# Define the partial order
root = StrictPartialOrder(nodes=[regulatory_check, path_design, weather_sync, traffic_align, package_secure, customer_alert, drone_assemble, flight_test, data_monitor, safety_audit, emergency_plan, maintenance_plan, battery_cycle, route_update, performance_review, impact_study, compliance_review])

# Define the partial order edges
root.order.add_edge(regulatory_check, path_design)
root.order.add_edge(path_design, weather_sync)
root.order.add_edge(weather_sync, traffic_align)
root.order.add_edge(traffic_align, package_secure)
root.order.add_edge(package_secure, customer_alert)
root.order.add_edge(customer_alert, drone_assemble)
root.order.add_edge(drone_assemble, flight_test)
root.order.add_edge(flight_test, data_monitor)
root.order.add_edge(data_monitor, safety_audit)
root.order.add_edge(safety_audit, emergency_plan)
root.order.add_edge(emergency_plan, maintenance_plan)
root.order.add_edge(maintenance_plan, battery_cycle)
root.order.add_edge(battery_cycle, route_update)
root.order.add_edge(route_update, performance_review)
root.order.add_edge(performance_review, impact_study)
root.order.add_edge(impact_study, compliance_review)

print(root)