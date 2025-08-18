import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

# Define the control flow
site_survey_choice = OperatorPOWL(operator=Operator.XOR, children=[permit_request, regulation_review])
permit_request_choice = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_meet, site_survey])
stakeholder_meet_choice = OperatorPOWL(operator=Operator.XOR, children=[route_mapping, permit_request])
route_mapping_choice = OperatorPOWL(operator=Operator.XOR, children=[traffic_sync, stakeholder_meet])
traffic_sync_choice = OperatorPOWL(operator=Operator.XOR, children=[drone_assembly, route_mapping])
drone_assembly_choice = OperatorPOWL(operator=Operator.XOR, children=[software_setup, traffic_sync])
software_setup_choice = OperatorPOWL(operator=Operator.XOR, children=[test_flight, drone_assembly])
test_flight_choice = OperatorPOWL(operator=Operator.XOR, children=[data_integration, software_setup])
data_integration_choice = OperatorPOWL(operator=Operator.XOR, children=[compliance_audit, test_flight])
compliance_audit_choice = OperatorPOWL(operator=Operator.XOR, children=[emergency_plan, data_integration])
emergency_plan_choice = OperatorPOWL(operator=Operator.XOR, children=[launch_prep, compliance_audit])
launch_prep_choice = OperatorPOWL(operator=Operator.XOR, children=[feedback_loop, emergency_plan])
feedback_loop_choice = OperatorPOWL(operator=Operator.XOR, children=[performance_tune, launch_prep])
performance_tune_choice = OperatorPOWL(operator=Operator.XOR, children=[scale_strategy, feedback_loop])

# Define the partial order
root = StrictPartialOrder(nodes=[
    site_survey, permit_request, regulation_review, stakeholder_meet, route_mapping, traffic_sync, drone_assembly,
    software_setup, test_flight, data_integration, compliance_audit, emergency_plan, launch_prep, feedback_loop,
    performance_tune, scale_strategy
])
root.order.add_edge(site_survey, permit_request_choice)
root.order.add_edge(permit_request, stakeholder_meet_choice)
root.order.add_edge(stakeholder_meet, route_mapping_choice)
root.order.add_edge(route_mapping, traffic_sync_choice)
root.order.add_edge(traffic_sync, drone_assembly_choice)
root.order.add_edge(drone_assembly, software_setup_choice)
root.order.add_edge(software_setup, test_flight_choice)
root.order.add_edge(test_flight, data_integration_choice)
root.order.add_edge(data_integration, compliance_audit_choice)
root.order.add_edge(compliance_audit, emergency_plan_choice)
root.order.add_edge(emergency_plan, launch_prep_choice)
root.order.add_edge(launch_prep, feedback_loop_choice)
root.order.add_edge(feedback_loop, performance_tune_choice)
root.order.add_edge(performance_tune, scale_strategy_choice)