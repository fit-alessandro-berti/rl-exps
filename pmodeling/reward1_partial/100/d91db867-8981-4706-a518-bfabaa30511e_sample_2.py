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
skip1 = SilentTransition()
skip2 = SilentTransition()

# Define POWL model components
# Stage 1: Initial Provenance Check
stage1 = StrictPartialOrder(nodes=[provenance_check])

# Stage 2: Material Scan and Context Review
stage2 = StrictPartialOrder(nodes=[material_scan, context_review])
stage2.order.add_edge(provenance_check, stage2.nodes[0])

# Stage 3: Expert Consult and Image Capture
stage3 = StrictPartialOrder(nodes=[expert_consult, image_capture])
stage3.order.add_edge(stage2.nodes[0], stage3.nodes[0])

# Stage 4: Condition Test, Forger Risk, and Registry Crosscheck
stage4 = StrictPartialOrder(nodes=[condition_test, forger_risk, registry_crosscheck])
stage4.order.add_edge(stage3.nodes[1], stage4.nodes[0])

# Stage 5: Legal Verify, Ethics Review, and Report Draft
stage5 = StrictPartialOrder(nodes=[legal_verify, ethics_review, report_draft])
stage5.order.add_edge(stage4.nodes[1], stage5.nodes[0])

# Stage 6: Certificate Issue and Digital Archive
stage6 = StrictPartialOrder(nodes=[certificate_issue, digital_archive])
stage6.order.add_edge(stage5.nodes[2], stage6.nodes[0])

# Stage 7: Transfer Setup and Final Approval
stage7 = StrictPartialOrder(nodes=[transfer_setup, final_approval])
stage7.order.add_edge(stage6.nodes[1], stage7.nodes[0])

# Connect stages
stage1.order.add_edge(stage1.nodes[0], stage2.nodes[0])
stage2.order.add_edge(stage2.nodes[0], stage3.nodes[0])
stage3.order.add_edge(stage3.nodes[1], stage4.nodes[0])
stage4.order.add_edge(stage4.nodes[1], stage5.nodes[0])
stage5.order.add_edge(stage5.nodes[2], stage6.nodes[0])
stage6.order.add_edge(stage6.nodes[1], stage7.nodes[0])

# Define root
root = StrictPartialOrder(nodes=[stage1, stage2, stage3, stage4, stage5, stage6, stage7])
root.order.add_edge(stage1.nodes[0], stage2.nodes[0])
root.order.add_edge(stage2.nodes[0], stage3.nodes[0])
root.order.add_edge(stage3.nodes[1], stage4.nodes[0])
root.order.add_edge(stage4.nodes[1], stage5.nodes[0])
root.order.add_edge(stage5.nodes[2], stage6.nodes[0])
root.order.add_edge(stage6.nodes[1], stage7.nodes[0])