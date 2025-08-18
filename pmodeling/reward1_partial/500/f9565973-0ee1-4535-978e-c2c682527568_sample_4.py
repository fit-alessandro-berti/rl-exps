from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) in the POWL model
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

# Define the partial order graph
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

# Define the dependencies between activities
root.order.add_edge(artifact_intake, initial_survey)
root.order.add_edge(initial_survey, material_test)
root.order.add_edge(material_test, historical_check)
root.order.add_edge(historical_check, registry_search)
root.order.add_edge(registry_search, owner_interview)
root.order.add_edge(owner_interview, condition_report)
root.order.add_edge(condition_report, forgery_scan)
root.order.add_edge(forgery_scan, digital_tagging)
root.order.add_edge(digital_tagging, ledger_entry)
root.order.add_edge(ledger_entry, expert_review)
root.order.add_edge(expert_review, legal_verify)
root.order.add_edge(legal_verify, provenance_draft)
root.order.add_edge(provenance_draft, client_approval)
root.order.add_edge(client_approval, final_certificate)
root.order.add_edge(final_certificate, archive_storage)

# Print the root to verify the model
print(root)