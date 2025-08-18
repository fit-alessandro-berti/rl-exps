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

# Define loop for test flights
loop_test_flights = OperatorPOWL(operator=Operator.LOOP, children=[test_flights])

# Define XOR for weather review and route optimize
xor_weather_review_route_optimize = OperatorPOWL(operator=Operator.XOR, children=[weather_review, route_optimize])

# Define XOR for parts logistics and feedback loop
xor_parts_logistics_feedback_loop = OperatorPOWL(operator=Operator.XOR, children=[parts_logistics, feedback_loop])

# Define XOR for risk assess and emergency plan
xor_risk_assess_emergency_plan = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, emergency_plan])

# Define XOR for compliance audit and data sync
xor_compliance_audit_data_sync = OperatorPOWL(operator=Operator.XOR, children=[compliance_audit, data_sync])

# Define XOR for service launch
xor_service_launch = OperatorPOWL(operator=Operator.XOR, children=[service_launch])

# Define root POWL model
root = StrictPartialOrder(nodes=[drone_design, regulatory_check, nav_system, partner_setup, operator_training, loop_test_flights, xor_weather_review_route_optimize, xor_parts_logistics_feedback_loop, xor_risk_assess_emergency_plan, xor_compliance_audit_data_sync, xor_service_launch])
root.order.add_edge(drone_design, regulatory_check)
root.order.add_edge(regulatory_check, nav_system)
root.order.add_edge(nav_system, partner_setup)
root.order.add_edge(partner_setup, operator_training)
root.order.add_edge(operator_training, loop_test_flights)
root.order.add_edge(loop_test_flights, xor_weather_review_route_optimize)
root.order.add_edge(xor_weather_review_route_optimize, xor_parts_logistics_feedback_loop)
root.order.add_edge(xor_parts_logistics_feedback_loop, xor_risk_assess_emergency_plan)
root.order.add_edge(xor_risk_assess_emergency_plan, xor_compliance_audit_data_sync)
root.order.add_edge(xor_compliance_audit_data_sync, xor_service_launch)