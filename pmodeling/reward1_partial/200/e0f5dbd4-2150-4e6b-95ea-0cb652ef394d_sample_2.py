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

# Define the partial order nodes
drone_design_node = OperatorPOWL(operator=Operator.PARTIAL_ORDER, children=[drone_design])
regulatory_check_node = OperatorPOWL(operator=Operator.PARTIAL_ORDER, children=[regulatory_check])
nav_system_node = OperatorPOWL(operator=Operator.PARTIAL_ORDER, children=[nav_system])
partner_setup_node = OperatorPOWL(operator=Operator.PARTIAL_ORDER, children=[partner_setup])
operator_training_node = OperatorPOWL(operator=Operator.PARTIAL_ORDER, children=[operator_training])
test_flights_node = OperatorPOWL(operator=Operator.PARTIAL_ORDER, children=[test_flights])
weather_review_node = OperatorPOWL(operator=Operator.PARTIAL_ORDER, children=[weather_review])
route_optimize_node = OperatorPOWL(operator=Operator.PARTIAL_ORDER, children=[route_optimize])
parts_logistics_node = OperatorPOWL(operator=Operator.PARTIAL_ORDER, children=[parts_logistics])
feedback_loop_node = OperatorPOWL(operator=Operator.PARTIAL_ORDER, children=[feedback_loop])
risk_assess_node = OperatorPOWL(operator=Operator.PARTIAL_ORDER, children=[risk_assess])
emergency_plan_node = OperatorPOWL(operator=Operator.PARTIAL_ORDER, children=[emergency_plan])
compliance_audit_node = OperatorPOWL(operator=Operator.PARTIAL_ORDER, children=[compliance_audit])
data_sync_node = OperatorPOWL(operator=Operator.PARTIAL_ORDER, children=[data_sync])
service_launch_node = OperatorPOWL(operator=Operator.PARTIAL_ORDER, children=[service_launch])

# Define the dependencies
root = StrictPartialOrder(nodes=[drone_design_node, regulatory_check_node, nav_system_node, partner_setup_node, operator_training_node, test_flights_node, weather_review_node, route_optimize_node, parts_logistics_node, feedback_loop_node, risk_assess_node, emergency_plan_node, compliance_audit_node, data_sync_node, service_launch_node])

# Add dependencies between nodes
root.order.add_edge(drone_design_node, regulatory_check_node)
root.order.add_edge(regulatory_check_node, nav_system_node)
root.order.add_edge(nav_system_node, partner_setup_node)
root.order.add_edge(partner_setup_node, operator_training_node)
root.order.add_edge(operator_training_node, test_flights_node)
root.order.add_edge(test_flights_node, weather_review_node)
root.order.add_edge(weather_review_node, route_optimize_node)
root.order.add_edge(route_optimize_node, parts_logistics_node)
root.order.add_edge(parts_logistics_node, feedback_loop_node)
root.order.add_edge(feedback_loop_node, risk_assess_node)
root.order.add_edge(risk_assess_node, emergency_plan_node)
root.order.add_edge(emergency_plan_node, compliance_audit_node)
root.order.add_edge(compliance_audit_node, data_sync_node)
root.order.add_edge(data_sync_node, service_launch_node)

# Print the root model
print(root)