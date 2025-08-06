from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define silent transitions
skip = SilentTransition()

# Define operators
xor = OperatorPOWL(operator=Operator.XOR, children=[data_integration, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[compliance_audit, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[emergency_plan, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[performance_tune, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[scale_strategy, skip])

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[permit_request, regulation_review, stakeholder_meet, route_mapping, traffic_sync, drone_assembly, software_setup, test_flight, xor])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[feedback_loop, xor2])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[xor3])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[xor4])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[xor5])

root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, loop5)

print(root)