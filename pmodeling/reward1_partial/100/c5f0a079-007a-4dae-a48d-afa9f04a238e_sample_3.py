from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

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

# Define silent transitions for concurrency
skip1 = SilentTransition()
skip2 = SilentTransition()

# Define exclusive choice for Wear Analysis and Image Capture
xor1 = OperatorPOWL(operator=Operator.XOR, children=[wear_analysis, skip1])

# Define exclusive choice for Pattern Match and Ownership Verify
xor2 = OperatorPOWL(operator=Operator.XOR, children=[pattern_match, skip2])

# Define exclusive choice for Ethics Review and Carbon Dating
xor3 = OperatorPOWL(operator=Operator.XOR, children=[ethics_review, skip2])

# Define exclusive choice for Restoration Eval and Final Certification
xor4 = OperatorPOWL(operator=Operator.XOR, children=[restoration_eval, skip2])

# Define loop for Condition Monitor and Final Certification
loop = OperatorPOWL(operator=Operator.LOOP, children=[condition_monitor, final_certification])

# Define partial order for the process
root = StrictPartialOrder(nodes=[provenance_check, material_scan, xor1, xor2, xor3, xor4, loop])
root.order.add_edge(provenance_check, material_scan)
root.order.add_edge(material_scan, xor1)
root.order.add_edge(material_scan, xor2)
root.order.add_edge(material_scan, xor3)
root.order.add_edge(material_scan, xor4)
root.order.add_edge(xor1, loop)
root.order.add_edge(xor2, loop)
root.order.add_edge(xor3, loop)
root.order.add_edge(xor4, loop)
root.order.add_edge(loop, condition_monitor)
root.order.add_edge(loop, final_certification)