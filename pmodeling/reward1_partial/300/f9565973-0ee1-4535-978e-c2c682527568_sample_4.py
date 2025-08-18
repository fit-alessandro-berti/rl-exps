from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define transitions
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

# Define silent transitions
skip = SilentTransition()

# Define nodes and loop structure
loop_node = OperatorPOWL(operator=Operator.LOOP, children=[artifact_intake, initial_survey, material_test, historical_check, registry_search, owner_interview, condition_report, forgery_scan, digital_tagging, ledger_entry, expert_review, legal_verify, provenance_draft, client_approval, final_certificate])
loop_node.order.add_edge(artifact_intake, initial_survey)
loop_node.order.add_edge(initial_survey, material_test)
loop_node.order.add_edge(material_test, historical_check)
loop_node.order.add_edge(historical_check, registry_search)
loop_node.order.add_edge(registry_search, owner_interview)
loop_node.order.add_edge(owner_interview, condition_report)
loop_node.order.add_edge(condition_report, forgery_scan)
loop_node.order.add_edge(forgery_scan, digital_tagging)
loop_node.order.add_edge(digital_tagging, ledger_entry)
loop_node.order.add_edge(ledger_entry, expert_review)
loop_node.order.add_edge(expert_review, legal_verify)
loop_node.order.add_edge(legal_verify, provenance_draft)
loop_node.order.add_edge(provenance_draft, client_approval)
loop_node.order.add_edge(client_approval, final_certificate)
loop_node.order.add_edge(final_certificate, archive_storage)

# Define the root
root = StrictPartialOrder(nodes=[loop_node])
```