from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
root = StrictPartialOrder()

# Define the transitions
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

# Define the loop for regulatory check and safety audit
loop_regulatory_safety = OperatorPOWL(operator=Operator.LOOP, children=[regulatory_check, safety_audit])

# Define the exclusive choice for flight test and battery cycle
xor_flight_battery = OperatorPOWL(operator=Operator.XOR, children=[flight_test, battery_cycle])

# Define the exclusive choice for maintenance plan and route update
xor_maintenance_route = OperatorPOWL(operator=Operator.XOR, children=[maintenance_plan, route_update])

# Define the exclusive choice for performance review and impact study
xor_performance_impact = OperatorPOWL(operator=Operator.XOR, children=[performance_review, impact_study])

# Define the exclusive choice for compliance review and emergency plan
xor_compliance_emergency = OperatorPOWL(operator=Operator.XOR, children=[compliance_review, emergency_plan])

# Define the exclusive choice for data monitor and xor_performance_impact
xor_data_monitor = OperatorPOWL(operator=Operator.XOR, children=[data_monitor, xor_performance_impact])

# Define the exclusive choice for xor_flight_battery and xor_data_monitor
xor_flight_battery_data = OperatorPOWL(operator=Operator.XOR, children=[xor_flight_battery, xor_data_monitor])

# Define the exclusive choice for xor_compliance_emergency and xor_flight_battery_data
xor_compliance_emergency_flight = OperatorPOWL(operator=Operator.XOR, children=[xor_compliance_emergency, xor_flight_battery_data])

# Add the nodes to the root
root.nodes.extend([regulatory_check, path_design, weather_sync, traffic_align, package_secure, customer_alert, drone_assemble, flight_test, data_monitor, safety_audit, emergency_plan, maintenance_plan, battery_cycle, route_update, performance_review, impact_study, compliance_review, xor_flight_battery, xor_data_monitor, xor_compliance_emergency, xor_flight_battery_data, xor_compliance_emergency_flight, loop_regulatory_safety])

# Define the dependencies
root.order.add_edge(regulatory_check, loop_regulatory_safety)
root.order.add_edge(path_design, loop_regulatory_safety)
root.order.add_edge(weather_sync, xor_flight_battery)
root.order.add_edge(traffic_align, xor_flight_battery)
root.order.add_edge(package_secure, xor_flight_battery)
root.order.add_edge(customer_alert, xor_flight_battery)
root.order.add_edge(drone_assemble, xor_flight_battery)
root.order.add_edge(flight_test, xor_flight_battery)
root.order.add_edge(data_monitor, xor_flight_battery)
root.order.add_edge(safety_audit, xor_flight_battery)
root.order.add_edge(emergency_plan, xor_flight_battery)
root.order.add_edge(maintenance_plan, xor_flight_battery)
root.order.add_edge(battery_cycle, xor_flight_battery)
root.order.add_edge(route_update, xor_flight_battery)
root.order.add_edge(performance_review, xor_flight_battery)
root.order.add_edge(impact_study, xor_flight_battery)
root.order.add_edge(compliance_review, xor_flight_battery)
root.order.add_edge(xor_flight_battery, xor_data_monitor)
root.order.add_edge(xor_flight_battery, xor_compliance_emergency)
root.order.add_edge(xor_data_monitor, xor_compliance_emergency)
root.order.add_edge(xor_compliance_emergency, xor_flight_battery_data)
root.order.add_edge(xor_compliance_emergency, xor_compliance_emergency_flight)
root.order.add_edge(xor_flight_battery_data, xor_compliance_emergency_flight)
root.order.add_edge(loop_regulatory_safety, xor_compliance_emergency_flight)

# Print the root
print(root)