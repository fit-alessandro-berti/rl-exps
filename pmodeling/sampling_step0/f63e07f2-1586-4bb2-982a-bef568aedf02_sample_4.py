import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
artifact_intake = Transition(label='Artifact Intake')
provenance_check = Transition(label='Provenance Check')
archive_research = Transition(label='Archive Research')
expert_interview = Transition(label='Expert Interview')
material_analysis = Transition(label='Material Analysis')
spectroscopy_test = Transition(label='Spectroscopy Test')
carbon_dating = Transition(label='Carbon Dating')
digital_imaging = Transition(label='Digital Imaging')
three_d_modeling = Transition(label='3D Modeling')
data_review = Transition(label='Data Review')
consensus_meeting = Transition(label='Consensus Meeting')
conservation_plan = Transition(label='Conservation Plan')
preservation_setup = Transition(label='Preservation Setup')
documentation = Transition(label='Documentation')
exhibition_prep = Transition(label='Exhibition Prep')

# Define silent transitions
skip1 = SilentTransition()
skip2 = SilentTransition()

# Define POWL operators
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[archive_research, expert_interview])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[spectroscopy_test, carbon_dating])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[digital_imaging, three_d_modeling])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[data_review, skip1])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[consensus_meeting, skip2])

# Define the root POWL model
root = StrictPartialOrder(nodes=[artifact_intake, provenance_check, loop1, loop2, loop3, xor1, xor2, conservation_plan, preservation_setup, documentation, exhibition_prep])
root.order.add_edge(artifact_intake, provenance_check)
root.order.add_edge(provenance_check, loop1)
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, conservation_plan)
root.order.add_edge(conservation_plan, preservation_setup)
root.order.add_edge(preservation_setup, documentation)
root.order.add_edge(documentation, exhibition_prep)

# Print the final POWL model
print(root)