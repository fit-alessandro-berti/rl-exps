import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
artifact_intake    = Transition(label='Artifact Intake')
condition_check    = Transition(label='Condition Check')
multi_spectral     = Transition(label='Multi-spectral Scan')
material_test      = Transition(label='Material Test')
database_match     = Transition(label='Database Match')
provenance_check   = Transition(label='Provenance Check')
historical_query   = Transition(label='Historical Query')
expert_review      = Transition(label='Expert Review')
lab_collaboration  = Transition(label='Lab Collaboration')
imaging_analysis   = Transition(label='Imaging Analysis')
forgery_detection  = Transition(label='Forgery Detection')
legal_drafting     = Transition(label='Legal Drafting')
certification_issue= Transition(label='Certification Issue')
client_briefing    = Transition(label='Client Briefing')
archival_update    = Transition(label='Archival Update')

# Loop for iterative historical and provenance checks
# Body A: Historical Query -> Provenance Check
body_a = StrictPartialOrder(nodes=[historical_query, provenance_check])
body_a.order.add_edge(historical_query, provenance_check)

# Body B: No-op (skip) or additional historical/provenance checks
body_b = StrictPartialOrder(nodes=[provenance_check])
# no edge => they can run in parallel

# LOOP: do body_a, then either exit or do body_b and body_a again
history_loop = OperatorPOWL(operator=Operator.LOOP, children=[body_a, body_b])

# XOR for either imaging_analysis or forgery_detection
xor = OperatorPOWL(operator=Operator.XOR, children=[imaging_analysis, forgery_detection])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    artifact_intake,
    condition_check,
    multi_spectral,
    material_test,
    history_loop,
    database_match,
    xor,
    legal_drafting,
    certification_issue,
    client_briefing,
    archival_update
])

# Sequence of activities
root.order.add_edge(artifact_intake, condition_check)
root.order.add_edge(condition_check, multi_spectral)
root.order.add_edge(condition_check, material_test)
root.order.add_edge(multi_spectral, history_loop)
root.order.add_edge(material_test, history_loop)
root.order.add_edge(history_loop, database_match)
root.order.add_edge(database_match, xor)
root.order.add_edge(xor, legal_drafting)
root.order.add_edge(legal_drafting, certification_issue)
root.order.add_edge(certification_issue, client_briefing)
root.order.add_edge(client_briefing, archival_update)