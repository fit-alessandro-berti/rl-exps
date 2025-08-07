import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
artifact_intake = Transition(label='Artifact Intake')
condition_check = Transition(label='Condition Check')
multi_spectral_scan = Transition(label='Multi-spectral Scan')
material_test = Transition(label='Material Test')
database_match = Transition(label='Database Match')
provenance_check = Transition(label='Provenance Check')
expert_review = Transition(label='Expert Review')
historical_query = Transition(label='Historical Query')
lab_collaboration = Transition(label='Lab Collaboration')
imaging_analysis = Transition(label='Imaging Analysis')
forgery_detection = Transition(label='Forgery Detection')
legal_drafting = Transition(label='Legal Drafting')
certification_issue = Transition(label='Certification Issue')
client_briefing = Transition(label='Client Briefing')
archival_update = Transition(label='Archival Update')

# Define the root Partial Order
root = StrictPartialOrder(nodes=[
    artifact_intake, condition_check, multi_spectral_scan, material_test,
    database_match, provenance_check, expert_review, historical_query,
    lab_collaboration, imaging_analysis, forgery_detection, legal_drafting,
    certification_issue, client_briefing, archival_update
])

# Define dependencies between activities
root.order.add_edge(artifact_intake, condition_check)
root.order.add_edge(artifact_intake, multi_spectral_scan)
root.order.add_edge(artifact_intake, material_test)
root.order.add_edge(artifact_intake, database_match)
root.order.add_edge(artifact_intake, provenance_check)
root.order.add_edge(artifact_intake, expert_review)
root.order.add_edge(artifact_intake, historical_query)
root.order.add_edge(artifact_intake, lab_collaboration)
root.order.add_edge(artifact_intake, imaging_analysis)
root.order.add_edge(artifact_intake, forgery_detection)
root.order.add_edge(artifact_intake, legal_drafting)
root.order.add_edge(artifact_intake, certification_issue)
root.order.add_edge(artifact_intake, client_briefing)
root.order.add_edge(artifact_intake, archival_update)

# Print the root Partial Order for verification
print(root)