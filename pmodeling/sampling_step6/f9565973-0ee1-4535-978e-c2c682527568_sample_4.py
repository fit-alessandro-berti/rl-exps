import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
artifact_intake = Transition(label='Artifact Intake')
initial_survey = Transition(label='Initial Survey')
material_test = Transition(label='Material Test')
historical_check = Transition(label='Historical Check')
registry_search = Transition(label='Registry Search')
owner_interview = Transition(label='Owner Interview')
condition_report = Transition(label='Condition Report')
forgery_scan = Transition(label='Forgery Scan')
digital_tagging = Transition(label='Digital Tagging')
ledger_entry = Transition(label='Ledger Entry')
expert_review = Transition(label='Expert Review')
legal_verify = Transition(label='Legal Verify')
provenance_draft = Transition(label='Provenance Draft')
client_approval = Transition(label='Client Approval')
final_certificate = Transition(label='Final Certificate')
archive_storage = Transition(label='Archive Storage')

# Define the partial order
root = StrictPartialOrder(nodes=[
    artifact_intake,
    initial_survey,
    material_test,
    historical_check,
    registry_search,
    owner_interview,
    condition_report,
    forgery_scan,
    digital_tagging,
    ledger_entry,
    expert_review,
    legal_verify,
    provenance_draft,
    client_approval,
    final_certificate,
    archive_storage
])

# Define dependencies (optional, if needed)
# For example, if initial_survey depends on artifact_intake:
# root.order.add_edge(artifact_intake, initial_survey)

# Now, 'root' contains the POWL model for the described process.