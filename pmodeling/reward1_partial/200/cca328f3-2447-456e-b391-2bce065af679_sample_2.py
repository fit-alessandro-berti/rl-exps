from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Add dependencies between nodes
root.order.add_edge(artifact_intake, provenance_check)
root.order.add_edge(artifact_intake, material_scan)
root.order.add_edge(artifact_intake, style_compare)
root.order.add_edge(artifact_intake, digital_capture)
root.order.add_edge(artifact_intake, expert_review)
root.order.add_edge(artifact_intake, database_search)
root.order.add_edge(artifact_intake, legal_audit)
root.order.add_edge(artifact_intake, cultural_assess)
root.order.add_edge(artifact_intake, data_synthesis)
root.order.add_edge(artifact_intake, report_draft)
root.order.add_edge(artifact_intake, archival_store)
root.order.add_edge(artifact_intake, display_approve)
root.order.add_edge(artifact_intake, lender_notify)
root.order.add_edge(artifact_intake, investigation_flag)

root.order.add_edge(provenance_check, material_scan)
root.order.add_edge(provenance_check, style_compare)
root.order.add_edge(provenance_check, digital_capture)
root.order.add_edge(provenance_check, expert_review)
root.order.add_edge(provenance_check, database_search)
root.order.add_edge(provenance_check, legal_audit)
root.order.add_edge(provenance_check, cultural_assess)
root.order.add_edge(provenance_check, data_synthesis)
root.order.add_edge(provenance_check, report_draft)
root.order.add_edge(provenance_check, archival_store)
root.order.add_edge(provenance_check, display_approve)
root.order.add_edge(provenance_check, lender_notify)
root.order.add_edge(provenance_check, investigation_flag)

root.order.add_edge(material_scan, style_compare)
root.order.add_edge(material_scan, digital_capture)
root.order.add_edge(material_scan, expert_review)
root.order.add_edge(material_scan, database_search)
root.order.add_edge(material_scan, legal_audit)
root.order.add_edge(material_scan, cultural_assess)
root.order.add_edge(material_scan, data_synthesis)
root.order.add_edge(material_scan, report_draft)
root.order.add_edge(material_scan, archival_store)
root.order.add_edge(material_scan, display_approve)
root.order.add_edge(material_scan, lender_notify)
root.order.add_edge(material_scan, investigation_flag)

root.order.add_edge(style_compare, digital_capture)
root.order.add_edge(style_compare, expert_review)
root.order.add_edge(style_compare, database_search)
root.order.add_edge(style_compare, legal_audit)
root.order.add_edge(style_compare, cultural_assess)
root.order.add_edge(style_compare, data_synthesis)
root.order.add_edge(style_compare, report_draft)
root.order.add_edge(style_compare, archival_store)
root.order.add_edge(style_compare, display_approve)
root.order.add_edge(style_compare, lender_notify)
root.order.add_edge(style_compare, investigation_flag)

root.order.add_edge(digital_capture, expert_review)
root.order.add_edge(digital_capture, database_search)
root.order.add_edge(digital_capture, legal_audit)
root.order.add_edge(digital_capture, cultural_assess)
root.order.add_edge(digital_capture, data_synthesis)
root.order.add_edge(digital_capture, report_draft)
root.order.add_edge(digital_capture, archival_store)
root.order.add_edge(digital_capture, display_approve)
root.order.add_edge(digital_capture, lender_notify)
root.order.add_edge(digital_capture, investigation_flag)

root.order.add_edge(expert_review, database_search)
root.order.add_edge(expert_review, legal_audit)
root.order.add_edge(expert_review, cultural_assess)
root.order.add_edge(expert_review, data_synthesis)
root.order.add_edge(expert_review, report_draft)
root.order.add_edge(expert_review, archival_store)
root.order.add_edge(expert_review, display_approve)
root.order.add_edge(expert_review, lender_notify)
root.order.add_edge(expert_review, investigation_flag)

root.order.add_edge(database_search, legal_audit)
root.order.add_edge(database_search, cultural_assess)
root.order.add_edge(database_search, data_synthesis)
root.order.add_edge(database_search, report_draft)
root.order.add_edge(database_search, archival_store)
root.order.add_edge(database_search, display_approve)
root.order.add_edge(database_search, lender_notify)
root.order.add_edge(database_search, investigation_flag)

root.order.add_edge(legal_audit, cultural_assess)
root.order.add_edge(legal_audit, data_synthesis)
root.order.add_edge(legal_audit, report_draft)
root.order.add_edge(legal_audit, archival_store)
root.order.add_edge(legal_audit, display_approve)
root.order.add_edge(legal_audit, lender_notify)
root.order.add_edge(legal_audit, investigation_flag)

root.order.add_edge(cultural_assess, data_synthesis)
root.order.add_edge(cultural_assess, report_draft)
root.order.add_edge(cultural_assess, archival_store)
root.order.add_edge(cultural_assess, display_approve)
root.order.add_edge(cultural_assess, lender_notify)
root.order.add_edge(cultural_assess, investigation_flag)

root.order.add_edge(data_synthesis, report_draft)
root.order.add_edge(data_synthesis, archival_store)
root.order.add_edge(data_synthesis, display_approve)
root.order.add_edge(data_synthesis, lender_notify)
root.order.add_edge(data_synthesis, investigation_flag)

root.order.add_edge(report_draft, archival_store)
root.order.add_edge(report_draft, display_approve)
root.order.add_edge(report_draft, lender_notify)
root.order.add_edge(report_draft, investigation_flag)

root.order.add_edge(archival_store, display_approve)
root.order.add_edge(archival_store, lender_notify)
root.order.add_edge(archival_store, investigation_flag)

root.order.add_edge(display_approve, lender_notify)
root.order.add_edge(display_approve, investigation_flag)

root.order.add_edge(lender_notify, investigation_flag)

print(root)