import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
intake = Transition(label='Asset Intake')
provenance = Transition(label='Provenance Check')
sampling = Transition(label='Material Sampling')
radiocarbon = Transition(label='Radiocarbon Test')
style_compare = Transition(label='Style Compare')
historical = Transition(label='Historical Search')
expert = Transition(label='Expert Consult')
condition = Transition(label='Condition Review')
analysis = Transition(label='Scientific Analysis')
data_compilation = Transition(label='Data Compilation')
peer_review = Transition(label='Peer Review')
report_draft = Transition(label='Report Draft')
certification = Transition(label='Certification')
digital_archive = Transition(label='Digital Archive')
client_delivery = Transition(label='Client Delivery')

# Define the partial order
root = StrictPartialOrder(nodes=[intake, provenance, sampling, radiocarbon, style_compare, historical, expert, condition, analysis, data_compilation, peer_review, report_draft, certification, digital_archive, client_delivery])

# Define the dependencies between the activities
root.order.add_edge(intake, provenance)
root.order.add_edge(provenance, sampling)
root.order.add_edge(sampling, radiocarbon)
root.order.add_edge(radiocarbon, style_compare)
root.order.add_edge(style_compare, historical)
root.order.add_edge(historical, expert)
root.order.add_edge(expert, condition)
root.order.add_edge(condition, analysis)
root.order.add_edge(analysis, data_compilation)
root.order.add_edge(data_compilation, peer_review)
root.order.add_edge(peer_review, report_draft)
root.order.add_edge(report_draft, certification)
root.order.add_edge(certification, digital_archive)
root.order.add_edge(digital_archive, client_delivery)

# Print the root model
print(root)