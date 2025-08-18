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

# Define the partial order structure
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, material_sampling, radiocarbon_test, style_compare, historical_search, expert_consult, condition_review, scientific_analysis])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[data_compilation, peer_review])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[report_draft, certification, digital_archive, client_delivery])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[loop1, xor1, loop2])

root = StrictPartialOrder(nodes=[xor2])
root.order.add_edge(loop1, xor1)
root.order.add_edge(xor1, loop2)
root.order.add_edge(loop2, xor2)

# Print the root POWL model
print(root)