import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the control flow operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, archive_research, expert_interview, material_analysis, spectroscopy_test, carbon_dating, digital_imaging, three_d_modeling, data_review])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[consensus_meeting, conservation_plan, preservation_setup, documentation, exhibition_prep])

# Create the POWL model
root = StrictPartialOrder(nodes=[artifact_intake, xor1, xor2])
root.order.add_edge(artifact_intake, xor1)
root.order.add_edge(xor1, xor2)

# Print the root node for verification
print(root)