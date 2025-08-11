import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the silent transitions
skip = SilentTransition()

# Define the loop nodes
provenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, skip])
material_loop = OperatorPOWL(operator=Operator.LOOP, children=[material_sampling, skip])
scientific_loop = OperatorPOWL(operator=Operator.LOOP, children=[scientific_analysis, skip])

# Define the exclusive choice nodes
analysis_choice = OperatorPOWL(operator=Operator.XOR, children=[radiocarbon_test, style_compare, historical_search])
consult_choice = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, condition_review])

# Define the partial order
root = StrictPartialOrder(nodes=[asset_intake, provenance_loop, material_loop, scientific_loop, analysis_choice, consult_choice, data_compilation, peer_review, report_draft, certification, digital_archive, client_delivery])
root.order.add_edge(asset_intake, provenance_loop)
root.order.add_edge(asset_intake, material_loop)
root.order.add_edge(asset_intake, scientific_loop)
root.order.add_edge(provenance_loop, data_compilation)
root.order.add_edge(material_loop, data_compilation)
root.order.add_edge(scientific_loop, data_compilation)
root.order.add_edge(data_compilation, peer_review)
root.order.add_edge(peer_review, report_draft)
root.order.add_edge(report_draft, certification)
root.order.add_edge(certification, digital_archive)
root.order.add_edge(digital_archive, client_delivery)