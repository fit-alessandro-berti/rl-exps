import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the silent transitions
skip1 = SilentTransition()
skip2 = SilentTransition()
skip3 = SilentTransition()

# Define the loops and exclusive choices
site_survey_loop = OperatorPOWL(operator=Operator.LOOP, children=[site_survey])
fleet_design_loop = OperatorPOWL(operator=Operator.LOOP, children=[fleet_design])
permit_request_loop = OperatorPOWL(operator=Operator.LOOP, children=[permit_request])
regulation_review_loop = OperatorPOWL(operator=Operator.LOOP, children=[regulation_review])
stakeholder_meet_loop = OperatorPOWL(operator=Operator.LOOP, children=[stakeholder_meet])
route_mapping_loop = OperatorPOWL(operator=Operator.LOOP, children=[route_mapping])
traffic_sync_loop = OperatorPOWL(operator=Operator.LOOP, children=[traffic_sync])
drone_assembly_loop = OperatorPOWL(operator=Operator.LOOP, children=[drone_assembly])
software_setup_loop = OperatorPOWL(operator=Operator.LOOP, children=[software_setup])
test_flight_loop = OperatorPOWL(operator=Operator.LOOP, children=[test_flight])
data_integration_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_integration])
compliance_audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[compliance_audit])
emergency_plan_loop = OperatorPOWL(operator=Operator.LOOP, children=[emergency_plan])
launch_prep_loop = OperatorPOWL(operator=Operator.LOOP, children=[launch_prep])
feedback_loop_loop = OperatorPOWL(operator=Operator.LOOP, children=[feedback_loop])
performance_tune_loop = OperatorPOWL(operator=Operator.LOOP, children=[performance_tune])
scale_strategy_loop = OperatorPOWL(operator=Operator.LOOP, children=[scale_strategy])

# Define the exclusive choices
permit_request_choice = OperatorPOWL(operator=Operator.XOR, children=[permit_request_loop, skip1])
regulation_review_choice = OperatorPOWL(operator=Operator.XOR, children=[regulation_review_loop, skip2])
stakeholder_meet_choice = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_meet_loop, skip3])
route_mapping_choice = OperatorPOWL(operator=Operator.XOR, children=[route_mapping_loop, skip1])
traffic_sync_choice = OperatorPOWL(operator=Operator.XOR, children=[traffic_sync_loop, skip2])
drone_assembly_choice = OperatorPOWL(operator=Operator.XOR, children=[drone_assembly_loop, skip3])
software_setup_choice = OperatorPOWL(operator=Operator.XOR, children=[software_setup_loop, skip1])
test_flight_choice = OperatorPOWL(operator=Operator.XOR, children=[test_flight_loop, skip2])
data_integration_choice = OperatorPOWL(operator=Operator.XOR, children=[data_integration_loop, skip3])
compliance_audit_choice = OperatorPOWL(operator=Operator.XOR, children=[compliance_audit_loop, skip1])
emergency_plan_choice = OperatorPOWL(operator=Operator.XOR, children=[emergency_plan_loop, skip2])
launch_prep_choice = OperatorPOWL(operator=Operator.XOR, children=[launch_prep_loop, skip3])
feedback_loop_choice = OperatorPOWL(operator=Operator.XOR, children=[feedback_loop_loop, skip1])
performance_tune_choice = OperatorPOWL(operator=Operator.XOR, children=[performance_tune_loop, skip2])
scale_strategy_choice = OperatorPOWL(operator=Operator.XOR, children=[scale_strategy_loop, skip3])

# Define the root node
root = StrictPartialOrder(nodes=[
    site_survey_loop,
    fleet_design_loop,
    permit_request_choice,
    regulation_review_choice,
    stakeholder_meet_choice,
    route_mapping_choice,
    traffic_sync_choice,
    drone_assembly_choice,
    software_setup_choice,
    test_flight_choice,
    data_integration_choice,
    compliance_audit_choice,
    emergency_plan_choice,
    launch_prep_choice,
    feedback_loop_choice,
    performance_tune_choice,
    scale_strategy_choice
])

# Define the dependencies between nodes
root.order.add_edge(site_survey_loop, fleet_design_loop)
root.order.add_edge(permit_request_choice, regulation_review_choice)
root.order.add_edge(regulation_review_choice, stakeholder_meet_choice)
root.order.add_edge(stakeholder_meet_choice, route_mapping_choice)
root.order.add_edge(route_mapping_choice, traffic_sync_choice)
root.order.add_edge(traffic_sync_choice, drone_assembly_choice)
root.order.add_edge(drone_assembly_choice, software_setup_choice)
root.order.add_edge(software_setup_choice, test_flight_choice)
root.order.add_edge(test_flight_choice, data_integration_choice)
root.order.add_edge(data_integration_choice, compliance_audit_choice)
root.order.add_edge(compliance_audit_choice, emergency_plan_choice)
root.order.add_edge(emergency_plan_choice, launch_prep_choice)
root.order.add_edge(launch_prep_choice, feedback_loop_choice)
root.order.add_edge(feedback_loop_choice, performance_tune_choice)
root.order.add_edge(performance_tune_choice, scale_strategy_choice)

print(root)