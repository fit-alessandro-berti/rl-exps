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

# Define the process structure
artifact_intake_to_initial_survey = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, initial_survey])
initial_survey_to_material_test = OperatorPOWL(operator=Operator.XOR, children=[initial_survey, material_test])
material_test_to_historical_check = OperatorPOWL(operator=Operator.XOR, children=[material_test, historical_check])
historical_check_to_registry_search = OperatorPOWL(operator=Operator.XOR, children=[historical_check, registry_search])
registry_search_to_owner_interview = OperatorPOWL(operator=Operator.XOR, children=[registry_search, owner_interview])
owner_interview_to_condition_report = OperatorPOWL(operator=Operator.XOR, children=[owner_interview, condition_report])
condition_report_to_forgery_scan = OperatorPOWL(operator=Operator.XOR, children=[condition_report, forgery_scan])
forgery_scan_to_digital_tagging = OperatorPOWL(operator=Operator.XOR, children=[forgery_scan, digital_tagging])
digital_tagging_to_ledger_entry = OperatorPOWL(operator=Operator.XOR, children=[digital_tagging, ledger_entry])
ledger_entry_to_expert_review = OperatorPOWL(operator=Operator.XOR, children=[ledger_entry, expert_review])
expert_review_to_legal_verify = OperatorPOWL(operator=Operator.XOR, children=[expert_review, legal_verify])
legal_verify_to_provenance_draft = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, provenance_draft])
provenance_draft_to_client_approval = OperatorPOWL(operator=Operator.XOR, children=[provenance_draft, client_approval])
client_approval_to_final_certificate = OperatorPOWL(operator=Operator.XOR, children=[client_approval, final_certificate])
final_certificate_to_archive_storage = OperatorPOWL(operator=Operator.XOR, children=[final_certificate, archive_storage])

# Define the root node
root = StrictPartialOrder(nodes=[artifact_intake, initial_survey, material_test, historical_check, registry_search, owner_interview, condition_report, forgery_scan, digital_tagging, ledger_entry, expert_review, legal_verify, provenance_draft, client_approval, final_certificate, archive_storage])

# Define the dependencies
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

print(root)