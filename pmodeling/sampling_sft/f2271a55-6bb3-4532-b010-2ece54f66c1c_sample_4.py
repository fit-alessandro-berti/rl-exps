import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
provenance_check      = Transition(label='Provenance Check')
spectroscopy_test     = Transition(label='Spectroscopy Test')
carbon_dating         = Transition(label='Carbon Dating')
style_analysis        = Transition(label='Style Analysis')
image_scanning        = Transition(label='Image Scanning')
restoration_scan      = Transition(label='Restoration Scan')
appraiser_review      = Transition(label='Appraiser Review')
database_match        = Transition(label='Database Match')
forgery_detect        = Transition(label='Forgery Detect')
report_compilation    = Transition(label='Report Compilation')
blockchain_entry      = Transition(label='Blockchain Entry')
certificate_issue     = Transition(label='Certificate Issue')
client_briefing       = Transition(label='Client Briefing')
secure_storage        = Transition(label='Secure Storage')
final_approval        = Transition(label='Final Approval')

# Loop for continuous forgery detection and report compilation
# Body of the loop: forgery_detect -> report_compilation
loop_body = StrictPartialOrder(nodes=[forgery_detect, report_compilation])
# No exit condition, so the loop runs indefinitely (or until exit)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    provenance_check,
    spectroscopy_test,
    carbon_dating,
    style_analysis,
    image_scanning,
    restoration_scan,
    appraiser_review,
    database_match,
    loop_body,
    blockchain_entry,
    certificate_issue,
    client_briefing,
    secure_storage,
    final_approval
])

# Sequential order
root.order.add_edge(provenance_check,   spectroscopy_test)
root.order.add_edge(provenance_check,   carbon_dating)
root.order.add_edge(provenance_check,   style_analysis)
root.order.add_edge(provenance_check,   image_scanning)
root.order.add_edge(provenance_check,   restoration_scan)
root.order.add_edge(provenance_check,   appraiser_review)

# After appraiser review, match with database
root.order.add_edge(appraiser_review,   database_match)

# After database match, optionally enter the forgery loop
root.order.add_edge(database_match,     loop_body)

# After the loop, proceed to blockchain entry and certificate issue
root.order.add_edge(loop_body,          blockchain_entry)
root.order.add_edge(blockchain_entry,   certificate_issue)

# After certificate issue, brief the client and secure storage
root.order.add_edge(certificate_issue,  client_briefing)
root.order.add_edge(client_briefing,    secure_storage)

# Finally, approve the process
root.order.add_edge(secure_storage,     final_approval)