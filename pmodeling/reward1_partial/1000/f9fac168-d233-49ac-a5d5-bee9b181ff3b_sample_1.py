import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities
site_survey = Transition(label='Site Survey')
fleet_design = Transition(label='Fleet Design')
permit_request = Transition(label='Permit Request')
regulation_review = Transition(label='Regulation Review')
stakeholder_meet = Transition(label='Stakeholder Meet')
route_mapping = Transition(label='Route Mapping')
traffic_sync = Transition(label='Traffic Sync')
drone_assembly = Transition(label='Drone Assembly')
software_setup = Transition(label='Software Setup')
test_flight = Transition(label='Test Flight')
data_integration = Transition(label='Data Integration')
compliance_audit = Transition(label='Compliance Audit')
emergency_plan = Transition(label='Emergency Plan')
launch_prep = Transition(label='Launch Prep')
feedback_loop = Transition(label='Feedback Loop')
performance_tune = Transition(label='Performance Tune')
scale_strategy = Transition(label='Scale Strategy')

# Create the POWL model
root = StrictPartialOrder(nodes=[site_survey, fleet_design, permit_request, regulation_review, stakeholder_meet, route_mapping, traffic_sync, drone_assembly, software_setup, test_flight, data_integration, compliance_audit, emergency_plan, launch_prep, feedback_loop, performance_tune, scale_strategy])

# Define the dependencies between activities
root.add_edge(site_survey, fleet_design)
root.add_edge(fleet_design, permit_request)
root.add_edge(permit_request, regulation_review)
root.add_edge(regulation_review, stakeholder_meet)
root.add_edge(stakeholder_meet, route_mapping)
root.add_edge(route_mapping, traffic_sync)
root.add_edge(traffic_sync, drone_assembly)
root.add_edge(drone_assembly, software_setup)
root.add_edge(software_setup, test_flight)
root.add_edge(test_flight, data_integration)
root.add_edge(data_integration, compliance_audit)
root.add_edge(compliance_audit, emergency_plan)
root.add_edge(emergency_plan, launch_prep)
root.add_edge(launch_prep, feedback_loop)
root.add_edge(feedback_loop, performance_tune)
root.add_edge(performance_tune, scale_strategy)

# Print the POWL model
print(root)