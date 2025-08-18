import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) in the process
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

# Define the control-flow operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[historical_match, forgery_detect])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[documentation_verify, cross_border_check])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[condition_assess, value_estimate])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[report_draft, report_review])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[client_approval, certification_issue])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[archive_record])

# Create the root POWL model
root = StrictPartialOrder(nodes=[initial_review, provenance_check, material_scan, chemical_test, imaging_capture, expert_consult, xor1, xor2, xor3, xor4, xor5, xor6])
root.order.add_edge(initial_review, provenance_check)
root.order.add_edge(provenance_check, material_scan)
root.order.add_edge(material_scan, chemical_test)
root.order.add_edge(chemical_test, imaging_capture)
root.order.add_edge(imaging_capture, expert_consult)
root.order.add_edge(expert_consult, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, archive_record)

print(root)