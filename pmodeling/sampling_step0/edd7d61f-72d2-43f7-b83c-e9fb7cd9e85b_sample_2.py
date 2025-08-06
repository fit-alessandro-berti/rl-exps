import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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
skip1 = SilentTransition()
skip2 = SilentTransition()

# Define loops
provenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, skip1])
material_scan_loop = OperatorPOWL(operator=Operator.LOOP, children=[material_scan, skip2])
chemical_test_loop = OperatorPOWL(operator=Operator.LOOP, children=[chemical_test, skip2])
imaging_capture_loop = OperatorPOWL(operator=Operator.LOOP, children=[imaging_capture, skip2])

# Define XORs
cross_border_xor = OperatorPOWL(operator=Operator.XOR, children=[cross_border_check, skip1])
documentation_verify_xor = OperatorPOWL(operator=Operator.XOR, children=[documentation_verify, skip1])
condition_assess_xor = OperatorPOWL(operator=Operator.XOR, children=[condition_assess, skip1])
value_estimate_xor = OperatorPOWL(operator=Operator.XOR, children=[value_estimate, skip1])
report_draft_xor = OperatorPOWL(operator=Operator.XOR, children=[report_draft, skip1])
report_review_xor = OperatorPOWL(operator=Operator.XOR, children=[report_review, skip1])
client_approval_xor = OperatorPOWL(operator=Operator.XOR, children=[client_approval, skip1])
certification_issue_xor = OperatorPOWL(operator=Operator.XOR, children=[certification_issue, skip1])
archive_record_xor = OperatorPOWL(operator=Operator.XOR, children=[archive_record, skip1])

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    initial_review,
    provenance_loop,
    material_scan_loop,
    chemical_test_loop,
    imaging_capture_loop,
    expert_consult,
    historical_match,
    forgery_detect,
    documentation_verify_xor,
    cross_border_xor,
    condition_assess_xor,
    value_estimate_xor,
    report_draft_xor,
    report_review_xor,
    client_approval_xor,
    certification_issue_xor,
    archive_record_xor
])

# Define the order dependencies
root.order.add_edge(initial_review, provenance_loop)
root.order.add_edge(provenance_loop, material_scan_loop)
root.order.add_edge(material_scan_loop, chemical_test_loop)
root.order.add_edge(chemical_test_loop, imaging_capture_loop)
root.order.add_edge(imaging_capture_loop, expert_consult)
root.order.add_edge(expert_consult, historical_match)
root.order.add_edge(historical_match, forgery_detect)
root.order.add_edge(forgery_detect, documentation_verify_xor)
root.order.add_edge(documentation_verify_xor, cross_border_xor)
root.order.add_edge(cross_border_xor, condition_assess_xor)
root.order.add_edge(condition_assess_xor, value_estimate_xor)
root.order.add_edge(value_estimate_xor, report_draft_xor)
root.order.add_edge(report_draft_xor, report_review_xor)
root.order.add_edge(report_review_xor, client_approval_xor)
root.order.add_edge(client_approval_xor, certification_issue_xor)
root.order.add_edge(certification_issue_xor, archive_record_xor)

# Print the root POWL model
print(root)