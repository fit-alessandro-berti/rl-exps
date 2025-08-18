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

# Define the control flow operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[historical_check, registry_search, owner_interview, condition_report, forgery_scan])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[ledger_entry, expert_review, legal_verify])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[provenance_draft, client_approval])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[final_certificate, archive_storage])

# Define the partial order
root = StrictPartialOrder(nodes=[artifact_intake, initial_survey, material_test, xor1, xor2, xor3, xor4])
root.order.add_edge(artifact_intake, initial_survey)
root.order.add_edge(initial_survey, material_test)
root.order.add_edge(material_test, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, final_certificate)
root.order.add_edge(xor4, archive_storage)

print(root)