import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a Transition
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

# Define the process using StrictPartialOrder and OperatorPOWL
loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[material_analysis, spectroscopy_test, carbon_dating])
loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[digital_imaging, three_d_modeling])
xor = OperatorPOWL(operator=Operator.XOR, children=[data_review, consensus_meeting])
xor_2 = OperatorPOWL(operator=Operator.XOR, children=[conservation_plan, preservation_setup])
xor_3 = OperatorPOWL(operator=Operator.XOR, children=[documentation, exhibition_prep])

root = StrictPartialOrder(nodes=[artifact_intake, provenance_check, archive_research, expert_interview, loop_1, loop_2, xor, xor_2, xor_3])
root.order.add_edge(artifact_intake, provenance_check)
root.order.add_edge(provenance_check, archive_research)
root.order.add_edge(archive_research, expert_interview)
root.order.add_edge(expert_interview, loop_1)
root.order.add_edge(loop_1, loop_2)
root.order.add_edge(loop_2, xor)
root.order.add_edge(xor, xor_2)
root.order.add_edge(xor_2, xor_3)
root.order.add_edge(xor_3, conservation_plan)
root.order.add_edge(conservation_plan, preservation_setup)
root.order.add_edge(preservation_setup, documentation)
root.order.add_edge(documentation, exhibition_prep)