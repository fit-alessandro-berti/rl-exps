import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the detailed validation and documentation process
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
xor1 = OperatorPOWL(operator=Operator.XOR, children=[material_test, initial_survey])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[historical_check, registry_search])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[owner_interview, condition_report])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[forgery_scan, digital_tagging])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[ledger_entry, expert_review])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, provenance_draft])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[client_approval, final_certificate])

# Define the partial order
root = StrictPartialOrder(nodes=[artifact_intake, xor1, xor2, xor3, xor4, xor5, xor6, xor7])
root.order.add_edge(artifact_intake, xor1)
root.order.add_edge(artifact_intake, xor2)
root.order.add_edge(artifact_intake, xor3)
root.order.add_edge(artifact_intake, xor4)
root.order.add_edge(artifact_intake, xor5)
root.order.add_edge(artifact_intake, xor6)
root.order.add_edge(artifact_intake, xor7)