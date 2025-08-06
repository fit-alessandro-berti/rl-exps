import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
provenance_check = Transition(label='Provenance Check')
material_scan = Transition(label='Material Scan')
context_review = Transition(label='Context Review')
expert_consult = Transition(label='Expert Consult')
image_capture = Transition(label='Image Capture')
condition_test = Transition(label='Condition Test')
forger_risk = Transition(label='Forgery Risk')
registry_crosscheck = Transition(label='Registry Crosscheck')
legal_verify = Transition(label='Legal Verify')
ethics_review = Transition(label='Ethics Review')
report_draft = Transition(label='Report Draft')
certificate_issue = Transition(label='Certificate Issue')
digital_archive = Transition(label='Digital Archive')
transfer_setup = Transition(label='Transfer Setup')
final_approval = Transition(label='Final Approval')

# Define silent transitions
skip = SilentTransition()

# Define operators
xor = OperatorPOWL(operator=Operator.XOR, children=[forger_risk, skip])
loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, material_scan, context_review, expert_consult, image_capture, condition_test])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, registry_crosscheck, ethics_review])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[report_draft, certificate_issue])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[digital_archive, transfer_setup])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[final_approval, skip])

# Define root
root = StrictPartialOrder(nodes=[loop, xor, xor2, xor3, xor4, xor5])
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)

# Print the POWL model
print(root)