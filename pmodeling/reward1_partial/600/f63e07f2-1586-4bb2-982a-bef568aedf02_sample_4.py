import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the loop for material analysis and data collection
material_analysis_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    spectroscopy_test,
    carbon_dating,
    digital_imaging,
    three_d_modeling
])

# Define the choice between expert interview and skip for provenance check
provenance_choice = OperatorPOWL(operator=Operator.XOR, children=[
    expert_interview,
    skip
])

# Define the partial order
root = StrictPartialOrder(nodes=[
    artifact_intake,
    provenance_check,
    archive_research,
    provenance_choice,
    material_analysis,
    material_analysis_loop,
    data_review,
    consensus_meeting,
    conservation_plan,
    preservation_setup,
    documentation,
    exhibition_prep
])

# Define the dependencies between nodes
root.order.add_edge(artifact_intake, provenance_check)
root.order.add_edge(provenance_check, provenance_choice)
root.order.add_edge(provenance_choice, material_analysis)
root.order.add_edge(material_analysis, material_analysis_loop)
root.order.add_edge(material_analysis_loop, data_review)
root.order.add_edge(data_review, consensus_meeting)
root.order.add_edge(consensus_meeting, conservation_plan)
root.order.add_edge(conservation_plan, preservation_setup)
root.order.add_edge(preservation_setup, documentation)
root.order.add_edge(documentation, exhibition_prep)

print(root)