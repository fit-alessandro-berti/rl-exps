from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

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

# Construct the POWL model
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
    forgery_detect, 
    report_compilation, 
    client_briefing, 
    secure_storage, 
    final_approval
])

# Define the partial order dependencies
root.order.add_edge(provenance_check, spectroscopy_test)
root.order.add_edge(provenance_check, carbon_dating)
root.order.add_edge(provenance_check, style_analysis)
root.order.add_edge(provenance_check, image_scanning)
root.order.add_edge(provenance_check, restoration_scan)
root.order.add_edge(provenance_check, appraiser_review)
root.order.add_edge(provenance_check, database_match)
root.order.add_edge(provenance_check, blockchain_entry)
root.order.add_edge(provenance_check, certificate_issue)
root.order.add_edge(provenance_check, forgery_detect)
root.order.add_edge(provenance_check, report_compilation)
root.order.add_edge(provenance_check, client_briefing)
root.order.add_edge(provenance_check, secure_storage)
root.order.add_edge(provenance_check, final_approval)

# Add a loop node for the report compilation
report_loop = OperatorPOWL(operator=Operator.LOOP, children=[report_compilation])
root.order.add_edge(final_approval, report_loop)
root.order.add_edge(report_loop, final_approval)

# Print the POWL model
print(root)