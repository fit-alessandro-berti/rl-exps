import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the partial order
root = StrictPartialOrder(nodes=[
    asset_intake,
    provenance_check,
    material_sampling,
    radiocarbon_test,
    style_compare,
    historical_search,
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

# Define the dependencies between activities
root.order.add_edge(asset_intake, provenance_check)
root.order.add_edge(asset_intake, material_sampling)
root.order.add_edge(asset_intake, radiocarbon_test)
root.order.add_edge(asset_intake, style_compare)
root.order.add_edge(asset_intake, historical_search)
root.order.add_edge(asset_intake, expert_consult)
root.order.add_edge(asset_intake, condition_review)
root.order.add_edge(asset_intake, scientific_analysis)
root.order.add_edge(asset_intake, data_compilation)
root.order.add_edge(asset_intake, peer_review)
root.order.add_edge(asset_intake, report_draft)
root.order.add_edge(asset_intake, certification)
root.order.add_edge(asset_intake, digital_archive)
root.order.add_edge(asset_intake, client_delivery)

# The 'root' variable now contains the POWL model for the process.