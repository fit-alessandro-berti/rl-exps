import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define the partial order
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[wear_analysis, image_capture, pattern_match])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, material_scan])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[ownership_verify, ethics_review])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[carbon_dating, restoration_eval])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[report_draft, stakeholder_review])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[archive_data, exhibit_approve])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[condition_monitor, final_certification])

root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5, xor6, loop1])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor1, xor3)
root.order.add_edge(xor1, xor4)
root.order.add_edge(xor1, xor5)
root.order.add_edge(xor1, xor6)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor2, xor4)
root.order.add_edge(xor2, xor5)
root.order.add_edge(xor2, xor6)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor3, xor5)
root.order.add_edge(xor3, xor6)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor4, xor6)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, loop1)

print(root)