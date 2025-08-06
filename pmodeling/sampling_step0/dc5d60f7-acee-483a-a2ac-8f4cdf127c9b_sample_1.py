import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

intake_review = Transition(label='Intake Review')
condition_scan = Transition(label='Condition Scan')
material_test = Transition(label='Material Test')
style_match = Transition(label='Style Match')
provenance_log = Transition(label='Provenance Log')
forgery_risk = Transition(label='Forgery Risk')
legal_audit = Transition(label='Legal Audit')
expert_panel = Transition(label='Expert Panel')
data_crosscheck = Transition(label='Data Crosscheck')
report_draft = Transition(label='Report Draft')
blockchain_tag = Transition(label='Blockchain Tag')
certification = Transition(label='Certification')
client_feedback = Transition(label='Client Feedback')
final_approval = Transition(label='Final Approval')
release_prep = Transition(label='Release Prep')

skip = SilentTransition()

# Intake Review and Condition Scan
intake_scan_choice = OperatorPOWL(operator=Operator.XOR, children=[intake_review, condition_scan])

# Material Test and Style Match
material_test_style_choice = OperatorPOWL(operator=Operator.XOR, children=[material_test, style_match])

# Provenance Log, Forgery Risk, Legal Audit, Expert Panel, Data Crosscheck
provenance_audit_panel_choice = OperatorPOWL(operator=Operator.XOR, children=[provenance_log, forgery_risk, legal_audit, expert_panel, data_crosscheck])

# Report Draft, Blockchain Tag, Certification
report_certification_choice = OperatorPOWL(operator=Operator.XOR, children=[report_draft, blockchain_tag, certification])

# Client Feedback and Final Approval
client_feedback_approval_choice = OperatorPOWL(operator=Operator.XOR, children=[client_feedback, final_approval])

# Release Prep
release_prep_loop = OperatorPOWL(operator=Operator.LOOP, children=[release_prep])

# Intake Review and Condition Scan
intake_scan_loop = OperatorPOWL(operator=Operator.LOOP, children=[intake_scan_choice, condition_scan])

# Material Test and Style Match
material_test_style_loop = OperatorPOWL(operator=Operator.LOOP, children=[material_test_style_choice, material_test])

# Provenance Log, Forgery Risk, Legal Audit, Expert Panel, Data Crosscheck
provenance_audit_panel_loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_audit_panel_choice, provenance_log])

# Report Draft, Blockchain Tag, Certification
report_certification_loop = OperatorPOWL(operator=Operator.LOOP, children=[report_certification_choice, report_draft])

# Client Feedback and Final Approval
client_feedback_approval_loop = OperatorPOWL(operator=Operator.LOOP, children=[client_feedback_approval_choice, client_feedback])

# Intake Review and Condition Scan
intake_scan_xor = OperatorPOWL(operator=Operator.XOR, children=[intake_scan_loop, intake_scan_choice])

# Material Test and Style Match
material_test_style_xor = OperatorPOWL(operator=Operator.XOR, children=[material_test_style_loop, material_test_style_choice])

# Provenance Log, Forgery Risk, Legal Audit, Expert Panel, Data Crosscheck
provenance_audit_panel_xor = OperatorPOWL(operator=Operator.XOR, children=[provenance_audit_panel_loop, provenance_audit_panel_choice])

# Report Draft, Blockchain Tag, Certification
report_certification_xor = OperatorPOWL(operator=Operator.XOR, children=[report_certification_loop, report_certification_choice])

# Client Feedback and Final Approval
client_feedback_approval_xor = OperatorPOWL(operator=Operator.XOR, children=[client_feedback_approval_loop, client_feedback_approval_choice])

# Intake Review and Condition Scan
intake_scan_xor_loop = OperatorPOWL(operator=Operator.LOOP, children=[intake_scan_xor, intake_scan_choice])

# Material Test and Style Match
material_test_style_xor_loop = OperatorPOWL(operator=Operator.LOOP, children=[material_test_style_xor, material_test_style_choice])

# Provenance Log, Forgery Risk, Legal Audit, Expert Panel, Data Crosscheck
provenance_audit_panel_xor_loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_audit_panel_xor, provenance_audit_panel_choice])

# Report Draft, Blockchain Tag, Certification
report_certification_xor_loop = OperatorPOWL(operator=Operator.LOOP, children=[report_certification_xor, report_certification_choice])

# Client Feedback and Final Approval
client_feedback_approval_xor_loop = OperatorPOWL(operator=Operator.LOOP, children=[client_feedback_approval_xor, client_feedback_approval_choice])

# Intake Review and Condition Scan
intake_scan_xor_loop_loop = OperatorPOWL(operator=Operator.LOOP, children=[intake_scan_xor_loop, intake_scan_choice])

# Material Test and Style Match
material_test_style_xor_loop_loop = OperatorPOWL(operator=Operator.LOOP, children=[material_test_style_xor_loop, material_test_style_choice])

# Provenance Log, Forgery Risk, Legal Audit, Expert Panel, Data Crosscheck
provenance_audit_panel_xor_loop_loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_audit_panel_xor_loop, provenance_audit_panel_choice])

# Report Draft, Blockchain Tag, Certification
report_certification_xor_loop_loop = OperatorPOWL(operator=Operator.LOOP, children=[report_certification_xor_loop, report_certification_choice])

# Client Feedback and Final Approval
client_feedback_approval_xor_loop_loop = OperatorPOWL(operator=Operator.LOOP, children=[client_feedback_approval_xor_loop, client_feedback_approval_choice])

# Intake Review and Condition Scan
intake_scan_xor_loop_loop_loop = OperatorPOWL(operator=Operator.LOOP, children=[intake_scan_xor_loop_loop, intake_scan_choice])

# Material Test and Style Match
material_test_style_xor_loop_loop_loop = OperatorPOWL(operator=Operator.LOOP, children=[material_test_style_xor_loop_loop, material_test_style_choice])

# Provenance Log, Forgery Risk, Legal Audit, Expert Panel, Data Crosscheck
provenance_audit_panel_xor_loop_loop_loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_audit_panel_xor_loop_loop, provenance_audit_panel_choice])

# Report Draft, Blockchain Tag, Certification
report_certification_xor_loop_loop_loop = OperatorPOWL(operator=Operator.LOOP, children=[report_certification_xor_loop_loop, report_certification_choice])

# Client Feedback and Final Approval
client_feedback_approval_xor_loop_loop_loop = OperatorPOWL(operator=Operator.LOOP, children=[client_feedback_approval_xor_loop_loop, client_feedback_approval_choice])

root = StrictPartialOrder(nodes=[intake_scan_xor_loop_loop_loop, material_test_style_xor_loop_loop_loop, provenance_audit_panel_xor_loop_loop_loop, report_certification_xor_loop_loop_loop, client_feedback_approval_xor_loop_loop_loop, release_prep_loop])
root.order.add_edge(intake_scan_xor_loop_loop_loop, material_test_style_xor_loop_loop_loop)
root.order.add_edge(material_test_style_xor_loop_loop_loop, provenance_audit_panel_xor_loop_loop_loop)
root.order.add_edge(provenance_audit_panel_xor_loop_loop_loop, report_certification_xor_loop_loop_loop)
root.order.add_edge(report_certification_xor_loop_loop_loop, client_feedback_approval_xor_loop_loop_loop)
root.order.add_edge(client_feedback_approval_xor_loop_loop_loop, release_prep_loop)