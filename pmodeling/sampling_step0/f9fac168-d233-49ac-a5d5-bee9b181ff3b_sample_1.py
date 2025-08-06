import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the POWL operators
choice1 = OperatorPOWL(operator=Operator.XOR, children=[site_survey, permit_request])
choice2 = OperatorPOWL(operator=Operator.XOR, children=[regulation_review, stakeholder_meet])
choice3 = OperatorPOWL(operator=Operator.XOR, children=[route_mapping, traffic_sync])
choice4 = OperatorPOWL(operator=Operator.XOR, children=[drone_assembly, software_setup])
choice5 = OperatorPOWL(operator=Operator.XOR, children=[test_flight, data_integration])
choice6 = OperatorPOWL(operator=Operator.XOR, children=[compliance_audit, emergency_plan])
choice7 = OperatorPOWL(operator=Operator.XOR, children=[launch_prep, feedback_loop])
choice8 = OperatorPOWL(operator=Operator.XOR, children=[performance_tune, scale_strategy])

# Define the loop
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[choice1, choice2, choice3, choice4, choice5, choice6, choice7, choice8])

# Define the root
root = StrictPartialOrder(nodes=[loop1])
root.order.add_edge(loop1, choice1)
root.order.add_edge(choice1, choice2)
root.order.add_edge(choice2, choice3)
root.order.add_edge(choice3, choice4)
root.order.add_edge(choice4, choice5)
root.order.add_edge(choice5, choice6)
root.order.add_edge(choice6, choice7)
root.order.add_edge(choice7, choice8)
root.order.add_edge(choice8, choice1)