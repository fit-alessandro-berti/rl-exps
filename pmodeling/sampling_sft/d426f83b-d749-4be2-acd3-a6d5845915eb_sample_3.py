import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
asset_intake      = Transition(label='Asset Intake')
provenance_check  = Transition(label='Provenance Check')
material_sampling = Transition(label='Material Sampling')
radiocarbon_test  = Transition(label='Radiocarbon Test')
historical_search = Transition(label='Historical Search')
style_compare     = Transition(label='Style Compare')
scientific_analysis = Transition(label='Scientific Analysis')
expert_consult    = Transition(label='Expert Consult')
condition_review  = Transition(label='Condition Review')
data_compilation  = Transition(label='Data Compilation')
peer_review       = Transition(label='Peer Review')
report_draft      = Transition(label='Report Draft')
certification     = Transition(label='Certification')
digital_archive   = Transition(label='Digital Archive')
client_delivery   = Transition(label='Client Delivery')

# Build the main analysis & verification partial order (A)
A = StrictPartialOrder(nodes=[
    provenance_check,
    material_sampling,
    radiocarbon_test,
    historical_search,
    style_compare,
    scientific_analysis,
    expert_consult,
    condition_review,
    data_compilation
])
# Sequential dependencies
A.order.add_edge(provenance_check,   material_sampling)
A.order.add_edge(material_sampling,  radiocarbon_test)
A.order.add_edge(material_sampling,  historical_search)
A.order.add_edge(material_sampling,  style_compare)
A.order.add_edge(radiocarbon_test,   scientific_analysis)
A.order.add_edge(historical_search,  scientific_analysis)
A.order.add_edge(style_compare,      scientific_analysis)
A.order.add_edge(scientific_analysis, expert_consult)
A.order.add_edge(expert_consult,     condition_review)
A.order.add_edge(condition_review,   data_compilation)

# Build the reporting & certification partial order (B)
B = StrictPartialOrder(nodes=[
    data_compilation,
    peer_review,
    report_draft,
    certification,
    digital_archive,
    client_delivery
])
# Sequential dependencies
B.order.add_edge(data_compilation,   peer_review)
B.order.add_edge(peer_review,        report_draft)
B.order.add_edge(report_draft,       certification)
B.order.add_edge(certification,      digital_archive)
B.order.add_edge(digital_archive,    client_delivery)

# Final loop: perform A, then either exit or do B and repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[A, B])

# Assemble the overall root partial order
root = StrictPartialOrder(nodes=[asset_intake, loop])
# Link the intake to the loop
root.order.add_edge(asset_intake, loop)