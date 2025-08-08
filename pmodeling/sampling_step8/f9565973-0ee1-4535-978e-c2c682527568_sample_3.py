import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL transitions
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

# Define the POWL operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, initial_survey])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[material_test, historical_check])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[registry_search, owner_interview])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[condition_report, forgery_scan])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[digital_tagging, ledger_entry])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[expert_review, legal_verify])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[provenance_draft, client_approval])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[final_certificate, archive_storage])

# Define the POWL loop
loop = OperatorPOWL(operator=Operator.LOOP, children=[xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8])

# Define the POWL root
root = StrictPartialOrder(nodes=[loop])
root.order.add_edge(loop, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)
root.order.add_edge(xor8, loop)