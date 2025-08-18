import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the process
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

# Define the control flow elements
xor1 = OperatorPOWL(operator=Operator.XOR, children=[regulatory_check, nav_system])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[partner_setup, operator_training])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[test_flights, weather_review])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[route_optimize, parts_logistics])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[feedback_loop, risk_assess])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[emergency_plan, compliance_audit])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[data_sync, service_launch])

# Define the partial order
root = StrictPartialOrder(nodes=[drone_design, xor1, xor2, xor3, xor4, xor5, xor6, xor7])
root.order.add_edge(drone_design, xor1)
root.order.add_edge(drone_design, xor2)
root.order.add_edge(drone_design, xor3)
root.order.add_edge(drone_design, xor4)
root.order.add_edge(drone_design, xor5)
root.order.add_edge(drone_design, xor6)
root.order.add_edge(drone_design, xor7)

# Print the root model
print(root)