from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define transitions
design = Transition(label='Drone Design')
regulatory = Transition(label='Regulatory Check')
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

# Define partial order
root = StrictPartialOrder(nodes=[design, regulatory, nav_system, partner_setup, operator_training, test_flights, weather_review, route_optimize, parts_logistics, feedback_loop, risk_assess, emergency_plan, compliance_audit, data_sync, service_launch])

# Define dependencies
root.order.add_edge(design, regulatory)
root.order.add_edge(regulatory, nav_system)
root.order.add_edge(nav_system, partner_setup)
root.order.add_edge(partner_setup, operator_training)
root.order.add_edge(operator_training, test_flights)
root.order.add_edge(test_flights, weather_review)
root.order.add_edge(weather_review, route_optimize)
root.order.add_edge(route_optimize, parts_logistics)
root.order.add_edge(parts_logistics, feedback_loop)
root.order.add_edge(feedback_loop, risk_assess)
root.order.add_edge(risk_assess, emergency_plan)
root.order.add_edge(emergency_plan, compliance_audit)
root.order.add_edge(compliance_audit, data_sync)
root.order.add_edge(data_sync, service_launch)

print(root)