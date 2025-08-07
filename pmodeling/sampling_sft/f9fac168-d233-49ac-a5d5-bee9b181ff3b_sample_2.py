import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
site_survey       = Transition(label='Site Survey')
stakeholder_meet  = Transition(label='Stakeholder Meet')
permit_request    = Transition(label='Permit Request')
regulation_review = Transition(label='Regulation Review')
drone_assembly    = Transition(label='Drone Assembly')
software_setup    = Transition(label='Software Setup')
fleet_design      = Transition(label='Fleet Design')
route_mapping     = Transition(label='Route Mapping')
traffic_sync      = Transition(label='Traffic Sync')
test_flight       = Transition(label='Test Flight')
data_integration  = Transition(label='Data Integration')
compliance_audit  = Transition(label='Compliance Audit')
launch_prep       = Transition(label='Launch Prep')
performance_tune  = Transition(label='Performance Tune')
scale_strategy    = Transition(label='Scale Strategy')
emergency_plan    = Transition(label='Emergency Plan')
feedback_loop     = Transition(label='Feedback Loop')

# Define the loop for continuous performance tuning
# Body A: performance tuning
# Body B: feedback loop
loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[performance_tune, feedback_loop]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    stakeholder_meet,
    permit_request,
    regulation_review,
    drone_assembly,
    software_setup,
    fleet_design,
    route_mapping,
    traffic_sync,
    test_flight,
    data_integration,
    compliance_audit,
    launch_prep,
    scale_strategy,
    emergency_plan,
    loop
])

# Sequence of activities before the main loop
root.order.add_edge(site_survey, stakeholder_meet)
root.order.add_edge(stakeholder_meet, permit_request)
root.order.add_edge(permit_request, regulation_review)
root.order.add_edge(regulation_review, drone_assembly)
root.order.add_edge(drone_assembly, software_setup)
root.order.add_edge(software_setup, fleet_design)
root.order.add_edge(fleet_design, route_mapping)
root.order.add_edge(route_mapping, traffic_sync)
root.order.add_edge(traffic_sync, test_flight)
root.order.add_edge(test_flight, data_integration)
root.order.add_edge(data_integration, compliance_audit)
root.order.add_edge(compliance_audit, launch_prep)
root.order.add_edge(launch_prep, scale_strategy)
root.order.add_edge(scale_strategy, emergency_plan)

# The loop itself
root.order.add_edge(emergency_plan, loop)

# No further edges after the loop (the loop will continue indefinitely)