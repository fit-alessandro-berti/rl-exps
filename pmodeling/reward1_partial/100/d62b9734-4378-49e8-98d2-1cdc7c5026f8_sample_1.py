import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
provenance_check = Transition(label='Provenance Check')
image_capture = Transition(label='Image Capture')
material_scan = Transition(label='Material Scan')
expert_review = Transition(label='Expert Review')
historical_cross = Transition(label='Historical Cross')
legal_verify = Transition(label='Legal Verify')
registry_search = Transition(label='Registry Search')
customs_clear = Transition(label='Customs Clear')
condition_assess = Transition(label='Condition Assess')
data_log = Transition(label='Data Log')
chain_custody = Transition(label='Chain Custody')
report_draft = Transition(label='Report Draft')
certification = Transition(label='Certification')
secure_archive = Transition(label='Secure Archive')
auction_prep = Transition(label='Auction Prep')

# Define silent transitions for loops and XORs
skip = SilentTransition()

# Define the POWL model
loop_image_capture = OperatorPOWL(operator=Operator.LOOP, children=[image_capture, material_scan])
loop_legal_verify = OperatorPOWL(operator=Operator.LOOP, children=[legal_verify, registry_search, customs_clear])
xor_report_draft = OperatorPOWL(operator=Operator.XOR, children=[report_draft, auction_prep])

# Create the root POWL model
root = StrictPartialOrder(nodes=[provenance_check, expert_review, historical_cross, loop_image_capture, loop_legal_verify, xor_report_draft])
root.order.add_edge(provenance_check, expert_review)
root.order.add_edge(provenance_check, historical_cross)
root.order.add_edge(expert_review, loop_image_capture)
root.order.add_edge(historical_cross, loop_legal_verify)
root.order.add_edge(loop_image_capture, xor_report_draft)
root.order.add_edge(loop_legal_verify, xor_report_draft)

# Print the root POWL model
print(root)