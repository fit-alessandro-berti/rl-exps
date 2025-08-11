import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define the loop node for material test, historical check, registry search, owner interview, and condition report
loop = OperatorPOWL(operator=Operator.LOOP, children=[material_test, historical_check, registry_search, owner_interview, condition_report])

# Define the exclusive choice node for forgery scan and digital tagging
xor = OperatorPOWL(operator=Operator.XOR, children=[forgery_scan, digital_tagging])

# Define the exclusive choice node for expert review and legal verify
xor2 = OperatorPOWL(operator=Operator.XOR, children=[expert_review, legal_verify])

# Define the exclusive choice node for provenance draft and client approval
xor3 = OperatorPOWL(operator=Operator.XOR, children=[provenance_draft, client_approval])

# Define the exclusive choice node for final certificate and archive storage
xor4 = OperatorPOWL(operator=Operator.XOR, children=[final_certificate, archive_storage])

# Define the root node with all the transitions and loops
root = StrictPartialOrder(nodes=[artifact_intake, initial_survey, loop, xor, xor2, xor3, xor4])
root.order.add_edge(artifact_intake, initial_survey)
root.order.add_edge(initial_survey, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, final_certificate)
root.order.add_edge(xor4, archive_storage)

# Print the root node
print(root)