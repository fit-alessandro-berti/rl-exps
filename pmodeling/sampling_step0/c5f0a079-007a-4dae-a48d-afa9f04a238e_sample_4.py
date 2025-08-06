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

# Define loops and exclusive choices
# Provenance Check -> Material Scan (exclusive choice)
xor = OperatorPOWL(operator=Operator.XOR, children=[material_scan, skip])
root = StrictPartialOrder(nodes=[provenance_check, xor])

# Material Scan -> Wear Analysis (loop)
loop = OperatorPOWL(operator=Operator.LOOP, children=[wear_analysis])
root.order.add_edge(provenance_check, xor)
root.order.add_edge(xor, loop)

# Wear Analysis -> Image Capture (loop)
loop = OperatorPOWL(operator=Operator.LOOP, children=[image_capture])
root.order.add_edge(material_scan, loop)

# Image Capture -> Pattern Match (exclusive choice)
xor = OperatorPOWL(operator=Operator.XOR, children=[pattern_match, skip])
root.order.add_edge(loop, xor)

# Pattern Match -> Ownership Verify (loop)
loop = OperatorPOWL(operator=Operator.LOOP, children=[ownership_verify])
root.order.add_edge(xor, loop)

# Ownership Verify -> Ethics Review (loop)
loop = OperatorPOWL(operator=Operator.LOOP, children=[ethics_review])
root.order.add_edge(loop, loop)

# Ethics Review -> Carbon Dating (loop)
loop = OperatorPOWL(operator=Operator.LOOP, children=[carbon_dating])
root.order.add_edge(ethics_review, loop)

# Carbon Dating -> Restoration Eval (loop)
loop = OperatorPOWL(operator=Operator.LOOP, children=[restoration_eval])
root.order.add_edge(carbon_dating, loop)

# Restoration Eval -> Report Draft (loop)
loop = OperatorPOWL(operator=Operator.LOOP, children=[report_draft])
root.order.add_edge(restoration_eval, loop)

# Report Draft -> Stakeholder Review (loop)
loop = OperatorPOWL(operator=Operator.LOOP, children=[stakeholder_review])
root.order.add_edge(report_draft, loop)

# Stakeholder Review -> Archive Data (loop)
loop = OperatorPOWL(operator=Operator.LOOP, children=[archive_data])
root.order.add_edge(stakeholder_review, loop)

# Archive Data -> Exhibit Approve (loop)
loop = OperatorPOWL(operator=Operator.LOOP, children=[exhibit_approve])
root.order.add_edge(archive_data, loop)

# Exhibit Approve -> Condition Monitor (loop)
loop = OperatorPOWL(operator=Operator.LOOP, children=[condition_monitor])
root.order.add_edge(exhibit_approve, loop)

# Condition Monitor -> Final Certification (loop)
loop = OperatorPOWL(operator=Operator.LOOP, children=[final_certification])
root.order.add_edge(condition_monitor, loop)

# Final Certification -> End
root.order.add_edge(final_certification, final_certification)

# Print the final POWL model
print(root)