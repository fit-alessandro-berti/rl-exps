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
forgeries_detect = Transition(label='Forgery Detect')
report_compilation = Transition(label='Report Compilation')
client_briefing = Transition(label='Client Briefing')
secure_storage = Transition(label='Secure Storage')
final_approval = Transition(label='Final Approval')

# Define silent transitions (empty labels)
skip1 = SilentTransition()
skip2 = SilentTransition()
skip3 = SilentTransition()
skip4 = SilentTransition()
skip5 = SilentTransition()
skip6 = SilentTransition()
skip7 = SilentTransition()

# Define POWL model
root = StrictPartialOrder(nodes=[
    provenance_check,
    spectroscopy_test,
    carbon_dating,
    style_analysis,
    image_scanning,
    restoration_scan,
    appraiser_review,
    database_match,
    blockchain_entry,
    certificate_issue,
    forgeries_detect,
    report_compilation,
    client_briefing,
    secure_storage,
    final_approval
])

# Define edges in the partial order
root.order.add_edge(provenance_check, spectroscopy_test)
root.order.add_edge(provenance_check, carbon_dating)
root.order.add_edge(spectroscopy_test, style_analysis)
root.order.add_edge(spectroscopy_test, image_scanning)
root.order.add_edge(carbon_dating, style_analysis)
root.order.add_edge(carbon_dating, image_scanning)
root.order.add_edge(style_analysis, database_match)
root.order.add_edge(image_scanning, database_match)
root.order.add_edge(database_match, blockchain_entry)
root.order.add_edge(blockchain_entry, certificate_issue)
root.order.add_edge(certificate_issue, forgeries_detect)
root.order.add_edge(forgeries_detect, report_compilation)
root.order.add_edge(report_compilation, client_briefing)
root.order.add_edge(client_briefing, secure_storage)
root.order.add_edge(secure_storage, final_approval)

# Output the root POWL model
print(root)