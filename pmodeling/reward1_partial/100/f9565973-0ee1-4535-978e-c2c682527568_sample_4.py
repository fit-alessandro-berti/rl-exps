import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions for 'skip' and 'skip2'
skip = SilentTransition()
skip2 = SilentTransition()

# Define partial order nodes
initial_survey_loop = OperatorPOWL(operator=Operator.LOOP, children=[material_test, historical_check, registry_search, owner_interview, condition_report, forgery_scan, digital_tagging, ledger_entry])
expert_review_loop = OperatorPOWL(operator=Operator.LOOP, children=[expert_review, legal_verify, provenance_draft, client_approval, final_certificate])
archive_storage_loop = OperatorPOWL(operator=Operator.LOOP, children=[archive_storage])

# Define exclusive choice nodes
expert_review_xor = OperatorPOWL(operator=Operator.XOR, children=[expert_review, legal_verify])
legal_verify_xor = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, provenance_draft])
provenance_draft_xor = OperatorPOWL(operator=Operator.XOR, children=[provenance_draft, client_approval])
client_approval_xor = OperatorPOWL(operator=Operator.XOR, children=[client_approval, final_certificate])
final_certificate_xor = OperatorPOWL(operator=Operator.XOR, children=[final_certificate, archive_storage])

# Define the root POWL model
root = StrictPartialOrder(nodes=[initial_survey_loop, expert_review_loop, archive_storage_loop, expert_review_xor, legal_verify_xor, provenance_draft_xor, client_approval_xor, final_certificate_xor])

# Add edges to the root POWL model
root.order.add_edge(initial_survey_loop, expert_review_xor)
root.order.add_edge(expert_review_xor, legal_verify_xor)
root.order.add_edge(legal_verify_xor, provenance_draft_xor)
root.order.add_edge(provenance_draft_xor, client_approval_xor)
root.order.add_edge(client_approval_xor, final_certificate_xor)
root.order.add_edge(final_certificate_xor, archive_storage_loop)

print(root)