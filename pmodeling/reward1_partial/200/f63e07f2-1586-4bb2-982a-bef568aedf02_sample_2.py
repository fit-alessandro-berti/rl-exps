from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

loop = OperatorPOWL(operator=Operator.LOOP, children=[artifact_intake, provenance_check, archive_research, expert_interview, material_analysis, spectroscopy_test, carbon_dating, digital_imaging, three_d_modeling])
xor = OperatorPOWL(operator=Operator.XOR, children=[data_review, consensus_meeting])
xor_2 = OperatorPOWL(operator=Operator.XOR, children=[conservation_plan, preservation_setup])
xor_3 = OperatorPOWL(operator=Operator.XOR, children=[documentation, exhibition_prep])

root = StrictPartialOrder(nodes=[loop, xor, xor_2, xor_3])
root.order.add_edge(loop, xor)
root.order.add_edge(loop, xor_2)
root.order.add_edge(loop, xor_3)
root.order.add_edge(xor, xor_2)
root.order.add_edge(xor_2, xor_3)