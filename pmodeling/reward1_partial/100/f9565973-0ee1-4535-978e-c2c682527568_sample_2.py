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

# Define the loop for material test
material_test_loop = OperatorPOWL(operator=Operator.LOOP, children=[material_test])

# Define the XOR for initial survey and owner interview
xor_initial_survey_owner_interview = OperatorPOWL(operator=Operator.XOR, children=[initial_survey, owner_interview])

# Define the XOR for historical check and registry search
xor_historical_check_registry_search = OperatorPOWL(operator=Operator.XOR, children=[historical_check, registry_search])

# Define the XOR for condition report and forgery scan
xor_condition_report_forgery_scan = OperatorPOWL(operator=Operator.XOR, children=[condition_report, forgery_scan])

# Define the XOR for digital tagging and ledger entry
xor_digital_tagging_ledger_entry = OperatorPOWL(operator=Operator.XOR, children=[digital_tagging, ledger_entry])

# Define the XOR for expert review and legal verify
xor_expert_review_legal_verify = OperatorPOWL(operator=Operator.XOR, children=[expert_review, legal_verify])

# Define the XOR for provenance draft and client approval
xor_provenance_draft_client_approval = OperatorPOWL(operator=Operator.XOR, children=[provenance_draft, client_approval])

# Define the XOR for final certificate and archive storage
xor_final_certificate_archive_storage = OperatorPOWL(operator=Operator.XOR, children=[final_certificate, archive_storage])

# Create the root POWL model
root = StrictPartialOrder(nodes=[
    artifact_intake,
    xor_initial_survey_owner_interview,
    xor_historical_check_registry_search,
    xor_condition_report_forgery_scan,
    xor_digital_tagging_ledger_entry,
    xor_expert_review_legal_verify,
    xor_provenance_draft_client_approval,
    xor_final_certificate_archive_storage,
    material_test_loop
])

# Add edges to the root model
root.order.add_edge(artifact_intake, xor_initial_survey_owner_interview)
root.order.add_edge(xor_initial_survey_owner_interview, xor_historical_check_registry_search)
root.order.add_edge(xor_historical_check_registry_search, xor_condition_report_forgery_scan)
root.order.add_edge(xor_condition_report_forgery_scan, xor_digital_tagging_ledger_entry)
root.order.add_edge(xor_digital_tagging_ledger_entry, xor_expert_review_legal_verify)
root.order.add_edge(xor_expert_review_legal_verify, xor_provenance_draft_client_approval)
root.order.add_edge(xor_provenance_draft_client_approval, xor_final_certificate_archive_storage)
root.order.add_edge(xor_final_certificate_archive_storage, material_test_loop)
root.order.add_edge(material_test_loop, xor_final_certificate_archive_storage)

# Print the root model
print(root)