import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

artifact_intake_loop = OperatorPOWL(operator=Operator.LOOP, children=[artifact_intake, initial_survey, material_test, historical_check, registry_search, owner_interview, condition_report, forgery_scan, digital_tagging, ledger_entry])
artifact_intake_loop.order.add_edge(artifact_intake, initial_survey)
artifact_intake_loop.order.add_edge(initial_survey, material_test)
artifact_intake_loop.order.add_edge(material_test, historical_check)
artifact_intake_loop.order.add_edge(historical_check, registry_search)
artifact_intake_loop.order.add_edge(registry_search, owner_interview)
artifact_intake_loop.order.add_edge(owner_interview, condition_report)
artifact_intake_loop.order.add_edge(condition_report, forgery_scan)
artifact_intake_loop.order.add_edge(forgery_scan, digital_tagging)
artifact_intake_loop.order.add_edge(digital_tagging, ledger_entry)

artifact_intake_xor = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake_loop, skip])
artifact_intake_xor.order.add_edge(artifact_intake_loop, skip)

artifact_intake_xor_loop = OperatorPOWL(operator=Operator.LOOP, children=[artifact_intake_xor])
artifact_intake_xor_loop.order.add_edge(artifact_intake_xor, skip)

expert_review_xor = OperatorPOWL(operator=Operator.XOR, children=[expert_review, skip])
expert_review_xor.order.add_edge(expert_review, skip)

legal_verify_xor = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, skip])
legal_verify_xor.order.add_edge(legal_verify, skip)

legal_verify_xor_loop = OperatorPOWL(operator=Operator.LOOP, children=[legal_verify_xor])
legal_verify_xor_loop.order.add_edge(legal_verify_xor, skip)

final_certificate_xor = OperatorPOWL(operator=Operator.XOR, children=[final_certificate, skip])
final_certificate_xor.order.add_edge(final_certificate, skip)

final_certificate_xor_loop = OperatorPOWL(operator=Operator.LOOP, children=[final_certificate_xor])
final_certificate_xor_loop.order.add_edge(final_certificate_xor, skip)

client_approval_xor = OperatorPOWL(operator=Operator.XOR, children=[client_approval, skip])
client_approval_xor.order.add_edge(client_approval, skip)

client_approval_xor_loop = OperatorPOWL(operator=Operator.LOOP, children=[client_approval_xor])
client_approval_xor_loop.order.add_edge(client_approval_xor, skip)

archive_storage_xor = OperatorPOWL(operator=Operator.XOR, children=[archive_storage, skip])
archive_storage_xor.order.add_edge(archive_storage, skip)

archive_storage_xor_loop = OperatorPOWL(operator=Operator.LOOP, children=[archive_storage_xor])
archive_storage_xor_loop.order.add_edge(archive_storage_xor, skip)

root = StrictPartialOrder(nodes=[artifact_intake_xor_loop, expert_review_xor_loop, legal_verify_xor_loop, final_certificate_xor_loop, client_approval_xor_loop, archive_storage_xor_loop])
root.order.add_edge(artifact_intake_xor_loop, expert_review_xor_loop)
root.order.add_edge(expert_review_xor_loop, legal_verify_xor_loop)
root.order.add_edge(legal_verify_xor_loop, final_certificate_xor_loop)
root.order.add_edge(final_certificate_xor_loop, client_approval_xor_loop)
root.order.add_edge(client_approval_xor_loop, archive_storage_xor_loop)