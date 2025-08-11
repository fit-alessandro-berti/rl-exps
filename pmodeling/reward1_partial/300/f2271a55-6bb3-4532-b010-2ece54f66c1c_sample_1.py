import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities)
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

# Define POWL models
provenance_check_process = StrictPartialOrder(nodes=[provenance_check])
spectroscopy_test_process = StrictPartialOrder(nodes=[spectroscopy_test])
carbon_dating_process = StrictPartialOrder(nodes=[carbon_dating])
style_analysis_process = StrictPartialOrder(nodes=[style_analysis])
image_scanning_process = StrictPartialOrder(nodes=[image_scanning])
restoration_scan_process = StrictPartialOrder(nodes=[restoration_scan])
appraiser_review_process = StrictPartialOrder(nodes=[appraiser_review])
database_match_process = StrictPartialOrder(nodes=[database_match])
blockchain_entry_process = StrictPartialOrder(nodes=[blockchain_entry])
certificate_issue_process = StrictPartialOrder(nodes=[certificate_issue])
forgery_detect_process = StrictPartialOrder(nodes=[forgery_detect])
report_compilation_process = StrictPartialOrder(nodes=[report_compilation])
client_briefing_process = StrictPartialOrder(nodes=[client_briefing])
secure_storage_process = StrictPartialOrder(nodes=[secure_storage])
final_approval_process = StrictPartialOrder(nodes=[final_approval])

# Define dependencies
root = StrictPartialOrder(nodes=[provenance_check_process, spectroscopy_test_process, carbon_dating_process, style_analysis_process, image_scanning_process, restoration_scan_process, appraiser_review_process, database_match_process, blockchain_entry_process, certificate_issue_process, forgery_detect_process, report_compilation_process, client_briefing_process, secure_storage_process, final_approval_process])

# Add dependencies
root.order.add_edge(provenance_check_process, spectroscopy_test_process)
root.order.add_edge(spectroscopy_test_process, carbon_dating_process)
root.order.add_edge(carbon_dating_process, style_analysis_process)
root.order.add_edge(style_analysis_process, image_scanning_process)
root.order.add_edge(image_scanning_process, restoration_scan_process)
root.order.add_edge(restoration_scan_process, appraiser_review_process)
root.order.add_edge(appraiser_review_process, database_match_process)
root.order.add_edge(database_match_process, blockchain_entry_process)
root.order.add_edge(blockchain_entry_process, certificate_issue_process)
root.order.add_edge(certificate_issue_process, forgery_detect_process)
root.order.add_edge(forgery_detect_process, report_compilation_process)
root.order.add_edge(report_compilation_process, client_briefing_process)
root.order.add_edge(client_briefing_process, secure_storage_process)
root.order.add_edge(secure_storage_process, final_approval_process)

# Print the root POWL model
print(root)