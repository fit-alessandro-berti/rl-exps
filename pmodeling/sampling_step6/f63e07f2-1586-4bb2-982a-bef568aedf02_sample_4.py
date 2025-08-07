import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL models for each activity
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

# Define the partial order and dependencies
root = StrictPartialOrder(nodes=[
    artifact_intake,
    provenance_check,
    archive_research,
    expert_interview,
    material_analysis,
    spectroscopy_test,
    carbon_dating,
    digital_imaging,
    three_d_modeling,
    data_review,
    consensus_meeting,
    conservation_plan,
    preservation_setup,
    documentation,
    exhibition_prep
])

# Define the dependencies between activities
root.order.add_edge(artifact_intake, provenance_check)
root.order.add_edge(artifact_intake, archive_research)
root.order.add_edge(artifact_intake, expert_interview)
root.order.add_edge(artifact_intake, material_analysis)
root.order.add_edge(artifact_intake, spectroscopy_test)
root.order.add_edge(artifact_intake, carbon_dating)
root.order.add_edge(artifact_intake, digital_imaging)
root.order.add_edge(artifact_intake, three_d_modeling)
root.order.add_edge(artifact_intake, data_review)
root.order.add_edge(artifact_intake, consensus_meeting)
root.order.add_edge(artifact_intake, conservation_plan)
root.order.add_edge(artifact_intake, preservation_setup)
root.order.add_edge(artifact_intake, documentation)
root.order.add_edge(artifact_intake, exhibition_prep)

# Save the final result in the variable 'root'
print(root)