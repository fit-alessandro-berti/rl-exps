import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions (if any)

# Define operators for exclusive choices
exclusive_choice_1 = OperatorPOWL(operator=Operator.XOR, children=[regulatory_check, nav_system])
exclusive_choice_2 = OperatorPOWL(operator=Operator.XOR, children=[partner_setup, operator_training])
exclusive_choice_3 = OperatorPOWL(operator=Operator.XOR, children=[test_flights, weather_review])
exclusive_choice_4 = OperatorPOWL(operator=Operator.XOR, children=[route_optimize, parts_logistics])
exclusive_choice_5 = OperatorPOWL(operator=Operator.XOR, children=[feedback_loop, risk_assess])
exclusive_choice_6 = OperatorPOWL(operator=Operator.XOR, children=[emergency_plan, compliance_audit])
exclusive_choice_7 = OperatorPOWL(operator=Operator.XOR, children=[data_sync, service_launch])

# Define loops
loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[drone_design, exclusive_choice_1])
loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[exclusive_choice_2, exclusive_choice_3])
loop_3 = OperatorPOWL(operator=Operator.LOOP, children=[exclusive_choice_4, exclusive_choice_5])
loop_4 = OperatorPOWL(operator=Operator.LOOP, children=[exclusive_choice_6, exclusive_choice_7])

# Define root node with all children
root = StrictPartialOrder(nodes=[loop_1, loop_2, loop_3, loop_4])
root.order.add_edge(loop_1, exclusive_choice_1)
root.order.add_edge(loop_2, exclusive_choice_2)
root.order.add_edge(loop_3, exclusive_choice_3)
root.order.add_edge(loop_4, exclusive_choice_4)

print(root)