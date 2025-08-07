import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    drone_design, regulatory_check, nav_system, partner_setup,
    operator_training, test_flights, weather_review,
    route_optimize, parts_logistics, feedback_loop,
    risk_assess, emergency_plan, compliance_audit, data_sync,
    service_launch
])

# Define the control‐flow dependencies
# 1. Regulatory Check must happen before Nav System
root.order.add_edge(regulatory_check, nav_system)

# 2. Nav System must happen before Partner Setup
root.order.add_edge(nav_system, partner_setup)

# 3. Operator Training must happen before Test Flights
root.order.add_edge(operator_training, test_flights)

# 4. Test Flights must happen before Weather Review
root.order.add_edge(test_flights, weather_review)

# 5. Weather Review must happen before Route Optimize
root.order.add_edge(weather_review, route_optimize)

# 6. Route Optimize must happen before Parts Logistics
root.order.add_edge(route_optimize, parts_logistics)

# 7. Parts Logistics must happen before Feedback Loop
root.order.add_edge(parts_logistics, feedback_loop)

# 8. Feedback Loop must happen before Risk Assess
root.order.add_edge(feedback_loop, risk_assess)

# 9. Risk Assess must happen before Emergency Plan
root.order.add_edge(risk_assess, emergency_plan)

# 10. Emergency Plan must happen before Compliance Audit
root.order.add_edge(emergency_plan, compliance_audit)

# 11. Compliance Audit must happen before Data Sync
root.order.add_edge(compliance_audit, data_sync)

# 12. Data Sync must happen before Service Launch
root.order.add_edge(data_sync, service_launch)