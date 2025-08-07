import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
asset_intake     = Transition(label='Asset Intake')
provenance_check = Transition(label='Provenance Check')
material_sampling= Transition(label='Material Sampling')
radiocarbon_test = Transition(label='Radiocarbon Test')
style_compare    = Transition(label='Style Compare')
historical_search= Transition(label='Historical Search')
expert_consult   = Transition(label='Expert Consult')
condition_review = Transition(label='Condition Review')
scientific_analysis = Transition(label='Scientific Analysis')
data_compilation = Transition(label='Data Compilation')
peer_review      = Transition(label='Peer Review')
report_draft     = Transition(label='Report Draft')
certification    = Transition(label='Certification')
digital_archive  = Transition(label='Digital Archive')
client_delivery  = Transition(label='Client Delivery')

# Build the analysis sub-process (A)
analysis = StrictPartialOrder(nodes=[
    material_sampling, radiocarbon_test, style_compare,
    historical_search, expert_consult, scientific_analysis,
    condition_review
])
analysis.order.add_edge(material_sampling, radiocarbon_test)
analysis.order.add_edge(material_sampling, style_compare)
analysis.order.add_edge(historical_search, expert_consult)
analysis.order.add_edge(style_compare, scientific_analysis)
analysis.order.add_edge(expert_consult, scientific_analysis)
analysis.order.add_edge(scientific_analysis, condition_review)

# Build the peer review sub-process (B)
peer = StrictPartialOrder(nodes=[data_compilation, peer_review])
peer.order.add_edge(data_compilation, peer_review)

# Build the main process (root)
root = StrictPartialOrder(nodes=[
    asset_intake, provenance_check,
    analysis, peer,
    report_draft, certification, digital_archive, client_delivery
])
root.order.add_edge(asset_intake, provenance_check)
root.order.add_edge(provenance_check, analysis)
root.order.add_edge(analysis, peer)
root.order.add_edge(peer, report_draft)
root.order.add_edge(report_draft, certification)
root.order.add_edge(certification, digital_archive)
root.order.add_edge(digital_archive, client_delivery)