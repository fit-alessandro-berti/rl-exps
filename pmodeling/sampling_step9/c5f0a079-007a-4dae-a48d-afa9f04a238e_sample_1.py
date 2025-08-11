import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define the POWL model
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, material_scan])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[wear_analysis, skip])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[image_capture, pattern_match])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[ownership_verify, ethics_review])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[carbon_dating, restoration_eval])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[report_draft, stakeholder_review])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[archive_data, exhibit_approve])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[condition_monitor, final_certification])

# Define the root POWL model
root = StrictPartialOrder(nodes=[loop1, xor1, loop2, xor2, loop3, xor3, loop4, xor4])
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop2, xor2)
root.order.add_edge(loop3, xor3)
root.order.add_edge(loop4, xor4)

# Print the root POWL model
print(root)