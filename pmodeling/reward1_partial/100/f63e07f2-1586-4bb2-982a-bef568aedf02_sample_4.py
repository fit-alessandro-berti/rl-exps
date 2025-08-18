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
skip = SilentTransition()

# Define partial order nodes and their dependencies
loop_node = OperatorPOWL(operator=Operator.LOOP, children=[material_analysis, spectroscopy_test, carbon_dating, digital_imaging, three_d_modeling])
xor_node = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, skip])
partial_order = StrictPartialOrder(nodes=[artifact_intake, archive_research, expert_interview, loop_node, data_review, consensus_meeting, conservation_plan, preservation_setup, documentation, exhibition_prep])
partial_order.order.add_edge(artifact_intake, archive_research)
partial_order.order.add_edge(artifact_intake, expert_interview)
partial_order.order.add_edge(archive_research, provenance_check)
partial_order.order.add_edge(expert_interview, provenance_check)
partial_order.order.add_edge(provenance_check, loop_node)
partial_order.order.add_edge(loop_node, data_review)
partial_order.order.add_edge(data_review, consensus_meeting)
partial_order.order.add_edge(consensus_meeting, conservation_plan)
partial_order.order.add_edge(conservation_plan, preservation_setup)
partial_order.order.add_edge(preservation_setup, documentation)
partial_order.order.add_edge(documentation, exhibition_prep)

# Assign the final POWL model to 'root'
root = partial_order