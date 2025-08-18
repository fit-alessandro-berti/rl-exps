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

# Define silent transitions (for concurrency)
skip = SilentTransition()

# Define the POWL model
loop = OperatorPOWL(operator=Operator.LOOP, children=[material_analysis, spectroscopy_test, carbon_dating, skip])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[archive_research, expert_interview])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[digital_imaging, three_d_modeling])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[data_review, consensus_meeting])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[conservation_plan, preservation_setup])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[documentation, exhibition_prep])

root = StrictPartialOrder(nodes=[artifact_intake, provenance_check, loop, xor1, xor2, xor3, xor4, xor5])
root.order.add_edge(artifact_intake, provenance_check)
root.order.add_edge(provenance_check, loop)
root.order.add_edge(loop, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)

print(root)