import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

provenance_check = Transition(label='Provenance Check')
material_scan = Transition(label='Material Scan')
context_review = Transition(label='Context Review')
expert_consult = Transition(label='Expert Consult')
image_capture = Transition(label='Image Capture')
condition_test = Transition(label='Condition Test')
forger_risk = Transition(label='Forgery Risk')
registry_check = Transition(label='Registry Crosscheck')
legal_verify = Transition(label='Legal Verify')
ethics_review = Transition(label='Ethics Review')
report_draft = Transition(label='Report Draft')
certificate_issue = Transition(label='Certificate Issue')
digital_archive = Transition(label='Digital Archive')
transfer_setup = Transition(label='Transfer Setup')
final_approval = Transition(label='Final Approval')

skip = SilentTransition()

provenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, material_scan])
context_loop = OperatorPOWL(operator=Operator.LOOP, children=[context_review, expert_consult])
image_loop = OperatorPOWL(operator=Operator.LOOP, children=[image_capture, condition_test])
forger_loop = OperatorPOWL(operator=Operator.LOOP, children=[forger_risk, registry_check])
legal_loop = OperatorPOWL(operator=Operator.LOOP, children=[legal_verify, ethics_review])
report_loop = OperatorPOWL(operator=Operator.LOOP, children=[report_draft, certificate_issue])
digital_loop = OperatorPOWL(operator=Operator.LOOP, children=[digital_archive, transfer_setup])

root = StrictPartialOrder(nodes=[provenance_loop, context_loop, image_loop, forger_loop, legal_loop, report_loop, digital_loop, final_approval])
root.order.add_edge(provenance_loop, context_loop)
root.order.add_edge(context_loop, image_loop)
root.order.add_edge(image_loop, forger_loop)
root.order.add_edge(forger_loop, legal_loop)
root.order.add_edge(legal_loop, report_loop)
root.order.add_edge(report_loop, digital_loop)
root.order.add_edge(digital_loop, final_approval)

print(root)