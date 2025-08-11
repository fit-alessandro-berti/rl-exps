import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
initial_review = Transition(label='Initial Review')
provenance_check = Transition(label='Provenance Check')
material_scan = Transition(label='Material Scan')
chemical_test = Transition(label='Chemical Test')
imaging_capture = Transition(label='Imaging Capture')
expert_consult = Transition(label='Expert Consult')
historical_match = Transition(label='Historical Match')
forgery_detect = Transition(label='Forgery Detect')
documentation_verify = Transition(label='Documentation Verify')
cross_border_check = Transition(label='Cross-Border Check')
condition_assess = Transition(label='Condition Assess')
value_estimate = Transition(label='Value Estimate')
report_draft = Transition(label='Report Draft')
report_review = Transition(label='Report Review')
client_approval = Transition(label='Client Approval')
certification_issue = Transition(label='Certification Issue')
archive_record = Transition(label='Archive Record')

# Define silent transitions
skip = SilentTransition()

# Define loops and choices
provenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check])
material_scan_loop = OperatorPOWL(operator=Operator.LOOP, children=[material_scan])
chemical_test_loop = OperatorPOWL(operator=Operator.LOOP, children=[chemical_test])
imaging_capture_loop = OperatorPOWL(operator=Operator.LOOP, children=[imaging_capture])
expert_consult_loop = OperatorPOWL(operator=Operator.LOOP, children=[expert_consult])
historical_match_loop = OperatorPOWL(operator=Operator.LOOP, children=[historical_match])
forgery_detect_loop = OperatorPOWL(operator=Operator.LOOP, children=[forgery_detect])
documentation_verify_loop = OperatorPOWL(operator=Operator.LOOP, children=[documentation_verify])
cross_border_check_loop = OperatorPOWL(operator=Operator.LOOP, children=[cross_border_check])
condition_assess_loop = OperatorPOWL(operator=Operator.LOOP, children=[condition_assess])
value_estimate_loop = OperatorPOWL(operator=Operator.LOOP, children=[value_estimate])
report_draft_loop = OperatorPOWL(operator=Operator.LOOP, children=[report_draft])
report_review_loop = OperatorPOWL(operator=Operator.LOOP, children=[report_review])
client_approval_loop = OperatorPOWL(operator=Operator.LOOP, children=[client_approval])
certification_issue_loop = OperatorPOWL(operator=Operator.LOOP, children=[certification_issue])
archive_record_loop = OperatorPOWL(operator=Operator.LOOP, children=[archive_record])

xor = OperatorPOWL(operator=Operator.XOR, children=[initial_review, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[value_estimate, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[report_review, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[client_approval, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[certification_issue, skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[archive_record, skip])

# Create the root POWL model
root = StrictPartialOrder(nodes=[provenance_loop, material_scan_loop, chemical_test_loop, imaging_capture_loop,
                                 expert_consult_loop, historical_match_loop, forgery_detect_loop,
                                 documentation_verify_loop, cross_border_check_loop, condition_assess_loop,
                                 value_estimate_loop, report_draft_loop, report_review_loop, client_approval_loop,
                                 certification_issue_loop, archive_record_loop, xor, xor2, xor3, xor4, xor5, xor6])
root.order.add_edge(provenance_loop, material_scan_loop)
root.order.add_edge(material_scan_loop, chemical_test_loop)
root.order.add_edge(chemical_test_loop, imaging_capture_loop)
root.order.add_edge(imaging_capture_loop, expert_consult_loop)
root.order.add_edge(expert_consult_loop, historical_match_loop)
root.order.add_edge(historical_match_loop, forgery_detect_loop)
root.order.add_edge(forgery_detect_loop, documentation_verify_loop)
root.order.add_edge(documentation_verify_loop, cross_border_check_loop)
root.order.add_edge(cross_border_check_loop, condition_assess_loop)
root.order.add_edge(condition_assess_loop, value_estimate_loop)
root.order.add_edge(value_estimate_loop, report_draft_loop)
root.order.add_edge(report_draft_loop, report_review_loop)
root.order.add_edge(report_review_loop, client_approval_loop)
root.order.add_edge(client_approval_loop, certification_issue_loop)
root.order.add_edge(certification_issue_loop, archive_record_loop)
root.order.add_edge(archive_record_loop, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)