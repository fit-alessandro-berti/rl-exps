import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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
loop_material_analysis = OperatorPOWL(operator=Operator.LOOP, children=[material_analysis, spectroscopy_test, carbon_dating, three_d_modeling])

# Define the XOR for the data review
xor_data_review = OperatorPOWL(operator=Operator.XOR, children=[data_review, exhibition_prep])

# Define the partial order
root = StrictPartialOrder(nodes=[artifact_intake, provenance_check, archive_research, expert_interview, loop_material_analysis, xor_data_review, consensus_meeting, conservation_plan, preservation_setup, documentation])

# Define the order dependencies
root.order.add_edge(artifact_intake, provenance_check)
root.order.add_edge(provenance_check, archive_research)
root.order.add_edge(provenance_check, expert_interview)
root.order.add_edge(archive_research, loop_material_analysis)
root.order.add_edge(expert_interview, loop_material_analysis)
root.order.add_edge(loop_material_analysis, data_review)
root.order.add_edge(data_review, xor_data_review)
root.order.add_edge(xor_data_review, consensus_meeting)
root.order.add_edge(consensus_meeting, conservation_plan)
root.order.add_edge(conservation_plan, preservation_setup)
root.order.add_edge(preservation_setup, documentation)
root.order.add_edge(documentation, exhibition_prep)