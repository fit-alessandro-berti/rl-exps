import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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
forger_detect = Transition(label='Forgery Detect')
report_compilation = Transition(label='Report Compilation')
client_briefing = Transition(label='Client Briefing')
secure_storage = Transition(label='Secure Storage')
final_approval = Transition(label='Final Approval')

# Define silent transitions
skip = SilentTransition()

# Define POWL model
xor1 = OperatorPOWL(operator=Operator.XOR, children=[database_match, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[restoration_scan, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[appraiser_review, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[forger_detect, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[report_compilation, skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[client_briefing, skip])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[secure_storage, skip])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[final_approval, skip])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[certificate_issue, skip])

# Define partial order
root = StrictPartialOrder(nodes=[
    provenance_check,
    spectroscopy_test,
    carbon_dating,
    style_analysis,
    image_scanning,
    xor1,
    xor2,
    xor3,
    xor4,
    xor5,
    xor6,
    xor7,
    xor8,
    xor9
])

# Define dependencies
root.order.add_edge(provenance_check, spectroscopy_test)
root.order.add_edge(provenance_check, carbon_dating)
root.order.add_edge(provenance_check, style_analysis)
root.order.add_edge(provenance_check, image_scanning)
root.order.add_edge(spectroscopy_test, xor1)
root.order.add_edge(carbon_dating, xor1)
root.order.add_edge(style_analysis, xor1)
root.order.add_edge(image_scanning, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor1, xor3)
root.order.add_edge(xor1, xor4)
root.order.add_edge(xor1, xor5)
root.order.add_edge(xor1, xor6)
root.order.add_edge(xor1, xor7)
root.order.add_edge(xor1, xor8)
root.order.add_edge(xor1, xor9)
root.order.add_edge(xor2, blockchain_entry)
root.order.add_edge(xor3, blockchain_entry)
root.order.add_edge(xor4, blockchain_entry)
root.order.add_edge(xor5, blockchain_entry)
root.order.add_edge(xor6, blockchain_entry)
root.order.add_edge(xor7, blockchain_entry)
root.order.add_edge(xor8, blockchain_entry)
root.order.add_edge(xor9, blockchain_entry)
root.order.add_edge(blockchain_entry, certificate_issue)
root.order.add_edge(certificate_issue, final_approval)