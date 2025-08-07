import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
asset_intake      = Transition(label='Asset Intake')
provenance_check  = Transition(label='Provenance Check')
material_sampling = Transition(label='Material Sampling')
radiocarbon_test  = Transition(label='Radiocarbon Test')
style_compare     = Transition(label='Style Compare')
historical_search = Transition(label='Historical Search')
expert_consult    = Transition(label='Expert Consult')
condition_review  = Transition(label='Condition Review')
scientific_analysis = Transition(label='Scientific Analysis')
data_compilation  = Transition(label='Data Compilation')
peer_review       = Transition(label='Peer Review')
report_draft      = Transition(label='Report Draft')
certification     = Transition(label='Certification')
digital_archive   = Transition(label='Digital Archive')
client_delivery   = Transition(label='Client Delivery')

# Build the partial order model
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

# Define the control-flow dependencies
root.order.add_edge(asset_intake, provenance_check)
root.order.add_edge(asset_intake, material_sampling)

# Sampling and analysis converge before expert consult
root.order.add_edge(material_sampling, expert_consult)
root.order.add_edge(radiocarbon_test, expert_consult)
root.order.add_edge(style_compare, expert_consult)

# After expert consult, proceed to condition review
root.order.add_edge(provenance_check, condition_review)
root.order.add_edge(historical_search, condition_review)

# After condition review, proceed to scientific analysis
root.order.add_edge(condition_review, scientific_analysis)

# Analysis and compilation converge before peer review
root.order.add_edge(scientific_analysis, peer_review)
root.order.add_edge(data_compilation, peer_review)

# After peer review, generate the report draft
root.order.add_edge(peer_review, report_draft)

# The certification and digital archive can proceed in parallel from the report
root.order.add_edge(report_draft, certification)
root.order.add_edge(report_draft, digital_archive)

# Finally, deliver the results to the client
root.order.add_edge(certification, client_delivery)
root.order.add_edge(digital_archive, client_delivery)