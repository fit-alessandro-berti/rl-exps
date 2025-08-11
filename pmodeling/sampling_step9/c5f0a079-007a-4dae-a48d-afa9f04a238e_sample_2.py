import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

skip = SilentTransition()

# Define the POWL operators
xor = OperatorPOWL(operator=Operator.XOR, children=[pattern_match, skip])
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[restoration_eval, condition_monitor])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[exhibit_approve, final_certification])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[stakeholder_review, archive_data])

# Define the POWL model
root = StrictPartialOrder(nodes=[provenance_check, material_scan, wear_analysis, image_capture, xor, loop1, loop2, loop3])
root.order.add_edge(provenance_check, material_scan)
root.order.add_edge(material_scan, wear_analysis)
root.order.add_edge(wear_analysis, image_capture)
root.order.add_edge(image_capture, xor)
root.order.add_edge(xor, loop1)
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, stakeholder_review)
root.order.add_edge(stakeholder_review, archive_data)
root.order.add_edge(archive_data, exhibit_approve)
root.order.add_edge(exhibit_approve, final_certification)

print(root)