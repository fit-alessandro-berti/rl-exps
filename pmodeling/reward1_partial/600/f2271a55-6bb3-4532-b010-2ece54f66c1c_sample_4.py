from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define activities
provenance_check = Transition(label='Provenance Check')
spectroscopy_test = Transition(label='Spectroscopy Test')
carbon_dating = Transition(label='Carbon Dating')
style_analysis = Transition(label='Style Analysis')
image_scanning = Transition(label='Image Scanning')
restoration_scan = Transition(label='Restoration Scan')
appraiser_review = Transition(label='Appraiser Review')
database_match = Transition(label='Database Match')
blockchain_entry = Transition(label='Blockchain Entry')
certificate_issue = Transition(label='Certificate Issue')
forgery_detect = Transition(label='Forgery Detect')
report_compilation = Transition(label='Report Compilation')
client_briefing = Transition(label='Client Briefing')
secure_storage = Transition(label='Secure Storage')
final_approval = Transition(label='Final Approval')

# Define control flow operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[appraiser_review, database_match])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[restoration_scan, image_scanning])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[carbon_dating, spectroscopy_test])
loop = OperatorPOWL(operator=Operator.LOOP, children=[xor3, xor2, xor1])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[forgery_detect, report_compilation])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[secure_storage, final_approval])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[client_briefing, certificate_issue])

# Create the root POWL model
root = StrictPartialOrder(nodes=[provenance_check, loop, xor4, xor5, xor6])
root.order.add_edge(provenance_check, loop)
root.order.add_edge(loop, xor4)
root.order.add_edge(loop, xor5)
root.order.add_edge(loop, xor6)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor4, xor6)
root.order.add_edge(xor5, xor6)

# Print the root model
print(root)