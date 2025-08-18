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

# Define the process workflow using the defined transitions
loop_provenance = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, chemical_test, imaging_capture, expert_consult, historical_match, forgery_detect])
xor_documentation = OperatorPOWL(operator=Operator.XOR, children=[documentation_verify, skip])
xor_cross_border = OperatorPOWL(operator=Operator.XOR, children=[cross_border_check, skip])
xor_condition = OperatorPOWL(operator=Operator.XOR, children=[condition_assess, skip])
xor_value = OperatorPOWL(operator=Operator.XOR, children=[value_estimate, skip])
xor_report = OperatorPOWL(operator=Operator.XOR, children=[report_draft, skip])
xor_approval = OperatorPOWL(operator=Operator.XOR, children=[client_approval, skip])
xor_issue = OperatorPOWL(operator=Operator.XOR, children=[certification_issue, skip])
xor_archive = OperatorPOWL(operator=Operator.XOR, children=[archive_record, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[initial_review, loop_provenance, xor_documentation, xor_cross_border, xor_condition, xor_value, xor_report, xor_approval, xor_issue, xor_archive])
root.order.add_edge(initial_review, loop_provenance)
root.order.add_edge(loop_provenance, xor_documentation)
root.order.add_edge(xor_documentation, xor_cross_border)
root.order.add_edge(xor_cross_border, xor_condition)
root.order.add_edge(xor_condition, xor_value)
root.order.add_edge(xor_value, xor_report)
root.order.add_edge(xor_report, xor_approval)
root.order.add_edge(xor_approval, xor_issue)
root.order.add_edge(xor_issue, xor_archive)

print(root)