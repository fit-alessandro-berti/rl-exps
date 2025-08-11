import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the process
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

skip = SilentTransition()

# Define the workflow steps
provenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, skip])
material_scan_loop = OperatorPOWL(operator=Operator.LOOP, children=[material_scan, skip])
chemical_test_loop = OperatorPOWL(operator=Operator.LOOP, children=[chemical_test, skip])
imaging_capture_loop = OperatorPOWL(operator=Operator.LOOP, children=[imaging_capture, skip])
expert_consult_loop = OperatorPOWL(operator=Operator.LOOP, children=[expert_consult, skip])
historical_match_loop = OperatorPOWL(operator=Operator.LOOP, children=[historical_match, skip])
forgery_detect_loop = OperatorPOWL(operator=Operator.LOOP, children=[forgery_detect, skip])
documentation_verify_loop = OperatorPOWL(operator=Operator.LOOP, children=[documentation_verify, skip])
cross_border_check_loop = OperatorPOWL(operator=Operator.LOOP, children=[cross_border_check, skip])
condition_assess_loop = OperatorPOWL(operator=Operator.LOOP, children=[condition_assess, skip])
value_estimate_loop = OperatorPOWL(operator=Operator.LOOP, children=[value_estimate, skip])

# Define the choice between different loops
verification_choice = OperatorPOWL(operator=Operator.XOR, children=[provenance_loop, material_scan_loop, chemical_test_loop, imaging_capture_loop, expert_consult_loop, historical_match_loop, forgery_detect_loop, documentation_verify_loop, cross_border_check_loop, condition_assess_loop, value_estimate_loop])

# Define the main workflow
root = StrictPartialOrder(nodes=[initial_review, verification_choice, report_draft, report_review, client_approval, certification_issue, archive_record])
root.order.add_edge(initial_review, verification_choice)
root.order.add_edge(verification_choice, report_draft)
root.order.add_edge(report_draft, report_review)
root.order.add_edge(report_review, client_approval)
root.order.add_edge(client_approval, certification_issue)
root.order.add_edge(certification_issue, archive_record)