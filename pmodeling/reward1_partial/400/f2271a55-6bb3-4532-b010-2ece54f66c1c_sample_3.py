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

# Define the control flow operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[restoration_scan, SilentTransition()])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[database_match, SilentTransition()])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[appraiser_review, SilentTransition()])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[forgery_detect, SilentTransition()])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[report_compilation, SilentTransition()])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[client_briefing, SilentTransition()])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[secure_storage, SilentTransition()])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[final_approval, SilentTransition()])

# Create the POWL model
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
    xor8
])

# Define the dependencies between activities
root.order.add_edge(provenance_check, spectroscopy_test)
root.order.add_edge(provenance_check, carbon_dating)
root.order.add_edge(provenance_check, style_analysis)
root.order.add_edge(provenance_check, image_scanning)
root.order.add_edge(spectroscopy_test, xor1)
root.order.add_edge(carbon_dating, xor2)
root.order.add_edge(style_analysis, xor3)
root.order.add_edge(image_scanning, xor4)
root.order.add_edge(xor1, xor5)
root.order.add_edge(xor2, xor6)
root.order.add_edge(xor3, xor7)
root.order.add_edge(xor4, xor8)
root.order.add_edge(xor5, blockchain_entry)
root.order.add_edge(xor6, certificate_issue)
root.order.add_edge(xor7, SecureStorage)
root.order.add_edge(xor8, final_approval)

print(root)