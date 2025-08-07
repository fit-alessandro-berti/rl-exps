import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
asset_intake    = Transition(label='Asset Intake')
provenance_check= Transition(label='Provenance Check')
material_sampling= Transition(label='Material Sampling')
radiocarbon_test= Transition(label='Radiocarbon Test')
historical_search= Transition(label='Historical Search')
style_compare   = Transition(label='Style Compare')
expert_consult   = Transition(label='Expert Consult')
condition_review= Transition(label='Condition Review')
scientific_analysis= Transition(label='Scientific Analysis')
data_compilation= Transition(label='Data Compilation')
peer_review     = Transition(label='Peer Review')
report_draft    = Transition(label='Report Draft')
certification   = Transition(label='Certification')
digital_archive = Transition(label='Digital Archive')
client_delivery = Transition(label='Client Delivery')

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    asset_intake,
    provenance_check,
    material_sampling,
    radiocarbon_test,
    historical_search,
    style_compare,
    expert_consult,
    condition_review,
    scientific_analysis,
    data_compilation,
    peer_review,
    report_draft,
    certification,
    digital_archive,
    client_delivery
])

# Sequence of activities before peer review
root.order.add_edge(asset_intake,     provenance_check)
root.order.add_edge(provenance_check, material_sampling)
root.order.add_edge(material_sampling, radiocarbon_test)
root.order.add_edge(radiocarbon_test, historical_search)
root.order.add_edge(historical_search, style_compare)
root.order.add_edge(style_compare, expert_consult)
root.order.add_edge(expert_consult, condition_review)
root.order.add_edge(condition_review, scientific_analysis)
root.order.add_edge(scientific_analysis, data_compilation)

# Loop for peer review and report drafting: do peer_review, then optionally report_draft and repeat
loop_body = StrictPartialOrder(nodes=[peer_review, report_draft])
loop_body.order.add_edge(peer_review, report_draft)
loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body])

# Sequence after peer review loop
root.order.add_edge(data_compilation, loop)
root.order.add_edge(loop, certification)
root.order.add_edge(certification, digital_archive)
root.order.add_edge(digital_archive, client_delivery)