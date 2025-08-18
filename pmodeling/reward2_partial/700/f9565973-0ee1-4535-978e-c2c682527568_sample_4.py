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

artifact_intake_loop = OperatorPOWL(operator=Operator.LOOP, children=[artifact_intake])
initial_survey_loop = OperatorPOWL(operator=Operator.LOOP, children=[initial_survey])
material_test_loop = OperatorPOWL(operator=Operator.LOOP, children=[material_test])
historical_check_loop = OperatorPOWL(operator=Operator.LOOP, children=[historical_check])
registry_search_loop = OperatorPOWL(operator=Operator.LOOP, children=[registry_search])
owner_interview_loop = OperatorPOWL(operator=Operator.LOOP, children=[owner_interview])
condition_report_loop = OperatorPOWL(operator=Operator.LOOP, children=[condition_report])
forgery_scan_loop = OperatorPOWL(operator=Operator.LOOP, children=[forgery_scan])
digital_tagging_loop = OperatorPOWL(operator=Operator.LOOP, children=[digital_tagging])
ledger_entry_loop = OperatorPOWL(operator=Operator.LOOP, children=[ledger_entry])
expert_review_loop = OperatorPOWL(operator=Operator.LOOP, children=[expert_review])
legal_verify_loop = OperatorPOWL(operator=Operator.LOOP, children=[legal_verify])
provenance_draft_loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_draft])
client_approval_loop = OperatorPOWL(operator=Operator.LOOP, children=[client_approval])
final_certificate_loop = OperatorPOWL(operator=Operator.LOOP, children=[final_certificate])
archive_storage_loop = OperatorPOWL(operator=Operator.LOOP, children=[archive_storage])

root = StrictPartialOrder(nodes=[
    artifact_intake_loop,
    initial_survey_loop,
    material_test_loop,
    historical_check_loop,
    registry_search_loop,
    owner_interview_loop,
    condition_report_loop,
    forgery_scan_loop,
    digital_tagging_loop,
    ledger_entry_loop,
    expert_review_loop,
    legal_verify_loop,
    provenance_draft_loop,
    client_approval_loop,
    final_certificate_loop,
    archive_storage_loop
])

root.order.add_edge(artifact_intake_loop, initial_survey_loop)
root.order.add_edge(initial_survey_loop, material_test_loop)
root.order.add_edge(material_test_loop, historical_check_loop)
root.order.add_edge(historical_check_loop, registry_search_loop)
root.order.add_edge(registry_search_loop, owner_interview_loop)
root.order.add_edge(owner_interview_loop, condition_report_loop)
root.order.add_edge(condition_report_loop, forgery_scan_loop)
root.order.add_edge(forgery_scan_loop, digital_tagging_loop)
root.order.add_edge(digital_tagging_loop, ledger_entry_loop)
root.order.add_edge(ledger_entry_loop, expert_review_loop)
root.order.add_edge(expert_review_loop, legal_verify_loop)
root.order.add_edge(legal_verify_loop, provenance_draft_loop)
root.order.add_edge(provenance_draft_loop, client_approval_loop)
root.order.add_edge(client_approval_loop, final_certificate_loop)
root.order.add_edge(final_certificate_loop, archive_storage_loop)