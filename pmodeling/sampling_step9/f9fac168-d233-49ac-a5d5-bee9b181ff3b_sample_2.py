import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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
skip = SilentTransition()

# Define the choice nodes
xor1 = OperatorPOWL(operator=Operator.XOR, children=[permit_request, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[regulation_review, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_meet, skip])

# Define the loop nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[route_mapping, traffic_sync])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[drone_assembly, software_setup, test_flight, data_integration, compliance_audit, emergency_plan, launch_prep, feedback_loop, performance_tune, scale_strategy])

# Define the root
root = StrictPartialOrder(nodes=[site_survey, fleet_design, xor1, xor2, xor3, loop1, loop2])
root.order.add_edge(site_survey, xor1)
root.order.add_edge(site_survey, xor2)
root.order.add_edge(site_survey, xor3)
root.order.add_edge(xor1, loop1)
root.order.add_edge(xor2, loop2)
root.order.add_edge(xor3, loop1)
root.order.add_edge(loop1, loop2)

# Print the root
print(root)