import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
drone_design = Transition(label='Drone Design')
regulatory_check = Transition(label='Regulatory Check')
nav_system = Transition(label='Nav System')
partner_setup = Transition(label='Partner Setup')
operator_training = Transition(label='Operator Training')
test_flights = Transition(label='Test Flights')
weather_review = Transition(label='Weather Review')
route_optimize = Transition(label='Route Optimize')
parts_logistics = Transition(label='Parts Logistics')
feedback_loop = Transition(label='Feedback Loop')
risk_assess = Transition(label='Risk Assess')
emergency_plan = Transition(label='Emergency Plan')
compliance_audit = Transition(label='Compliance Audit')
data_sync = Transition(label='Data Sync')
service_launch = Transition(label='Service Launch')

# Define the control-flow operators
xor_1 = OperatorPOWL(operator=Operator.XOR, children=[drone_design, regulatory_check])
xor_2 = OperatorPOWL(operator=Operator.XOR, children=[nav_system, partner_setup])
xor_3 = OperatorPOWL(operator=Operator.XOR, children=[operator_training, test_flights])
xor_4 = OperatorPOWL(operator=Operator.XOR, children=[weather_review, route_optimize])
xor_5 = OperatorPOWL(operator=Operator.XOR, children=[parts_logistics, feedback_loop])
xor_6 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, emergency_plan])
xor_7 = OperatorPOWL(operator=Operator.XOR, children=[compliance_audit, data_sync])

# Define the loop for phased testing
loop_test = OperatorPOWL(operator=Operator.LOOP, children=[test_flights, operator_training])

# Define the loop for real-time monitoring
loop_monitor = OperatorPOWL(operator=Operator.LOOP, children=[emergency_plan, compliance_audit])

# Define the root POWL model
root = StrictPartialOrder(nodes=[xor_1, xor_2, xor_3, xor_4, xor_5, xor_6, xor_7, loop_test, loop_monitor])
root.order.add_edge(xor_1, xor_2)
root.order.add_edge(xor_2, xor_3)
root.order.add_edge(xor_3, xor_4)
root.order.add_edge(xor_4, xor_5)
root.order.add_edge(xor_5, xor_6)
root.order.add_edge(xor_6, xor_7)
root.order.add_edge(loop_test, xor_3)
root.order.add_edge(loop_monitor, xor_7)
root.order.add_edge(loop_monitor, loop_test)

# Save the final result in the variable 'root'
print("POWL model generated successfully.")