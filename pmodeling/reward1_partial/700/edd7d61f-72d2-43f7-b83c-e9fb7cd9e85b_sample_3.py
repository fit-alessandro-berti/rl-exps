import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

# Define the POWL model
xor1 = OperatorPOWL(operator=Operator.XOR, children=[documentation_verify, cross_border_check])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[historical_match, forgery_detect])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[material_scan, chemical_test])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[condition_assess, value_estimate])

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[expert_consult, xor1])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, xor2])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[imaging_capture, xor3])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[report_review, client_approval])

root = StrictPartialOrder(nodes=[initial_review, loop1, loop2, loop3, loop4, xor4, certification_issue, archive_record])
root.order.add_edge(initial_review, loop1)
root.order.add_edge(initial_review, loop2)
root.order.add_edge(initial_review, loop3)
root.order.add_edge(initial_review, loop4)
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop2, xor2)
root.order.add_edge(loop3, xor3)
root.order.add_edge(loop4, xor4)
root.order.add_edge(xor1, certification_issue)
root.order.add_edge(xor2, certification_issue)
root.order.add_edge(xor3, certification_issue)
root.order.add_edge(xor4, archive_record)
root.order.add_edge(certification_issue, archive_record)