import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL transitions
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

# Define the silent transitions
skip = SilentTransition()

# Define the POWL operators
loop_provenance = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, material_scan])
loop_image = OperatorPOWL(operator=Operator.LOOP, children=[image_capture, condition_test])
xor_forger = OperatorPOWL(operator=Operator.XOR, children=[forger_risk, skip])
xor_registry = OperatorPOWL(operator=Operator.XOR, children=[registry_crosscheck, skip])
xor_legal = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, skip])
xor_ethics = OperatorPOWL(operator=Operator.XOR, children=[ethics_review, skip])
loop_report = OperatorPOWL(operator=Operator.LOOP, children=[report_draft, certificate_issue])
loop_archive = OperatorPOWL(operator=Operator.LOOP, children=[digital_archive, transfer_setup])

# Define the root POWL model
root = StrictPartialOrder(nodes=[loop_provenance, loop_image, xor_forger, xor_registry, xor_legal, xor_ethics, loop_report, loop_archive])

# Define the partial order edges
root.order.add_edge(loop_provenance, loop_image)
root.order.add_edge(loop_image, xor_forger)
root.order.add_edge(xor_forger, xor_registry)
root.order.add_edge(xor_registry, xor_legal)
root.order.add_edge(xor_legal, xor_ethics)
root.order.add_edge(xor_ethics, loop_report)
root.order.add_edge(loop_report, loop_archive)
root.order.add_edge(loop_archive, final_approval)

print(root)