from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the process
provenance_check_to_material_scan = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, material_scan])
material_scan_to_context_review = OperatorPOWL(operator=Operator.XOR, children=[material_scan, context_review])
context_review_to_expert_consult = OperatorPOWL(operator=Operator.XOR, children=[context_review, expert_consult])
expert_consult_to_image_capture = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, image_capture])
image_capture_to_condition_test = OperatorPOWL(operator=Operator.XOR, children=[image_capture, condition_test])
condition_test_to_forger_risk = OperatorPOWL(operator=Operator.XOR, children=[condition_test, forger_risk])
forger_risk_to_registry_crosscheck = OperatorPOWL(operator=Operator.XOR, children=[forger_risk, registry_crosscheck])
registry_crosscheck_to_legal_verify = OperatorPOWL(operator=Operator.XOR, children=[registry_crosscheck, legal_verify])
legal_verify_to_ethics_review = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, ethics_review])
ethics_review_to_report_draft = OperatorPOWL(operator=Operator.XOR, children=[ethics_review, report_draft])
report_draft_to_certificate_issue = OperatorPOWL(operator=Operator.XOR, children=[report_draft, certificate_issue])
certificate_issue_to_digital_archive = OperatorPOWL(operator=Operator.XOR, children=[certificate_issue, digital_archive])
digital_archive_to_transfer_setup = OperatorPOWL(operator=Operator.XOR, children=[digital_archive, transfer_setup])
transfer_setup_to_final_approval = OperatorPOWL(operator=Operator.XOR, children=[transfer_setup, final_approval])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[provenance_check_to_material_scan, material_scan_to_context_review, context_review_to_expert_consult, expert_consult_to_image_capture, image_capture_to_condition_test, condition_test_to_forger_risk, forger_risk_to_registry_crosscheck, registry_crosscheck_to_legal_verify, legal_verify_to_ethics_review, ethics_review_to_report_draft, report_draft_to_certificate_issue, certificate_issue_to_digital_archive, digital_archive_to_transfer_setup, transfer_setup_to_final_approval])
root.order.add_edge(provenance_check_to_material_scan, material_scan_to_context_review)
root.order.add_edge(material_scan_to_context_review, context_review_to_expert_consult)
root.order.add_edge(context_review_to_expert_consult, expert_consult_to_image_capture)
root.order.add_edge(expert_consult_to_image_capture, image_capture_to_condition_test)
root.order.add_edge(image_capture_to_condition_test, condition_test_to_forger_risk)
root.order.add_edge(condition_test_to_forger_risk, forger_risk_to_registry_crosscheck)
root.order.add_edge(forger_risk_to_registry_crosscheck, registry_crosscheck_to_legal_verify)
root.order.add_edge(registry_crosscheck_to_legal_verify, legal_verify_to_ethics_review)
root.order.add_edge(legal_verify_to_ethics_review, ethics_review_to_report_draft)
root.order.add_edge(ethics_review_to_report_draft, report_draft_to_certificate_issue)
root.order.add_edge(report_draft_to_certificate_issue, certificate_issue_to_digital_archive)
root.order.add_edge(certificate_issue_to_digital_archive, digital_archive_to_transfer_setup)
root.order.add_edge(digital_archive_to_transfer_setup, transfer_setup_to_final_approval)

# Print the POWL model
print(root)