from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

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

# Define the loop for the blockchain entry process
loop = OperatorPOWL(operator=Operator.LOOP, children=[blockchain_entry, certificate_issue])

# Define the exclusive choice for forgery detection and report compilation
xor = OperatorPOWL(operator=Operator.XOR, children=[forgery_detect, report_compilation])

# Define the root model
root = StrictPartialOrder(nodes=[provenance_check, spectroscopy_test, carbon_dating, style_analysis, image_scanning, restoration_scan, appraiser_review, database_match, loop, xor, certificate_issue, forgery_detect, report_compilation, client_briefing, secure_storage, final_approval])

# Define the dependencies in the root model
root.order.add_edge(provenance_check, spectroscopy_test)
root.order.add_edge(provenance_check, carbon_dating)
root.order.add_edge(provenance_check, style_analysis)
root.order.add_edge(provenance_check, image_scanning)
root.order.add_edge(provenance_check, restoration_scan)
root.order.add_edge(provenance_check, appraiser_review)
root.order.add_edge(provenance_check, database_match)
root.order.add_edge(spectroscopy_test, database_match)
root.order.add_edge(carbon_dating, database_match)
root.order.add_edge(style_analysis, database_match)
root.order.add_edge(image_scanning, database_match)
root.order.add_edge(restoration_scan, database_match)
root.order.add_edge(appraiser_review, database_match)
root.order.add_edge(database_match, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, certificate_issue)
root.order.add_edge(xor, forgery_detect)
root.order.add_edge(xor, report_compilation)
root.order.add_edge(certificate_issue, client_briefing)
root.order.add_edge(forgery_detect, client_briefing)
root.order.add_edge(report_compilation, client_briefing)
root.order.add_edge(client_briefing, secure_storage)
root.order.add_edge(secure_storage, final_approval)