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
registry_crosscheck = Transition(label='Registry Crosscheck')
legal_verify = Transition(label='Legal Verify')
ethics_review = Transition(label='Ethics Review')
report_draft = Transition(label='Report Draft')
certificate_issue = Transition(label='Certificate Issue')
digital_archive = Transition(label='Digital Archive')
transfer_setup = Transition(label='Transfer Setup')
final_approval = Transition(label='Final Approval')

skip = SilentTransition()

# Provenance Check -> Material Scan
# Material Scan -> Context Review
# Context Review -> Expert Consult
# Expert Consult -> Image Capture
# Image Capture -> Condition Test
# Condition Test -> Forger Risk
# Forger Risk -> Registry Crosscheck
# Registry Crosscheck -> Legal Verify
# Legal Verify -> Ethics Review
# Ethics Review -> Report Draft
# Report Draft -> Certificate Issue
# Certificate Issue -> Digital Archive
# Digital Archive -> Transfer Setup
# Transfer Setup -> Final Approval

provenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, material_scan, context_review, expert_consult, image_capture, condition_test, forger_risk, registry_crosscheck, legal_verify, ethics_review, report_draft, certificate_issue, digital_archive, transfer_setup])
xor = OperatorPOWL(operator=Operator.XOR, children=[final_approval, skip])

root = StrictPartialOrder(nodes=[provenance_loop, xor])
root.order.add_edge(provenance_loop, xor)

print(root)