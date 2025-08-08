import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their labels
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

# Define the silent transition for skipping
skip = SilentTransition()

# Define the process flow
artifact_intake_transition = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, skip])
initial_survey_transition = OperatorPOWL(operator=Operator.XOR, children=[initial_survey, skip])
material_test_transition = OperatorPOWL(operator=Operator.XOR, children=[material_test, skip])
historical_check_transition = OperatorPOWL(operator=Operator.XOR, children=[historical_check, skip])
registry_search_transition = OperatorPOWL(operator=Operator.XOR, children=[registry_search, skip])
owner_interview_transition = OperatorPOWL(operator=Operator.XOR, children=[owner_interview, skip])
condition_report_transition = OperatorPOWL(operator=Operator.XOR, children=[condition_report, skip])
forgery_scan_transition = OperatorPOWL(operator=Operator.XOR, children=[forgery_scan, skip])
digital_tagging_transition = OperatorPOWL(operator=Operator.XOR, children=[digital_tagging, skip])
ledger_entry_transition = OperatorPOWL(operator=Operator.XOR, children=[ledger_entry, skip])
expert_review_transition = OperatorPOWL(operator=Operator.XOR, children=[expert_review, skip])
legal_verify_transition = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, skip])
provenance_draft_transition = OperatorPOWL(operator=Operator.XOR, children=[provenance_draft, skip])
client_approval_transition = OperatorPOWL(operator=Operator.XOR, children=[client_approval, skip])
final_certificate_transition = OperatorPOWL(operator=Operator.XOR, children=[final_certificate, skip])
archive_storage_transition = OperatorPOWL(operator=Operator.XOR, children=[archive_storage, skip])

# Define the partial order
root = StrictPartialOrder(nodes=[
    artifact_intake_transition,
    initial_survey_transition,
    material_test_transition,
    historical_check_transition,
    registry_search_transition,
    owner_interview_transition,
    condition_report_transition,
    forgery_scan_transition,
    digital_tagging_transition,
    ledger_entry_transition,
    expert_review_transition,
    legal_verify_transition,
    provenance_draft_transition,
    client_approval_transition,
    final_certificate_transition,
    archive_storage_transition
])

# Add the dependencies
root.order.add_edge(artifact_intake_transition, initial_survey_transition)
root.order.add_edge(initial_survey_transition, material_test_transition)
root.order.add_edge(material_test_transition, historical_check_transition)
root.order.add_edge(historical_check_transition, registry_search_transition)
root.order.add_edge(registry_search_transition, owner_interview_transition)
root.order.add_edge(owner_interview_transition, condition_report_transition)
root.order.add_edge(condition_report_transition, forgery_scan_transition)
root.order.add_edge(forgery_scan_transition, digital_tagging_transition)
root.order.add_edge(digital_tagging_transition, ledger_entry_transition)
root.order.add_edge(ledger_entry_transition, expert_review_transition)
root.order.add_edge(expert_review_transition, legal_verify_transition)
root.order.add_edge(legal_verify_transition, provenance_draft_transition)
root.order.add_edge(provenance_draft_transition, client_approval_transition)
root.order.add_edge(client_approval_transition, final_certificate_transition)
root.order.add_edge(final_certificate_transition, archive_storage_transition)

# Print the root model
print(root)