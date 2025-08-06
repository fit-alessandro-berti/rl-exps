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

# Define the partial order
root = StrictPartialOrder(nodes=[artifact_intake, provenance_check, archive_research, expert_interview, material_analysis, spectroscopy_test, carbon_dating, digital_imaging, three_d_modeling, data_review, consensus_meeting, conservation_plan, preservation_setup, documentation, exhibition_prep])

# Define the dependencies
root.order.add_edge(artifact_intake, provenance_check)
root.order.add_edge(provenance_check, archive_research)
root.order.add_edge(provenance_check, expert_interview)
root.order.add_edge(archive_research, data_review)
root.order.add_edge(expert_interview, data_review)
root.order.add_edge(material_analysis, spectroscopy_test)
root.order.add_edge(material_analysis, carbon_dating)
root.order.add_edge(spectroscopy_test, data_review)
root.order.add_edge(carbon_dating, data_review)
root.order.add_edge(digital_imaging, data_review)
root.order.add_edge(three_d_modeling, data_review)
root.order.add_edge(data_review, consensus_meeting)
root.order.add_edge(consensus_meeting, conservation_plan)
root.order.add_edge(conservation_plan, preservation_setup)
root.order.add_edge(preservation_setup, documentation)
root.order.add_edge(documentation, exhibition_prep)

print(root)