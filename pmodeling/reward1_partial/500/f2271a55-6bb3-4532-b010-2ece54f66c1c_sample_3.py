import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the relationships between the activities using the POWL model
xor1 = OperatorPOWL(operator=Operator.XOR, children=[spectroscopy_test, carbon_dating, style_analysis, image_scanning, restoration_scan])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[appraiser_review, database_match, blockchain_entry])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[certificate_issue, forgery_detect, report_compilation])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[client_briefing, secure_storage, final_approval])

# Define the partial order of the activities
root = StrictPartialOrder(nodes=[provenance_check, xor1, xor2, xor3, xor4])
root.order.add_edge(provenance_check, xor1)
root.order.add_edge(provenance_check, xor2)
root.order.add_edge(provenance_check, xor3)
root.order.add_edge(provenance_check, xor4)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor1, xor3)
root.order.add_edge(xor1, xor4)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor2, xor4)
root.order.add_edge(xor3, xor4)