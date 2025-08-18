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

# Establish the relationships
provenance_check.children = [archive_research, expert_interview]
material_analysis.children = [spectroscopy_test, carbon_dating]
data_review.children = [three_d_modeling, digital_imaging, material_analysis]
consensus_meeting.children = [data_review, provenance_check]
conservation_plan.children = [provenance_check, material_analysis]
preservation_setup.children = [conservation_plan]
documentation.children = [preservation_setup]
exhibition_prep.children = [documentation]

# Define the POWL model
root = StrictPartialOrder(nodes=[artifact_intake, provenance_check, archive_research, expert_interview, material_analysis, spectroscopy_test, carbon_dating, digital_imaging, three_d_modeling, data_review, consensus_meeting, conservation_plan, preservation_setup, documentation, exhibition_prep])
root.order.add_edge(provenance_check, archive_research)
root.order.add_edge(provenance_check, expert_interview)
root.order.add_edge(material_analysis, spectroscopy_test)
root.order.add_edge(material_analysis, carbon_dating)
root.order.add_edge(data_review, three_d_modeling)
root.order.add_edge(data_review, digital_imaging)
root.order.add_edge(data_review, material_analysis)
root.order.add_edge(consensus_meeting, data_review)
root.order.add_edge(consensus_meeting, provenance_check)
root.order.add_edge(conservation_plan, provenance_check)
root.order.add_edge(conservation_plan, material_analysis)
root.order.add_edge(preservation_setup, conservation_plan)
root.order.add_edge(documentation, preservation_setup)
root.order.add_edge(exhibition_prep, documentation)