import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the control flow
xor1 = OperatorPOWL(operator=Operator.XOR, children=[regulatory_check, path_design])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[weather_sync, traffic_align])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[package_secure, customer_alert])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[drone_assemble, flight_test])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[data_monitor, safety_audit])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[emergency_plan, maintenance_plan])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[battery_cycle, route_update])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[performance_review, impact_study])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[compliance_review, None])

# Define the partial order
root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8, xor9])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)
root.order.add_edge(xor8, xor9)