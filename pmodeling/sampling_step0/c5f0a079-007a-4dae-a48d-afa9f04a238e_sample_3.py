import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the silent transitions
skip = SilentTransition()

# Define the partial order structure
loop = OperatorPOWL(operator=Operator.LOOP, children=[condition_monitor, final_certification])
xor = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, material_scan])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[wear_analysis, image_capture])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[pattern_match, ownership_verify])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[ethics_review, carbon_dating])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[restoration_eval, report_draft])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_review, archive_data])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[exhibit_approve, skip])

# Create the root partial order
root = StrictPartialOrder(nodes=[loop, xor, xor2, xor3, xor4, xor5, xor6, xor7])
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, loop)