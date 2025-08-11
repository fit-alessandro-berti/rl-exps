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
forgery_risk = Transition(label='Forgery Risk')
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

# Define sub-processes
# Provenance Check -> Material Scan -> Context Review -> Expert Consult
provenance_to_material = OperatorPOWL(operator=Operator.XOR, children=[material_scan, skip])
context_to_expert = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, skip])
provenance_to_context = OperatorPOWL(operator=Operator.XOR, children=[context_review, skip])
provenance_to_expert = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, skip])
provenance_to_final = OperatorPOWL(operator=Operator.XOR, children=[final_approval, skip])
provenance_to_registry = OperatorPOWL(operator=Operator.XOR, children=[registry_crosscheck, skip])
provenance_to_legal = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, skip])
provenance_to_ethics = OperatorPOWL(operator=Operator.XOR, children=[ethics_review, skip])
provenance_to_report = OperatorPOWL(operator=Operator.XOR, children=[report_draft, skip])
provenance_to_certificate = OperatorPOWL(operator=Operator.XOR, children=[certificate_issue, skip])
provenance_to_archive = OperatorPOWL(operator=Operator.XOR, children=[digital_archive, skip])
provenance_to_transfer = OperatorPOWL(operator=Operator.XOR, children=[transfer_setup, skip])

# Material Scan -> Condition Test -> Forgery Risk
material_to_condition = OperatorPOWL(operator=Operator.XOR, children=[condition_test, skip])
material_to_forgery = OperatorPOWL(operator=Operator.XOR, children=[forgery_risk, skip])

# Context Review -> Registry Crosscheck -> Legal Verify
context_to_registry = OperatorPOWL(operator=Operator.XOR, children=[registry_crosscheck, skip])
context_to_legal = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, skip])

# Expert Consult -> Ethics Review -> Report Draft
expert_to_ethics = OperatorPOWL(operator=Operator.XOR, children=[ethics_review, skip])
expert_to_report = OperatorPOWL(operator=Operator.XOR, children=[report_draft, skip])

# Report Draft -> Certificate Issue -> Digital Archive
report_to_certificate = OperatorPOWL(operator=Operator.XOR, children=[certificate_issue, skip])
report_to_archive = OperatorPOWL(operator=Operator.XOR, children=[digital_archive, skip])

# Certificate Issue -> Transfer Setup -> Final Approval
certificate_to_transfer = OperatorPOWL(operator=Operator.XOR, children=[transfer_setup, skip])
certificate_to_final = OperatorPOWL(operator=Operator.XOR, children=[final_approval, skip])

# Define the main process
root = StrictPartialOrder(nodes=[
    provenance_check,
    material_scan,
    context_review,
    expert_consult,
    image_capture,
    condition_test,
    forgery_risk,
    registry_crosscheck,
    legal_verify,
    ethics_review,
    report_draft,
    certificate_issue,
    digital_archive,
    transfer_setup,
    final_approval
])

# Define the dependencies
root.order.add_edge(provenance_check, material_scan)
root.order.add_edge(material_scan, condition_test)
root.order.add_edge(condition_test, forgery_risk)
root.order.add_edge(provenance_check, context_review)
root.order.add_edge(context_review, registry_crosscheck)
root.order.add_edge(registry_crosscheck, legal_verify)
root.order.add_edge(provenance_check, expert_consult)
root.order.add_edge(expert_consult, ethics_review)
root.order.add_edge(ethics_review, report_draft)
root.order.add_edge(report_draft, certificate_issue)
root.order.add_edge(certificate_issue, transfer_setup)
root.order.add_edge(transfer_setup, final_approval)

root.order.add_edge(provenance_check, material_scan)
root.order.add_edge(material_scan, condition_test)
root.order.add_edge(condition_test, forgery_risk)
root.order.add_edge(provenance_check, context_review)
root.order.add_edge(context_review, registry_crosscheck)
root.order.add_edge(registry_crosscheck, legal_verify)
root.order.add_edge(provenance_check, expert_consult)
root.order.add_edge(expert_consult, ethics_review)
root.order.add_edge(ethics_review, report_draft)
root.order.add_edge(report_draft, certificate_issue)
root.order.add_edge(certificate_issue, transfer_setup)
root.order.add_edge(transfer_setup, final_approval)