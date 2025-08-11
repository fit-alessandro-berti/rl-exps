import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define exclusive choice for expert appraisal and digital imaging
xor = OperatorPOWL(operator=Operator.XOR, children=[appraiser_review, image_scanning])

# Define loop for blockchain entry and final approval
loop = OperatorPOWL(operator=Operator.LOOP, children=[blockchain_entry, final_approval])

# Define partial order
root = StrictPartialOrder(nodes=[provenance_check, spectroscopy_test, carbon_dating, style_analysis, image_scanning, restoration_scan, xor, loop])

# Define the order of dependencies
root.order.add_edge(provenance_check, spectroscopy_test)
root.order.add_edge(provenance_check, carbon_dating)
root.order.add_edge(provenance_check, style_analysis)
root.order.add_edge(spectroscopy_test, xor)
root.order.add_edge(carbon_dating, xor)
root.order.add_edge(style_analysis, xor)
root.order.add_edge(xor, blockchain_entry)
root.order.add_edge(blockchain_entry, final_approval)
root.order.add_edge(final_approval, loop)

print(root)