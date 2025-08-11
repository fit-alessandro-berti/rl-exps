import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
RegulatoryCheck = Transition(label='Regulatory Check')
PathDesign = Transition(label='Path Design')
WeatherSync = Transition(label='Weather Sync')
TrafficAlign = Transition(label='Traffic Align')
PackageSecure = Transition(label='Package Secure')
CustomerAlert = Transition(label='Customer Alert')
DroneAssemble = Transition(label='Drone Assemble')
FlightTest = Transition(label='Flight Test')
DataMonitor = Transition(label='Data Monitor')
SafetyAudit = Transition(label='Safety Audit')
EmergencyPlan = Transition(label='Emergency Plan')
MaintenancePlan = Transition(label='Maintenance Plan')
BatteryCycle = Transition(label='Battery Cycle')
RouteUpdate = Transition(label='Route Update')
PerformanceReview = Transition(label='Performance Review')
ImpactStudy = Transition(label='Impact Study')
ComplianceReview = Transition(label='Compliance Review')

# Define silent transitions
skip = SilentTransition()

# Define the loop for regulatory check
loop_regulatory = OperatorPOWL(operator=Operator.LOOP, children=[RegulatoryCheck])

# Define the XOR for drone flight test and battery cycle
xor_flight_test_battery = OperatorPOWL(operator=Operator.XOR, children=[FlightTest, BatteryCycle])

# Define the loop for drone assemble and flight test
loop_drone_assemble_flight_test = OperatorPOWL(operator=Operator.LOOP, children=[DroneAssemble, xor_flight_test_battery])

# Define the loop for path design and traffic align
loop_path_design_traffic = OperatorPOWL(operator=Operator.LOOP, children=[PathDesign, TrafficAlign])

# Define the loop for package secure and customer alert
loop_package_secure_customer_alert = OperatorPOWL(operator=Operator.LOOP, children=[PackageSecure, CustomerAlert])

# Define the loop for data monitor and safety audit
loop_data_monitor_safety_audit = OperatorPOWL(operator=Operator.LOOP, children=[DataMonitor, SafetyAudit])

# Define the loop for emergency plan and maintenance plan
loop_emergency_plan_maintenance_plan = OperatorPOWL(operator=Operator.LOOP, children=[EmergencyPlan, MaintenancePlan])

# Define the loop for route update and performance review
loop_route_update_performance_review = OperatorPOWL(operator=Operator.LOOP, children=[RouteUpdate, PerformanceReview])

# Define the loop for impact study and compliance review
loop_impact_study_compliance_review = OperatorPOWL(operator=Operator.LOOP, children=[ImpactStudy, ComplianceReview])

# Define the XOR for loop regulatory and loop drone assemble flight test
xor_loop_regulatory_loop_drone_assemble_flight_test = OperatorPOWL(operator=Operator.XOR, children=[loop_regulatory, loop_drone_assemble_flight_test])

# Define the XOR for loop path design traffic and loop package secure customer alert
xor_loop_path_design_traffic_loop_package_secure_customer_alert = OperatorPOWL(operator=Operator.XOR, children=[loop_path_design_traffic, loop_package_secure_customer_alert])

# Define the XOR for loop data monitor safety audit and loop emergency plan maintenance plan
xor_loop_data_monitor_safety_audit_loop_emergency_plan_maintenance_plan = OperatorPOWL(operator=Operator.XOR, children=[loop_data_monitor_safety_audit, loop_emergency_plan_maintenance_plan])

# Define the XOR for loop route update performance review and loop impact study compliance review
xor_loop_route_update_performance_review_loop_impact_study_compliance_review = OperatorPOWL(operator=Operator.XOR, children=[loop_route_update_performance_review, loop_impact_study_compliance_review])

# Define the root POWL model
root = StrictPartialOrder(nodes=[xor_loop_regulatory_loop_drone_assemble_flight_test, xor_loop_path_design_traffic_loop_package_secure_customer_alert, xor_loop_data_monitor_safety_audit_loop_emergency_plan_maintenance_plan, xor_loop_route_update_performance_review_loop_impact_study_compliance_review])
root.order.add_edge(xor_loop_regulatory_loop_drone_assemble_flight_test, xor_loop_path_design_traffic_loop_package_secure_customer_alert)
root.order.add_edge(xor_loop_path_design_traffic_loop_package_secure_customer_alert, xor_loop_data_monitor_safety_audit_loop_emergency_plan_maintenance_plan)
root.order.add_edge(xor_loop_data_monitor_safety_audit_loop_emergency_plan_maintenance_plan, xor_loop_route_update_performance_review_loop_impact_study_compliance_review)

# Print the root POWL model
print(root)