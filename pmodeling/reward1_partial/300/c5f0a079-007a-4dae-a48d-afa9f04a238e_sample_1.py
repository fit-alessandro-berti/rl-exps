import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
provenance_check = Transition(label='Provenance Check')
material_scan = Transition(label='Material Scan')
wear_analysis = Transition(label='Wear Analysis')
image_capture = Transition(label='Image Capture')
pattern_match = Transition(label='Pattern Match')
ownership_verify = Transition(label='Ownership Verify')
ethics_review = Transition(label='Ethics Review')
carbon_dating = Transition(label='Carbon Dating')
restoration_eval = Transition(label='Restoration Eval')
report_draft = Transition(label='Report Draft')
stakeholder_review = Transition(label='Stakeholder Review')
archive_data = Transition(label='Archive Data')
exhibit_approve = Transition(label='Exhibit Approve')
condition_monitor = Transition(label='Condition Monitor')
final_certification = Transition(label='Final Certification')

# Define operators
xor = OperatorPOWL(operator=Operator.XOR, children=[pattern_match, image_capture])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[ethics_review, stakeholder_review])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[condition_monitor, exhibit_approve])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[final_certification, archive_data])

# Define loops
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, material_scan])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[wear_analysis, carbon_dating])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[restoration_eval, report_draft])

# Define partial order
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, xor, xor2, xor3, xor4])
root.order.add_edge(loop1, xor)
root.order.add_edge(loop2, xor)
root.order.add_edge(loop3, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor, xor3)
root.order.add_edge(xor2, xor4)
root.order.add_edge(xor3, xor4)