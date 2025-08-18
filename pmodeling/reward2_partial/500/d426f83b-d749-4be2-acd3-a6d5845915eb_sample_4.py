import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
intake = Transition(label='Asset Intake')
check = Transition(label='Provenance Check')
sampling = Transition(label='Material Sampling')
radiocarbon = Transition(label='Radiocarbon Test')
style_compare = Transition(label='Style Compare')
historical_search = Transition(label='Historical Search')
consult = Transition(label='Expert Consult')
review = Transition(label='Condition Review')
analysis = Transition(label='Scientific Analysis')
compilation = Transition(label='Data Compilation')
peer_review = Transition(label='Peer Review')
report_draft = Transition(label='Report Draft')
certification = Transition(label='Certification')
archive = Transition(label='Digital Archive')
delivery = Transition(label='Client Delivery')

# Define the partial order
root = StrictPartialOrder(nodes=[intake, check, sampling, radiocarbon, style_compare, historical_search, consult, review, analysis, compilation, peer_review, report_draft, certification, archive, delivery])

# Define the dependencies
root.order.add_edge(intake, check)
root.order.add_edge(check, sampling)
root.order.add_edge(sampling, radiocarbon)
root.order.add_edge(radiocarbon, style_compare)
root.order.add_edge(style_compare, historical_search)
root.order.add_edge(historical_search, consult)
root.order.add_edge(consult, review)
root.order.add_edge(review, analysis)
root.order.add_edge(analysis, compilation)
root.order.add_edge(compilation, peer_review)
root.order.add_edge(peer_review, report_draft)
root.order.add_edge(report_draft, certification)
root.order.add_edge(certification, archive)
root.order.add_edge(archive, delivery)

# Print the root
print(root)