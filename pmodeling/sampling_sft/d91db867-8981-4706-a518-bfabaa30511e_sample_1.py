import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
provenance_check   = Transition(label='Provenance Check')
material_scan      = Transition(label='Material Scan')
context_review     = Transition(label='Context Review')
expert_consult     = Transition(label='Expert Consult')
image_capture      = Transition(label='Image Capture')
condition_test     = Transition(label='Condition Test')
forgery_risk       = Transition(label='Forgery Risk')
registry_crosscheck= Transition(label='Registry Crosscheck')
legal_verify       = Transition(label='Legal Verify')
ethics_review      = Transition(label='Ethics Review')
report_draft       = Transition(label='Report Draft')
certificate_issue  = Transition(label='Certificate Issue')
digital_archive    = Transition(label='Digital Archive')
transfer_setup     = Transition(label='Transfer Setup')
final_approval     = Transition(label='Final Approval')

# Define the multi-stage imaging sub-process
imaging = StrictPartialOrder(nodes=[image_capture, condition_test, forgery_risk])
imaging.order.add_edge(image_capture, condition_test)
imaging.order.add_edge(condition_test, forgery_risk)

# Define the loop for repeated Registry Crosscheck & Legal Verify
loop = OperatorPOWL(operator=Operator.LOOP, children=[registry_crosscheck, legal_verify])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    provenance_check,
    material_scan,
    context_review,
    expert_consult,
    imaging,
    ethics_review,
    report_draft,
    certificate_issue,
    digital_archive,
    transfer_setup,
    final_approval
])

# Connect the sub-processes and loop
root.order.add_edge(provenance_check, material_scan)
root.order.add_edge(material_scan, context_review)
root.order.add_edge(context_review, expert_consult)
root.order.add_edge(expert_consult, imaging)
root.order.add_edge(imaging, ethics_review)
root.order.add_edge(ethics_review, report_draft)
root.order.add_edge(report_draft, certificate_issue)
root.order.add_edge(certificate_issue, digital_archive)
root.order.add_edge(digital_archive, transfer_setup)
root.order.add_edge(transfer_setup, final_approval)

# Loop for repeated Registry Crosscheck & Legal Verify
root.order.add_edge(final_approval, loop)
root.order.add_edge(loop, final_approval)

print(root)