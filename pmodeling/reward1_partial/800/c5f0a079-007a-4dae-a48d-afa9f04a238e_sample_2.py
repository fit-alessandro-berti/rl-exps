import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the control-flow operators
xor = OperatorPOWL(operator=Operator.XOR, children=[pattern_match, ownership_verify])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[restoration_eval, condition_monitor])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_review, exhibit_approve])
loop = OperatorPOWL(operator=Operator.LOOP, children=[carbon_dating, final_certification])

# Define the partial order
root = StrictPartialOrder(nodes=[provenance_check, material_scan, wear_analysis, image_capture, xor, xor2, xor3, loop])
root.order.add_edge(provenance_check, material_scan)
root.order.add_edge(material_scan, wear_analysis)
root.order.add_edge(wear_analysis, image_capture)
root.order.add_edge(image_capture, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, loop)
root.order.add_edge(loop, final_certification)

# Add edges to connect XORs and loops
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, loop)
root.order.add_edge(loop, final_certification)