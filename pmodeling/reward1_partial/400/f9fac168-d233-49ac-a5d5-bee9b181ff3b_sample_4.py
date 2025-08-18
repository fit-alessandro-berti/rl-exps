import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities)
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

# Define operators
xor = OperatorPOWL(operator=Operator.XOR, children=[route_mapping, traffic_sync])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[compliance_audit, emergency_plan])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[software_setup, test_flight])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[drone_assembly, feedback_loop])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[performance_tune, scale_strategy])

# Define partial order
root = StrictPartialOrder(nodes=[site_survey, fleet_design, permit_request, regulation_review, stakeholder_meet, xor, xor2, xor3, xor4, xor5])
root.order.add_edge(site_survey, fleet_design)
root.order.add_edge(fleet_design, permit_request)
root.order.add_edge(permit_request, regulation_review)
root.order.add_edge(regulation_review, stakeholder_meet)
root.order.add_edge(stakeholder_meet, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)