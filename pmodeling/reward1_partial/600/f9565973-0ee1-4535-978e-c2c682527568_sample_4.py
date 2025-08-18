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

skip = SilentTransition()

# Define the process
initial = OperatorPOWL(operator=Operator.XOR, children=[initial_survey, skip])
survey = OperatorPOWL(operator=Operator.XOR, children=[material_test, skip])
test = OperatorPOWL(operator=Operator.XOR, children=[historical_check, skip])
history = OperatorPOWL(operator=Operator.XOR, children=[registry_search, skip])
search = OperatorPOWL(operator=Operator.XOR, children=[owner_interview, skip])
interview = OperatorPOWL(operator=Operator.XOR, children=[condition_report, skip])
condition = OperatorPOWL(operator=Operator.XOR, children=[forgery_scan, skip])
forgery = OperatorPOWL(operator=Operator.XOR, children=[digital_tagging, skip])
tagging = OperatorPOWL(operator=Operator.XOR, children=[ledger_entry, skip])
ledger = OperatorPOWL(operator=Operator.XOR, children=[expert_review, skip])
expert = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, skip])
legal = OperatorPOWL(operator=Operator.XOR, children=[provenance_draft, skip])
draft = OperatorPOWL(operator=Operator.XOR, children=[client_approval, skip])
approval = OperatorPOWL(operator=Operator.XOR, children=[final_certificate, skip])
certificate = OperatorPOWL(operator=Operator.XOR, children=[archive_storage, skip])

# Define the dependencies
root = StrictPartialOrder(nodes=[artifact_intake, initial, survey, test, history, search, interview, condition, forgery, tagging, ledger, expert, legal, draft, approval, certificate])
root.order.add_edge(artifact_intake, initial)
root.order.add_edge(initial, survey)
root.order.add_edge(survey, test)
root.order.add_edge(test, history)
root.order.add_edge(history, search)
root.order.add_edge(search, interview)
root.order.add_edge(interview, condition)
root.order.add_edge(condition, forgery)
root.order.add_edge(forgery, tagging)
root.order.add_edge(tagging, ledger)
root.order.add_edge(ledger, expert)
root.order.add_edge(expert, legal)
root.order.add_edge(legal, draft)
root.order.add_edge(draft, approval)
root.order.add_edge(approval, certificate)
root.order.add_edge(certificate, archive_storage)

# Print the root
print(root)