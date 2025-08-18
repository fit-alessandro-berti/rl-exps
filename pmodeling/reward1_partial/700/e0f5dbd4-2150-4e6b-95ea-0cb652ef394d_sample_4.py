import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

# Define partial order nodes and their dependencies
partial_order_nodes = [drone_design, regulatory_check, nav_system, partner_setup, operator_training, test_flights, weather_review, route_optimize, parts_logistics, feedback_loop, risk_assess, emergency_plan, compliance_audit, data_sync, service_launch]
partial_order = StrictPartialOrder(nodes=partial_order_nodes)

# Define dependencies between nodes
partial_order.order.add_edge(drone_design, regulatory_check)
partial_order.order.add_edge(regulatory_check, nav_system)
partial_order.order.add_edge(nav_system, partner_setup)
partial_order.order.add_edge(partner_setup, operator_training)
partial_order.order.add_edge(operator_training, test_flights)
partial_order.order.add_edge(test_flights, weather_review)
partial_order.order.add_edge(weather_review, route_optimize)
partial_order.order.add_edge(route_optimize, parts_logistics)
partial_order.order.add_edge(parts_logistics, feedback_loop)
partial_order.order.add_edge(feedback_loop, risk_assess)
partial_order.order.add_edge(risk_assess, emergency_plan)
partial_order.order.add_edge(emergency_plan, compliance_audit)
partial_order.order.add_edge(compliance_audit, data_sync)
partial_order.order.add_edge(data_sync, service_launch)

root = partial_order