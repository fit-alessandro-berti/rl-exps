import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the process
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

# Define the loop node for material analysis and 3D modeling
loop = OperatorPOWL(operator=Operator.LOOP, children=[material_analysis, three_d_modeling])

# Define the exclusive choice for data review and consensus meeting
xor = OperatorPOWL(operator=Operator.XOR, children=[data_review, consensus_meeting])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[artifact_intake, provenance_check, archive_research, expert_interview, loop, xor, conservation_plan, preservation_setup, documentation, exhibition_prep])

# Add edges to the POWL model
root.order.add_edge(artifact_intake, provenance_check)
root.order.add_edge(artifact_intake, archive_research)
root.order.add_edge(artifact_intake, expert_interview)
root.order.add_edge(provenance_check, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, conservation_plan)
root.order.add_edge(xor, preservation_setup)
root.order.add_edge(conservation_plan, documentation)
root.order.add_edge(preservation_setup, exhibition_prep)
root.order.add_edge(exhibition_prep, documentation)

# Save the final result in the variable 'root'