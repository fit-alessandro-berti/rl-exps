import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
artifact_intake     = Transition(label='Artifact Intake')
provenance_check    = Transition(label='Provenance Check')
material_scan       = Transition(label='Material Scan')
style_compare       = Transition(label='Style Compare')
digital_capture     = Transition(label='Digital Capture')
database_search     = Transition(label='Database Search')
expert_review       = Transition(label='Expert Review')
cultural_assess     = Transition(label='Cultural Assess')
legal_audit         = Transition(label='Legal Audit')
data_synthesis      = Transition(label='Data Synthesis')
report_draft        = Transition(label='Report Draft')
archival_store      = Transition(label='Archival Store')
display_approve     = Transition(label='Display Approve')
lender_notify       = Transition(label='Lender Notify')
investigation_flag  = Transition(label='Investigation Flag')

# Build the loop body: Data Synthesis -> Report Draft -> Archive Store
body = StrictPartialOrder(nodes=[data_synthesis, report_draft, archival_store])
body.order.add_edge(data_synthesis, report_draft)
body.order.add_edge(report_draft, archival_store)

# LOOP: after initial intake, do provenance check, then either exit or do the loop body and repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, body])

# Build the top-level partial order
root = StrictPartialOrder(nodes=[
    artifact_intake, loop,
    digital_capture, database_search, expert_review, cultural_assess, legal_audit,
    report_draft, archival_store,
    display_approve, lender_notify, investigation_flag
])

# Add dependencies: after intake, do provenance check first, then material scan, style compare, digital capture
root.order.add_edge(artifact_intake, loop)

# After the provenance loop, do material scan, style compare, and digital capture in parallel
for act in [material_scan, style_compare, digital_capture]:
    root.order.add_edge(loop, act)

# After the digital capture, do the rest of the loop body
for act in [database_search, expert_review, cultural_assess, legal_audit]:
    root.order.add_edge(digital_capture, act)

# After the final synthesis, either approve for display or notify lender or flag for investigation
for target in [display_approve, lender_notify, investigation_flag]:
    root.order.add_edge(report_draft, target)