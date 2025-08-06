import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define each activity as a Transition object
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

# Define the control flow operations
xor = OperatorPOWL(operator=Operator.XOR, children=[appraiser_review, forgery_detect])
loop = OperatorPOWL(operator=Operator.LOOP, children=[database_match, blockchain_entry, certificate_issue])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[report_compilation, client_briefing])

# Define the partial order
root = StrictPartialOrder(nodes=[provenance_check, spectroscopy_test, carbon_dating, style_analysis, image_scanning, restoration_scan, xor, loop, xor2, secure_storage, final_approval])

# Add edges to represent the dependencies
root.order.add_edge(provenance_check, spectroscopy_test)
root.order.add_edge(spectroscopy_test, carbon_dating)
root.order.add_edge(carbon_dating, style_analysis)
root.order.add_edge(style_analysis, image_scanning)
root.order.add_edge(image_scanning, restoration_scan)
root.order.add_edge(restoration_scan, xor)
root.order.add_edge(xor, loop)
root.order.add_edge(loop, xor2)
root.order.add_edge(xor2, secure_storage)
root.order.add_edge(secure_storage, final_approval)

print(root)