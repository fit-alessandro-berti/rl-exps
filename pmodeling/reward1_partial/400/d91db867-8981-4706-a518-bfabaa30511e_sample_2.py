import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define the partial order structure
root = StrictPartialOrder(nodes=[
    provenance_check, material_scan, context_review, expert_consult,
    image_capture, condition_test, forger_risk, registry_crosscheck,
    legal_verify, ethics_review, report_draft, certificate_issue,
    digital_archive, transfer_setup, final_approval
])

# Define the dependencies between activities
root.order.add_edge(provenance_check, material_scan)
root.order.add_edge(provenance_check, context_review)
root.order.add_edge(provenance_check, expert_consult)
root.order.add_edge(material_scan, image_capture)
root.order.add_edge(material_scan, condition_test)
root.order.add_edge(context_review, image_capture)
root.order.add_edge(context_review, condition_test)
root.order.add_edge(expert_consult, image_capture)
root.order.add_edge(expert_consult, condition_test)
root.order.add_edge(image_capture, forger_risk)
root.order.add_edge(image_capture, registry_crosscheck)
root.order.add_edge(image_capture, legal_verify)
root.order.add_edge(image_capture, ethics_review)
root.order.add_edge(condition_test, forger_risk)
root.order.add_edge(condition_test, registry_crosscheck)
root.order.add_edge(condition_test, legal_verify)
root.order.add_edge(condition_test, ethics_review)
root.order.add_edge(forger_risk, report_draft)
root.order.add_edge(registry_crosscheck, report_draft)
root.order.add_edge(legal_verify, report_draft)
root.order.add_edge(ethics_review, report_draft)
root.order.add_edge(report_draft, certificate_issue)
root.order.add_edge(certificate_issue, digital_archive)
root.order.add_edge(digital_archive, transfer_setup)
root.order.add_edge(transfer_setup, final_approval)

# Print the root variable
print(root)