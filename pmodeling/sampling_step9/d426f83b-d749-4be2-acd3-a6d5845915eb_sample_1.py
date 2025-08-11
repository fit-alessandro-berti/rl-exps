import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

asset_intake = Transition(label='Asset Intake')
provenance_check = Transition(label='Provenance Check')
material_sampling = Transition(label='Material Sampling')
radiocarbon_test = Transition(label='Radiocarbon Test')
style_compare = Transition(label='Style Compare')
historical_search = Transition(label='Historical Search')
expert_consult = Transition(label='Expert Consult')
condition_review = Transition(label='Condition Review')
scientific_analysis = Transition(label='Scientific Analysis')
data_compilation = Transition(label='Data Compilation')
peer_review = Transition(label='Peer Review')
report_draft = Transition(label='Report Draft')
certification = Transition(label='Certification')
digital_archive = Transition(label='Digital Archive')
client_delivery = Transition(label='Client Delivery')

skip = SilentTransition()

provenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[historical_search, expert_consult, style_compare])
material_loop = OperatorPOWL(operator=Operator.LOOP, children=[material_sampling, radiocarbon_test])
scientific_loop = OperatorPOWL(operator=Operator.LOOP, children=[scientific_analysis, data_compilation])
peer_review_loop = OperatorPOWL(operator=Operator.LOOP, children=[peer_review, report_draft])

loop_1 = OperatorPOWL(operator=Operator.XOR, children=[provenance_loop, skip])
loop_2 = OperatorPOWL(operator=Operator.XOR, children=[material_loop, skip])
loop_3 = OperatorPOWL(operator=Operator.XOR, children=[scientific_loop, skip])
loop_4 = OperatorPOWL(operator=Operator.XOR, children=[peer_review_loop, skip])

root = StrictPartialOrder(nodes=[asset_intake, loop_1, loop_2, loop_3, loop_4, certification, digital_archive, client_delivery])
root.order.add_edge(asset_intake, loop_1)
root.order.add_edge(asset_intake, loop_2)
root.order.add_edge(asset_intake, loop_3)
root.order.add_edge(asset_intake, loop_4)
root.order.add_edge(loop_1, certification)
root.order.add_edge(loop_2, certification)
root.order.add_edge(loop_3, certification)
root.order.add_edge(loop_4, certification)
root.order.add_edge(certification, digital_archive)
root.order.add_edge(digital_archive, client_delivery)