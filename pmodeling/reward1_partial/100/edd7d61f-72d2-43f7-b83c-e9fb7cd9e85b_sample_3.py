import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

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

# Define the workflow
loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[initial_review, provenance_check, material_scan, chemical_test, imaging_capture, expert_consult, historical_match, forgery_detect, documentation_verify, cross_border_check, condition_assess, value_estimate, report_draft, report_review, client_approval, certification_issue])
loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[archive_record])

xor = OperatorPOWL(operator=Operator.XOR, children=[loop_1, loop_2])

root = StrictPartialOrder(nodes=[xor])
root.order.add_edge(loop_1, xor)
root.order.add_edge(loop_2, xor)

print(root)