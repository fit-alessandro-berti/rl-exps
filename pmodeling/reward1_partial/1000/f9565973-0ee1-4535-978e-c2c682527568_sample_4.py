import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the control flow
initial_survey_children = [material_test, historical_check, registry_search, owner_interview, condition_report, forgery_scan, digital_tagging, ledger_entry]
material_test_children = [initial_survey]
historical_check_children = [initial_survey]
registry_search_children = [initial_survey]
owner_interview_children = [initial_survey]
condition_report_children = [initial_survey]
forgery_scan_children = [initial_survey]
digital_tagging_children = [initial_survey]
ledger_entry_children = [initial_survey]
expert_review_children = [legal_verify, provenance_draft]
legal_verify_children = [client_approval, final_certificate]
provenance_draft_children = [client_approval, final_certificate]
client_approval_children = [archive_storage]
final_certificate_children = [archive_storage]
archive_storage_children = []

# Create the POWL model
root = StrictPartialOrder(nodes=[artifact_intake, initial_survey, material_test, historical_check, registry_search, owner_interview, condition_report, forgery_scan, digital_tagging, ledger_entry, expert_review, legal_verify, provenance_draft, client_approval, final_certificate, archive_storage])
root.order.add_edge(artifact_intake, initial_survey)
root.order.add_edge(initial_survey, material_test)
root.order.add_edge(initial_survey, historical_check)
root.order.add_edge(initial_survey, registry_search)
root.order.add_edge(initial_survey, owner_interview)
root.order.add_edge(initial_survey, condition_report)
root.order.add_edge(initial_survey, forgery_scan)
root.order.add_edge(initial_survey, digital_tagging)
root.order.add_edge(initial_survey, ledger_entry)
root.order.add_edge(ledger_entry, expert_review)
root.order.add_edge(expert_review, legal_verify)
root.order.add_edge(expert_review, provenance_draft)
root.order.add_edge(legal_verify, client_approval)
root.order.add_edge(legal_verify, final_certificate)
root.order.add_edge(provenance_draft, client_approval)
root.order.add_edge(provenance_draft, final_certificate)
root.order.add_edge(client_approval, archive_storage)
root.order.add_edge(final_certificate, archive_storage)

print(root)