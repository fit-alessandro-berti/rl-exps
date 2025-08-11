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
skip = SilentTransition()

# Define the process steps
provenance_check_step = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, skip])
material_analysis_step = OperatorPOWL(operator=Operator.XOR, children=[material_analysis, skip])
consensus_step = OperatorPOWL(operator=Operator.XOR, children=[consensus_meeting, skip])

# Define the partial order
loop = OperatorPOWL(operator=Operator.LOOP, children=[artifact_intake, provenance_check_step])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[material_analysis_step, consensus_step])
root = StrictPartialOrder(nodes=[loop, loop2])

# Define the partial order edges
root.order.add_edge(loop, provenance_check_step)
root.order.add_edge(loop2, material_analysis_step)
root.order.add_edge(consensus_step, exhibition_prep)

# Print the result
print(root)