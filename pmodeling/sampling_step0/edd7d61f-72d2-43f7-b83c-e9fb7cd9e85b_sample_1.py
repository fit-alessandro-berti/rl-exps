from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define workflow
loop = OperatorPOWL(operator=Operator.LOOP, children=[material_scan, chemical_test, imaging_capture])
xor = OperatorPOWL(operator=Operator.XOR, children=[historical_match, forgery_detect, documentation_verify, cross_border_check])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[condition_assess, value_estimate])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[report_draft, report_review, client_approval])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[certification_issue, archive_record])
root = StrictPartialOrder(nodes=[initial_review, provenance_check, loop, xor, xor2, xor3, xor4])

# Add dependencies
root.order.add_edge(initial_review, provenance_check)
root.order.add_edge(provenance_check, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)

print(root)