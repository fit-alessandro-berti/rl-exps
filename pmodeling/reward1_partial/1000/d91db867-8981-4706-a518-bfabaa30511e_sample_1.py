from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the POWL model
root = StrictPartialOrder()

# Define the transitions (activities)
provenance_check = Transition(label='Provenance Check')
material_scan = Transition(label='Material Scan')
context_review = Transition(label='Context Review')
expert_consult = Transition(label='Expert Consult')
image_capture = Transition(label='Image Capture')
condition_test = Transition(label='Condition Test')
forgery_risk = Transition(label='Forgery Risk')
registry_crosscheck = Transition(label='Registry Crosscheck')
legal_verify = Transition(label='Legal Verify')
ethics_review = Transition(label='Ethics Review')
report_draft = Transition(label='Report Draft')
certificate_issue = Transition(label='Certificate Issue')
digital_archive = Transition(label='Digital Archive')
transfer_setup = Transition(label='Transfer Setup')
final_approval = Transition(label='Final Approval')

# Add the transitions to the root
root.nodes = [provenance_check, material_scan, context_review, expert_consult, image_capture, condition_test, forgery_risk, registry_crosscheck, legal_verify, ethics_review, report_draft, certificate_issue, digital_archive, transfer_setup, final_approval]

# Define the partial order
root.order = [
    (provenance_check, material_scan),
    (material_scan, context_review),
    (context_review, expert_consult),
    (expert_consult, image_capture),
    (image_capture, condition_test),
    (condition_test, forgery_risk),
    (forgery_risk, registry_crosscheck),
    (registry_crosscheck, legal_verify),
    (legal_verify, ethics_review),
    (ethics_review, report_draft),
    (report_draft, certificate_issue),
    (certificate_issue, digital_archive),
    (digital_archive, transfer_setup),
    (transfer_setup, final_approval)
]