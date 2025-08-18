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

# Define the loop for material analysis and 3D modeling
loop_analysis = OperatorPOWL(operator=Operator.LOOP, children=[material_analysis, three_d_modeling])

# Define the XOR for consensus meeting and exhibition prep
xor_consensus_exhibition = OperatorPOWL(operator=Operator.XOR, children=[consensus_meeting, exhibition_prep])

# Define the root POWL model
root = StrictPartialOrder(nodes=[artifact_intake, provenance_check, archive_research, expert_interview, loop_analysis, data_review, xor_consensus_exhibition])
root.order.add_edge(artifact_intake, provenance_check)
root.order.add_edge(provenance_check, archive_research)
root.order.add_edge(archive_research, expert_interview)
root.order.add_edge(expert_interview, material_analysis)
root.order.add_edge(material_analysis, loop_analysis)
root.order.add_edge(loop_analysis, data_review)
root.order.add_edge(data_review, xor_consensus_exhibition)
root.order.add_edge(xor_consensus_exhibition, exhibition_prep)