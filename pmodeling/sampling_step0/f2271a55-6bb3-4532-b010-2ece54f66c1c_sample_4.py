import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the silent transitions
skip1 = SilentTransition()
skip2 = SilentTransition()
skip3 = SilentTransition()
skip4 = SilentTransition()
skip5 = SilentTransition()
skip6 = SilentTransition()
skip7 = SilentTransition()

# Define the exclusive choice between skip1 and provenance_check
provenance_choice = OperatorPOWL(operator=Operator.XOR, children=[skip1, provenance_check])

# Define the loop for carbon dating and style analysis
carbon_style_loop = OperatorPOWL(operator=Operator.LOOP, children=[carbon_dating, style_analysis])

# Define the exclusive choice between skip2 and image_scanning
image_choice = OperatorPOWL(operator=Operator.XOR, children=[skip2, image_scanning])

# Define the loop for restoration scan and appraisal review
restoration_appraisal_loop = OperatorPOWL(operator=Operator.LOOP, children=[restoration_scan, appraiser_review])

# Define the exclusive choice between skip3 and database_match
database_choice = OperatorPOWL(operator=Operator.XOR, children=[skip3, database_match])

# Define the loop for blockchain entry and certificate issue
blockchain_certificate_loop = OperatorPOWL(operator=Operator.LOOP, children=[blockchain_entry, certificate_issue])

# Define the exclusive choice between forgery_detect and report_compilation
report_choice = OperatorPOWL(operator=Operator.XOR, children=[forgery_detect, report_compilation])

# Define the loop for client briefing and secure storage
client_storage_loop = OperatorPOWL(operator=Operator.LOOP, children=[client_briefing, secure_storage])

# Define the exclusive choice between final_approval and skip4
final_choice = OperatorPOWL(operator=Operator.XOR, children=[final_approval, skip4])

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    provenance_choice,
    carbon_style_loop,
    image_choice,
    restoration_appraisal_loop,
    database_choice,
    blockchain_certificate_loop,
    report_choice,
    client_storage_loop,
    final_choice
])

# Add the necessary edges
root.order.add_edge(provenance_choice, carbon_style_loop)
root.order.add_edge(provenance_choice, image_choice)
root.order.add_edge(carbon_style_loop, restoration_appraisal_loop)
root.order.add_edge(image_choice, database_choice)
root.order.add_edge(database_choice, blockchain_certificate_loop)
root.order.add_edge(blockchain_certificate_loop, report_choice)
root.order.add_edge(report_choice, client_storage_loop)
root.order.add_edge(client_storage_loop, final_choice)

# Print the root POWL model
print(root)