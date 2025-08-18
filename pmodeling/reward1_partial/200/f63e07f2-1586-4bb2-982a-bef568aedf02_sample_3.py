import pm4py
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

provenance_check_op = OperatorPOWL(operator=Operator.XOR, children=[archive_research, expert_interview])
material_analysis_op = OperatorPOWL(operator=Operator.XOR, children=[material_analysis, spectroscopy_test, carbon_dating])
data_review_op = OperatorPOWL(operator=Operator.XOR, children=[digital_imaging, three_d_modeling])
consensus_meeting_op = OperatorPOWL(operator=Operator.XOR, children=[data_review, skip])
conservation_plan_op = OperatorPOWL(operator=Operator.XOR, children=[conservation_plan, skip])

loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check_op, material_analysis_op, data_review_op, consensus_meeting_op])
root = StrictPartialOrder(nodes=[loop, exhibition_prep])
root.order.add_edge(loop, exhibition_prep)