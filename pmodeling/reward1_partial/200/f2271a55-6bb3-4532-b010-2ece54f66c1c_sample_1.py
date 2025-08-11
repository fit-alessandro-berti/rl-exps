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
forger_detect = Transition(label='Forgery Detect')
report_compilation = Transition(label='Report Compilation')
client_briefing = Transition(label='Client Briefing')
secure_storage = Transition(label='Secure Storage')
final_approval = Transition(label='Final Approval')

skip = SilentTransition()

provenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check])
spectroscopy_choice = OperatorPOWL(operator=Operator.XOR, children=[spectroscopy_test, skip])
carbon_choice = OperatorPOWL(operator=Operator.XOR, children=[carbon_dating, skip])
style_choice = OperatorPOWL(operator=Operator.XOR, children=[style_analysis, skip])
image_choice = OperatorPOWL(operator=Operator.XOR, children=[image_scanning, skip])
restoration_choice = OperatorPOWL(operator=Operator.XOR, children=[restoration_scan, skip])
appraiser_choice = OperatorPOWL(operator=Operator.XOR, children=[appraiser_review, skip])
database_choice = OperatorPOWL(operator=Operator.XOR, children=[database_match, skip])
blockchain_choice = OperatorPOWL(operator=Operator.XOR, children=[blockchain_entry, skip])
certificate_choice = OperatorPOWL(operator=Operator.XOR, children=[certificate_issue, skip])
forger_choice = OperatorPOWL(operator=Operator.XOR, children=[forger_detect, skip])
report_choice = OperatorPOWL(operator=Operator.XOR, children=[report_compilation, skip])
client_choice = OperatorPOWL(operator=Operator.XOR, children=[client_briefing, skip])
storage_choice = OperatorPOWL(operator=Operator.XOR, children=[secure_storage, skip])
final_choice = OperatorPOWL(operator=Operator.XOR, children=[final_approval, skip])

root = StrictPartialOrder(nodes=[
    provenance_loop,
    spectroscopy_choice,
    carbon_choice,
    style_choice,
    image_choice,
    restoration_choice,
    appraiser_choice,
    database_choice,
    blockchain_choice,
    certificate_choice,
    forger_choice,
    report_choice,
    client_choice,
    storage_choice,
    final_choice
])

root.order.add_edge(provenance_loop, spectroscopy_choice)
root.order.add_edge(provenance_loop, carbon_choice)
root.order.add_edge(provenance_loop, style_choice)
root.order.add_edge(provenance_loop, image_choice)
root.order.add_edge(provenance_loop, restoration_choice)
root.order.add_edge(provenance_loop, appraiser_choice)
root.order.add_edge(provenance_loop, database_choice)
root.order.add_edge(provenance_loop, blockchain_choice)
root.order.add_edge(provenance_loop, certificate_choice)
root.order.add_edge(provenance_loop, forger_choice)
root.order.add_edge(provenance_loop, report_choice)
root.order.add_edge(provenance_loop, client_choice)
root.order.add_edge(provenance_loop, storage_choice)
root.order.add_edge(provenance_loop, final_choice)