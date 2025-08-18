import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the control flow
initial_review_transition = OperatorPOWL(operator=Operator.TRANSITION, children=[provenance_check])
provenance_check_transition = OperatorPOWL(operator=Operator.TRANSITION, children=[material_scan])
material_scan_transition = OperatorPOWL(operator=Operator.TRANSITION, children=[chemical_test])
chemical_test_transition = OperatorPOWL(operator=Operator.TRANSITION, children=[imaging_capture])
imaging_capture_transition = OperatorPOWL(operator=Operator.TRANSITION, children=[expert_consult])
expert_consult_transition = OperatorPOWL(operator=Operator.TRANSITION, children=[historical_match])
historical_match_transition = OperatorPOWL(operator=Operator.TRANSITION, children=[forgery_detect])
forgery_detect_transition = OperatorPOWL(operator=Operator.TRANSITION, children=[documentation_verify])
documentation_verify_transition = OperatorPOWL(operator=Operator.TRANSITION, children=[cross_border_check])
cross_border_check_transition = OperatorPOWL(operator=Operator.TRANSITION, children=[condition_assess])
condition_assess_transition = OperatorPOWL(operator=Operator.TRANSITION, children=[value_estimate])
value_estimate_transition = OperatorPOWL(operator=Operator.TRANSITION, children=[report_draft])
report_draft_transition = OperatorPOWL(operator=Operator.TRANSITION, children=[report_review])
report_review_transition = OperatorPOWL(operator=Operator.TRANSITION, children=[client_approval])
client_approval_transition = OperatorPOWL(operator=Operator.TRANSITION, children=[certification_issue])
certification_issue_transition = OperatorPOWL(operator=Operator.TRANSITION, children=[archive_record])

# Define the partial order
root = StrictPartialOrder(nodes=[
    initial_review_transition,
    provenance_check_transition,
    material_scan_transition,
    chemical_test_transition,
    imaging_capture_transition,
    expert_consult_transition,
    historical_match_transition,
    forgery_detect_transition,
    documentation_verify_transition,
    cross_border_check_transition,
    condition_assess_transition,
    value_estimate_transition,
    report_draft_transition,
    report_review_transition,
    client_approval_transition,
    certification_issue_transition,
    archive_record
])
root.order.add_edge(initial_review_transition, provenance_check_transition)
root.order.add_edge(provenance_check_transition, material_scan_transition)
root.order.add_edge(material_scan_transition, chemical_test_transition)
root.order.add_edge(chemical_test_transition, imaging_capture_transition)
root.order.add_edge(imaging_capture_transition, expert_consult_transition)
root.order.add_edge(expert_consult_transition, historical_match_transition)
root.order.add_edge(historical_match_transition, forgery_detect_transition)
root.order.add_edge(forgery_detect_transition, documentation_verify_transition)
root.order.add_edge(documentation_verify_transition, cross_border_check_transition)
root.order.add_edge(cross_border_check_transition, condition_assess_transition)
root.order.add_edge(condition_assess_transition, value_estimate_transition)
root.order.add_edge(value_estimate_transition, report_draft_transition)
root.order.add_edge(report_draft_transition, report_review_transition)
root.order.add_edge(report_review_transition, client_approval_transition)
root.order.add_edge(client_approval_transition, certification_issue_transition)
root.order.add_edge(certification_issue_transition, archive_record)