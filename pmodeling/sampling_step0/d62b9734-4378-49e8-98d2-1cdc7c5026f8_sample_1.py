import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the control flow
skip = SilentTransition()
xor1 = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, customs_clear])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[registry_search, data_log])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[historical_cross, expert_review])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[condition_assess, chain_custody])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[auction_prep, secure_archive])
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, image_capture])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[material_scan, xor1])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[xor2, xor3])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[xor4, xor5])
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, xor1, xor2, xor3, xor4, xor5])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)

# Print the POWL model
print(root)