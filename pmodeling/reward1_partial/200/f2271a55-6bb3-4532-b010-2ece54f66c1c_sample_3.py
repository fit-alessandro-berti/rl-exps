from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

skip = SilentTransition()

# Define the partial order
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[spectroscopy_test, carbon_dating])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[style_analysis, image_scanning])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[restoration_scan, appraiser_review])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[database_match, blockchain_entry])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[certificate_issue, forgery_detect])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[report_compilation, client_briefing])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[secure_storage, final_approval])

root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5, loop6, loop7])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, loop5)
root.order.add_edge(loop5, loop6)
root.order.add_edge(loop6, loop7)