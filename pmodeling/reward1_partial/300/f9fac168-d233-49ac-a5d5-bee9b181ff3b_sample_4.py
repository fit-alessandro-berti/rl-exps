import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

site_survey_to_fleet_design = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[site_survey, fleet_design])
fleet_design_to_permit_request = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[fleet_design, permit_request])
permit_request_to_regulation_review = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[permit_request, regulation_review])
regulation_review_to_stakeholder_meet = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[regulation_review, stakeholder_meet])
stakeholder_meet_to_route_mapping = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[stakeholder_meet, route_mapping])
route_mapping_to_traffic_sync = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[route_mapping, traffic_sync])
traffic_sync_to_drone_assembly = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[traffic_sync, drone_assembly])
drone_assembly_to_software_setup = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[drone_assembly, software_setup])
software_setup_to_test_flight = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[software_setup, test_flight])
test_flight_to_data_integration = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[test_flight, data_integration])
data_integration_to_compliance_audit = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[data_integration, compliance_audit])
compliance_audit_to_emergency_plan = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[compliance_audit, emergency_plan])
emergency_plan_to_launch_prep = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[emergency_plan, launch_prep])
launch_prep_to_feedback_loop = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[launch_prep, feedback_loop])
feedback_loop_to_performance_tune = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[feedback_loop, performance_tune])
performance_tune_to_scale_strategy = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[performance_tune, scale_strategy])

root = StrictPartialOrder(nodes=[
    site_survey_to_fleet_design,
    fleet_design_to_permit_request,
    permit_request_to_regulation_review,
    regulation_review_to_stakeholder_meet,
    stakeholder_meet_to_route_mapping,
    route_mapping_to_traffic_sync,
    traffic_sync_to_drone_assembly,
    drone_assembly_to_software_setup,
    software_setup_to_test_flight,
    test_flight_to_data_integration,
    data_integration_to_compliance_audit,
    compliance_audit_to_emergency_plan,
    emergency_plan_to_launch_prep,
    launch_prep_to_feedback_loop,
    feedback_loop_to_performance_tune,
    performance_tune_to_scale_strategy
])
root.order.add_edge(site_survey_to_fleet_design, fleet_design_to_permit_request)
root.order.add_edge(fleet_design_to_permit_request, permit_request_to_regulation_review)
root.order.add_edge(permit_request_to_regulation_review, regulation_review_to_stakeholder_meet)
root.order.add_edge(regulation_review_to_stakeholder_meet, stakeholder_meet_to_route_mapping)
root.order.add_edge(stakeholder_meet_to_route_mapping, route_mapping_to_traffic_sync)
root.order.add_edge(route_mapping_to_traffic_sync, traffic_sync_to_drone_assembly)
root.order.add_edge(traffic_sync_to_drone_assembly, drone_assembly_to_software_setup)
root.order.add_edge(drone_assembly_to_software_setup, software_setup_to_test_flight)
root.order.add_edge(software_setup_to_test_flight, test_flight_to_data_integration)
root.order.add_edge(test_flight_to_data_integration, data_integration_to_compliance_audit)
root.order.add_edge(data_integration_to_compliance_audit, compliance_audit_to_emergency_plan)
root.order.add_edge(compliance_audit_to_emergency_plan, emergency_plan_to_launch_prep)
root.order.add_edge(emergency_plan_to_launch_prep, launch_prep_to_feedback_loop)
root.order.add_edge(launch_prep_to_feedback_loop, feedback_loop_to_performance_tune)
root.order.add_edge(feedback_loop_to_performance_tune, performance_tune_to_scale_strategy)

print(root)