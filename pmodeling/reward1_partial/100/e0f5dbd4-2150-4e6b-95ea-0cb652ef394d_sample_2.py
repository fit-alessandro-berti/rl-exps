import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define the POWL model
xor = OperatorPOWL(operator=Operator.XOR, children=[parts_logistics, compliance_audit])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[feedback_loop, emergency_plan])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[route_optimize, data_sync])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[test_flights, weather_review])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[operator_training, partner_setup])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[nav_system, regulatory_check])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[drone_design, xor6])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[xor7, xor5])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[xor4, xor3])
xor10 = OperatorPOWL(operator=Operator.XOR, children=[xor2, xor10])
xor11 = OperatorPOWL(operator=Operator.XOR, children=[xor9, xor8])
xor12 = OperatorPOWL(operator=Operator.XOR, children=[service_launch, xor11])

# Construct the partial order
root = StrictPartialOrder(nodes=[xor12])
root.order.add_edge(xor12, xor11)
root.order.add_edge(xor11, xor9)
root.order.add_edge(xor9, xor8)
root.order.add_edge(xor8, xor7)
root.order.add_edge(xor7, xor6)
root.order.add_edge(xor6, xor5)
root.order.add_edge(xor5, xor4)
root.order.add_edge(xor4, xor3)
root.order.add_edge(xor3, xor2)
root.order.add_edge(xor2, xor12)

# Print the result
print(root)