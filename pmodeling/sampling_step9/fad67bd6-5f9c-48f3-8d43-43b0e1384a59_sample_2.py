import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define the loop for regulatory check, path design, weather sync, traffic align, package secure, customer alert
loop = OperatorPOWL(operator=Operator.LOOP, children=[regulatory_check, path_design, weather_sync, traffic_align, package_secure, customer_alert])

# Define XOR for drone assemble, flight test, data monitor, safety audit, emergency plan, maintenance plan, battery cycle, route update, performance review, impact study, compliance review
xor = OperatorPOWL(operator=Operator.XOR, children=[drone_assemble, flight_test, data_monitor, safety_audit, emergency_plan, maintenance_plan, battery_cycle, route_update, performance_review, impact_study, compliance_review])

# Define the root POWL model
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

print(root)