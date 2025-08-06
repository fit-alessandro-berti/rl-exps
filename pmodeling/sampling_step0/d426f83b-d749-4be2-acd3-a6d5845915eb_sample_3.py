import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) in the POWL model
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
skip1 = SilentTransition()
skip2 = SilentTransition()
skip3 = SilentTransition()

# Define the XOR operator for the peer review step
xor = OperatorPOWL(operator=Operator.XOR, children=[peer_review, skip1])

# Define the exclusive choice operator for the scientific analysis step
xor2 = OperatorPOWL(operator=Operator.XOR, children=[scientific_analysis, skip2])

# Define the exclusive choice operator for the material sampling step
xor3 = OperatorPOWL(operator=Operator.XOR, children=[material_sampling, skip3])

# Define the loop operator for the provenance check step
loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, xor3])

# Define the loop operator for the style compare step
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[style_compare, xor2])

# Define the strict partial order for the entire process
root = StrictPartialOrder(nodes=[asset_intake, loop, loop2, xor, data_compilation, report_draft, certification, digital_archive, client_delivery])

# Define the dependencies between the nodes
root.order.add_edge(asset_intake, loop)
root.order.add_edge(loop, loop2)
root.order.add_edge(loop2, xor)
root.order.add_edge(xor, data_compilation)
root.order.add_edge(data_compilation, report_draft)
root.order.add_edge(report_draft, certification)
root.order.add_edge(certification, digital_archive)
root.order.add_edge(digital_archive, client_delivery)

# Print the POWL model
print(root)