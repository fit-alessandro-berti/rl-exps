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

provenance_check_loop = OperatorPOWL(operator=Operator.LOOP, children=[archive_research, expert_interview])
material_analysis_loop = OperatorPOWL(operator=Operator.LOOP, children=[material_analysis, spectroscopy_test, carbon_dating])
data_review_xor = OperatorPOWL(operator=Operator.XOR, children=[digital_imaging, three_d_modeling])
consensus_meeting_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_review, consensus_meeting])
conservation_plan_loop = OperatorPOWL(operator=Operator.LOOP, children=[conservation_plan, preservation_setup])
documentation_loop = OperatorPOWL(operator=Operator.LOOP, children=[documentation, exhibition_prep])

root = StrictPartialOrder(nodes=[
    artifact_intake, 
    provenance_check_loop, 
    material_analysis_loop, 
    data_review_xor, 
    consensus_meeting_loop, 
    conservation_plan_loop, 
    documentation_loop
])

root.order.add_edge(artifact_intake, provenance_check_loop)
root.order.add_edge(provenance_check_loop, material_analysis_loop)
root.order.add_edge(material_analysis_loop, data_review_xor)
root.order.add_edge(data_review_xor, consensus_meeting_loop)
root.order.add_edge(consensus_meeting_loop, conservation_plan_loop)
root.order.add_edge(conservation_plan_loop, documentation_loop)

print(root)