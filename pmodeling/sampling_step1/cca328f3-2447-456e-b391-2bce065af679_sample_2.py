from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
artifact_intake = Transition(label='Artifact Intake')
provenance_check = Transition(label='Provenance Check')
material_scan = Transition(label='Material Scan')
style_compare = Transition(label='Style Compare')
digital_capture = Transition(label='Digital Capture')
expert_review = Transition(label='Expert Review')
database_search = Transition(label='Database Search')
legal_audit = Transition(label='Legal Audit')
cultural_assess = Transition(label='Cultural Assess')
data_synthesis = Transition(label='Data Synthesis')
report_draft = Transition(label='Report Draft')
archival_store = Transition(label='Archival Store')
display_approve = Transition(label='Display Approve')
lender_notify = Transition(label='Lender Notify')
investigation_flag = Transition(label='Investigation Flag')

# Define the partial order
root = StrictPartialOrder(nodes=[
    artifact_intake,
    provenance_check,
    material_scan,
    style_compare,
    digital_capture,
    expert_review,
    database_search,
    legal_audit,
    cultural_assess,
    data_synthesis,
    report_draft,
    archival_store,
    display_approve,
    lender_notify,
    investigation_flag
])

# Define the order dependencies
root.order.add_edge(artifact_intake, provenance_check)
root.order.add_edge(artifact_intake, material_scan)
root.order.add_edge(artifact_intake, digital_capture)
root.order.add_edge(provenance_check, style_compare)
root.order.add_edge(material_scan, style_compare)
root.order.add_edge(digital_capture, style_compare)
root.order.add_edge(style_compare, expert_review)
root.order.add_edge(expert_review, database_search)
root.order.add_edge(database_search, legal_audit)
root.order.add_edge(legal_audit, cultural_assess)
root.order.add_edge(cultural_assess, data_synthesis)
root.order.add_edge(data_synthesis, report_draft)
root.order.add_edge(report_draft, archival_store)
root.order.add_edge(archival_store, display_approve)
root.order.add_edge(archival_store, lender_notify)
root.order.add_edge(archival_store, investigation_flag)

# Print the final result
print(root)