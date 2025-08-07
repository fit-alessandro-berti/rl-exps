import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
site_survey       = Transition(label='Site Survey')
fleet_design      = Transition(label='Fleet Design')
permit_request    = Transition(label='Permit Request')
regulation_review = Transition(label='Regulation Review')
stakeholder_meet  = Transition(label='Stakeholder Meet')
route_mapping     = Transition(label='Route Mapping')
traffic_sync      = Transition(label='Traffic Sync')
drone_assembly    = Transition(label='Drone Assembly')
software_setup    = Transition(label='Software Setup')
test_flight       = Transition(label='Test Flight')
data_integration  = Transition(label='Data Integration')
compliance_audit  = Transition(label='Compliance Audit')
emergency_plan    = Transition(label='Emergency Plan')
launch_prep       = Transition(label='Launch Prep')
feedback_loop     = Transition(label='Feedback Loop')
performance_tune  = Transition(label='Performance Tune')
scale_strategy    = Transition(label='Scale Strategy')

# Build the loop body: Test Flight -> Data Integration -> Compliance Audit -> Emergency Plan -> Launch Prep -> Feedback Loop -> Performance Tune
body = StrictPartialOrder(nodes=[
    test_flight,
    data_integration,
    compliance_audit,
    emergency_plan,
    launch_prep,
    feedback_loop,
    performance_tune
])
body.order.add_edge(test_flight, data_integration)
body.order.add_edge(data_integration, compliance_audit)
body.order.add_edge(compliance_audit, emergency_plan)
body.order.add_edge(emergency_plan, launch_prep)
body.order.add_edge(launch_prep, feedback_loop)
body.order.add_edge(feedback_loop, performance_tune)

# Define the loop: execute body, then either exit or execute body again
drone_loop = OperatorPOWL(operator=Operator.LOOP, children=[body, body])

# Build the full process as a strict partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    fleet_design,
    permit_request,
    regulation_review,
    stakeholder_meet,
    route_mapping,
    traffic_sync,
    drone_assembly,
    software_setup,
    drone_loop,
    scale_strategy
])

# Add the control‐flow edges
root.order.add_edge(site_survey, fleet_design)
root.order.add_edge(fleet_design, permit_request)
root.order.add_edge(permit_request, regulation_review)
root.order.add_edge(regulation_review, stakeholder_meet)
root.order.add_edge(stakeholder_meet, route_mapping)
root.order.add_edge(route_mapping, traffic_sync)
root.order.add_edge(traffic_sync, drone_assembly)
root.order.add_edge(drone_assembly, software_setup)
root.order.add_edge(software_setup, drone_loop)
root.order.add_edge(drone_loop, scale_strategy)