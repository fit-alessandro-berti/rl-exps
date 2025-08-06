import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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
skip1 = SilentTransition()
skip2 = SilentTransition()

# Define loop nodes
provenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, material_scan, context_review, expert_consult])
condition_loop = OperatorPOWL(operator=Operator.LOOP, children=[image_capture, condition_test, forger_risk, registry_crosscheck, legal_verify, ethics_review, report_draft])

# Define XOR nodes
xor1 = OperatorPOWL(operator=Operator.XOR, children=[certificate_issue, skip1])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[digital_archive, transfer_setup, final_approval])

# Define partial order
root = StrictPartialOrder(nodes=[provenance_loop, condition_loop, xor1, xor2])
root.order.add_edge(provenance_loop, condition_loop)
root.order.add_edge(condition_loop, xor1)
root.order.add_edge(condition_loop, xor2)

# Return the root node
return root