import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the workflow structure
xor1 = OperatorPOWL(operator=Operator.XOR, children=[documentation_verify, cross_border_check])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[condition_assess, value_estimate])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[historical_match, forgery_detect])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, imaging_capture])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[chemical_test, material_scan])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, initial_review])

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[xor1, xor2])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[xor3, xor4])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[xor5, xor6])

root = StrictPartialOrder(nodes=[loop1, loop2, loop3])
root.order.add_edge(loop1, xor2)
root.order.add_edge(loop2, xor3)
root.order.add_edge(loop3, xor4)

print(root)