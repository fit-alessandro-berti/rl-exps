import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

provenance_check_loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check])
spectroscopy_test_loop = OperatorPOWL(operator=Operator.LOOP, children=[spectroscopy_test])
carbon_dating_loop = OperatorPOWL(operator=Operator.LOOP, children=[carbon_dating])
style_analysis_loop = OperatorPOWL(operator=Operator.LOOP, children=[style_analysis])
image_scanning_loop = OperatorPOWL(operator=Operator.LOOP, children=[image_scanning])
restoration_scan_loop = OperatorPOWL(operator=Operator.LOOP, children=[restoration_scan])
appraiser_review_loop = OperatorPOWL(operator=Operator.LOOP, children=[appraiser_review])
database_match_loop = OperatorPOWL(operator=Operator.LOOP, children=[database_match])

xor1 = OperatorPOWL(operator=Operator.XOR, children=[blockchain_entry, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[certificate_issue, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[forgery_detect, skip])

xor4 = OperatorPOWL(operator=Operator.XOR, children=[report_compilation, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[client_briefing, skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[secure_storage, skip])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[final_approval, skip])

root = StrictPartialOrder(nodes=[
    provenance_check_loop,
    spectroscopy_test_loop,
    carbon_dating_loop,
    style_analysis_loop,
    image_scanning_loop,
    restoration_scan_loop,
    appraiser_review_loop,
    database_match_loop,
    xor1,
    xor2,
    xor3,
    xor4,
    xor5,
    xor6,
    xor7
])

root.order.add_edge(provenance_check_loop, spectroscopy_test_loop)
root.order.add_edge(provenance_check_loop, carbon_dating_loop)
root.order.add_edge(provenance_check_loop, style_analysis_loop)
root.order.add_edge(provenance_check_loop, image_scanning_loop)
root.order.add_edge(provenance_check_loop, restoration_scan_loop)
root.order.add_edge(provenance_check_loop, appraiser_review_loop)
root.order.add_edge(provenance_check_loop, database_match_loop)

root.order.add_edge(spectroscopy_test_loop, xor1)
root.order.add_edge(carbon_dating_loop, xor2)
root.order.add_edge(style_analysis_loop, xor3)
root.order.add_edge(image_scanning_loop, xor4)
root.order.add_edge(restoration_scan_loop, xor5)
root.order.add_edge(appraiser_review_loop, xor6)
root.order.add_edge(database_match_loop, xor7)