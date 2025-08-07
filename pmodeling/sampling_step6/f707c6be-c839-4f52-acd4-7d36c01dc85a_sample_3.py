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

# Define the partial order
root = StrictPartialOrder(nodes=[
    artifact_intake,
    condition_check,
    multi_spectral_scan,
    material_test,
    database_match,
    provenance_check,
    expert_review,
    historical_query,
    lab_collaboration,
    imaging_analysis,
    forgery_detection,
    legal_drafting,
    certification_issue,
    client_briefing,
    archival_update
])

# Define dependencies (optional)
# In this example, all activities are concurrent, so no explicit dependencies are needed.
# If there were dependencies, they would be added here using root.order.add_edge(source, target).

# Print the root to verify
print(root)