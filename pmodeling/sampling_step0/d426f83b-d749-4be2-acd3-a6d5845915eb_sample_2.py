import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define silent transitions
skip = SilentTransition()

# Define loops
provenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[historical_search, expert_consult, condition_review, scientific_analysis, data_compilation, peer_review])
radiocarbon_loop = OperatorPOWL(operator=Operator.LOOP, children=[radiocarbon_test])

# Define exclusive choices
material_choice = OperatorPOWL(operator=Operator.XOR, children=[material_sampling, skip])
style_choice = OperatorPOWL(operator=Operator.XOR, children=[style_compare, skip])

# Define the root partial order
root = StrictPartialOrder(nodes=[asset_intake, provenance_loop, material_choice, style_choice, report_draft, certification, digital_archive, client_delivery])
root.order.add_edge(asset_intake, provenance_loop)
root.order.add_edge(asset_intake, material_choice)
root.order.add_edge(asset_intake, style_choice)
root.order.add_edge(provenance_loop, report_draft)
root.order.add_edge(material_choice, report_draft)
root.order.add_edge(style_choice, report_draft)
root.order.add_edge(report_draft, certification)
root.order.add_edge(certification, digital_archive)
root.order.add_edge(digital_archive, client_delivery)