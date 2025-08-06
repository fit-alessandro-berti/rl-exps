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

# Define silent transitions for end of tasks
end_provenance_check = SilentTransition()
end_material_scan = SilentTransition()
end_context_review = SilentTransition()
end_expert_consult = SilentTransition()
end_image_capture = SilentTransition()
end_condition_test = SilentTransition()
end_forger_risk = SilentTransition()
end_registry_crosscheck = SilentTransition()
end_legal_verify = SilentTransition()
end_ethics_review = SilentTransition()
end_report_draft = SilentTransition()
end_certificate_issue = SilentTransition()
end_transfer_setup = SilentTransition()

# Define the POWL model
root = StrictPartialOrder(nodes=[
    provenance_check, material_scan, context_review, expert_consult, image_capture, condition_test,
    forger_risk, registry_crosscheck, legal_verify, ethics_review, report_draft, certificate_issue,
    digital_archive, transfer_setup, final_approval
])

# Define the partial order of activities
root.order.add_edge(provenance_check, material_scan)
root.order.add_edge(material_scan, context_review)
root.order.add_edge(context_review, expert_consult)
root.order.add_edge(expert_consult, image_capture)
root.order.add_edge(image_capture, condition_test)
root.order.add_edge(condition_test, forger_risk)
root.order.add_edge(forger_risk, registry_crosscheck)
root.order.add_edge(registry_crosscheck, legal_verify)
root.order.add_edge(legal_verify, ethics_review)
root.order.add_edge(ethics_review, report_draft)
root.order.add_edge(report_draft, certificate_issue)
root.order.add_edge(certificate_issue, digital_archive)
root.order.add_edge(digital_archive, transfer_setup)
root.order.add_edge(transfer_setup, final_approval)

# Connect the silent transitions to the end of each activity
root.order.add_edge(provenance_check, end_provenance_check)
root.order.add_edge(material_scan, end_material_scan)
root.order.add_edge(context_review, end_context_review)
root.order.add_edge(expert_consult, end_expert_consult)
root.order.add_edge(image_capture, end_image_capture)
root.order.add_edge(condition_test, end_condition_test)
root.order.add_edge(forger_risk, end_forger_risk)
root.order.add_edge(registry_crosscheck, end_registry_crosscheck)
root.order.add_edge(legal_verify, end_legal_verify)
root.order.add_edge(ethics_review, end_ethics_review)
root.order.add_edge(report_draft, end_report_draft)
root.order.add_edge(certificate_issue, end_certificate_issue)
root.order.add_edge(digital_archive, end_transfer_setup)
root.order.add_edge(transfer_setup, final_approval)