import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey      = Transition(label='Site Survey')
fleet_design     = Transition(label='Fleet Design')
permit_request   = Transition(label='Permit Request')
regulation_review= Transition(label='Regulation Review')
stakeholder_meet = Transition(label='Stakeholder Meet')
drone_assembly   = Transition(label='Drone Assembly')
software_setup   = Transition(label='Software Setup')
test_flight      = Transition(label='Test Flight')
data_integration = Transition(label='Data Integration')
traffic_sync     = Transition(label='Traffic Sync')
route_mapping    = Transition(label='Route Mapping')
compliance_audit = Transition(label='Compliance Audit')
emergency_plan   = Transition(label='Emergency Plan')
launch_prep      = Transition(label='Launch Prep')
feedback_loop    = Transition(label='Feedback Loop')
performance_tune = Transition(label='Performance Tune')
scale_strategy   = Transition(label='Scale Strategy')

# Loop for continuous compliance and feedback
loop = OperatorPOWL(operator=Operator.LOOP, children=[compliance_audit, feedback_loop])

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_survey, fleet_design, permit_request, regulation_review, stakeholder_meet,
    drone_assembly, software_setup, test_flight, data_integration,
    traffic_sync, route_mapping, loop,
    emergency_plan, launch_prep, performance_tune, scale_strategy
])

# Define the control-flow dependencies
root.order.add_edge(site_survey, fleet_design)
root.order.add_edge(site_survey, permit_request)
root.order.add_edge(fleet_design, drone_assembly)
root.order.add_edge(permit_request, regulation_review)
root.order.add_edge(regulation_review, stakeholder_meet)
root.order.add_edge(stakeholder_meet, drone_assembly)
root.order.add_edge(stakeholder_meet, software_setup)
root.order.add_edge(drone_assembly, test_flight)
root.order.add_edge(software_setup, test_flight)
root.order.add_edge(test_flight, data_integration)
root.order.add_edge(data_integration, traffic_sync)
root.order.add_edge(traffic_sync, route_mapping)
root.order.add_edge(route_mapping, loop)
root.order.add_edge(loop, compliance_audit)
root.order.add_edge(loop, feedback_loop)
root.order.add_edge(compliance_audit, emergency_plan)
root.order.add_edge(compliance_audit, launch_prep)
root.order.add_edge(emergency_plan, performance_tune)
root.order.add_edge(emergency_plan, scale_strategy)
root.order.add_edge(launch_prep, performance_tune)
root.order.add_edge(launch_prep, scale_strategy)
root.order.add_edge(performance_tune, scale_strategy)