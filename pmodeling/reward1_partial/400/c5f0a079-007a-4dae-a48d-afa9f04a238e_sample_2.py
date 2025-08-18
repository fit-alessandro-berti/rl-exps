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

# Define silent transitions
skip = SilentTransition()

# Define the POWL model
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, material_scan, wear_analysis, image_capture])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[pattern_match, ownership_verify, ethics_review, carbon_dating])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[restoration_eval, report_draft, stakeholder_review])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[archive_data, exhibit_approve, condition_monitor, final_certification])

# Define the partial order
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4])

# Add dependencies
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)

# Print the root model
print(root)