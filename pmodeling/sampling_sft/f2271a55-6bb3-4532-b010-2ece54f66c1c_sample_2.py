import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
provenance_check = Transition(label='Provenance Check')
spectroscopy_test = Transition(label='Spectroscopy Test')
carbon_dating = Transition(label='Carbon Dating')
style_analysis = Transition(label='Style Analysis')
image_scanning = Transition(label='Image Scanning')
restoration_scan = Transition(label='Restoration Scan')
appraiser_review = Transition(label='Appraiser Review')
database_match = Transition(label='Database Match')
forgery_detect = Transition(label='Forgery Detect')
report_compilation = Transition(label='Report Compilation')
blockchain_entry = Transition(label='Blockchain Entry')
certificate_issue = Transition(label='Certificate Issue')
client_briefing = Transition(label='Client Briefing')
secure_storage = Transition(label='Secure Storage')
final_approval = Transition(label='Final Approval')

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    provenance_check,
    spectroscopy_test,
    carbon_dating,
    style_analysis,
    image_scanning,
    restoration_scan,
    appraiser_review,
    database_match,
    forgery_detect,
    report_compilation,
    blockchain_entry,
    certificate_issue,
    client_briefing,
    secure_storage,
    final_approval
])

# Provenance -> spectroscopy & carbon dating in parallel
root.order.add_edge(provenance_check, spectroscopy_test)
root.order.add_edge(provenance_check, carbon_dating)

# Spectroscopy & carbon dating -> style analysis in parallel
root.order.add_edge(spectroscopy_test, style_analysis)
root.order.add_edge(carbon_dating, style_analysis)

# Style analysis -> image scanning
root.order.add_edge(style_analysis, image_scanning)

# Image scanning -> restoration scan
root.order.add_edge(image_scanning, restoration_scan)

# Restoration scan -> appraiser review
root.order.add_edge(restoration_scan, appraiser_review)

# Appraiser review -> database match
root.order.add_edge(appraiser_review, database_match)

# Database match -> forgery detection
root.order.add_edge(database_match, forgery_detect)

# Forgery detection -> report compilation
root.order.add_edge(forgery_detect, report_compilation)

# Report compilation -> blockchain entry
root.order.add_edge(report_compilation, blockchain_entry)

# Blockchain entry -> certificate issue
root.order.add_edge(blockchain_entry, certificate_issue)

# Certificate issue -> client briefing
root.order.add_edge(certificate_issue, client_briefing)

# Client briefing -> secure storage
root.order.add_edge(client_briefing, secure_storage)

# Secure storage -> final approval
root.order.add_edge(secure_storage, final_approval)