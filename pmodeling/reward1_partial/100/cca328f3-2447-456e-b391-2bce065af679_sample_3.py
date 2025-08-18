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

# Define the control flow
artifact_intake_to_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, SilentTransition()])
provenance_to_material = OperatorPOWL(operator=Operator.XOR, children=[material_scan, SilentTransition()])
material_to_style = OperatorPOWL(operator=Operator.XOR, children=[style_compare, SilentTransition()])
digital_capture_to_cultural = OperatorPOWL(operator=Operator.XOR, children=[digital_capture, SilentTransition()])
expert_review_to_legal = OperatorPOWL(operator=Operator.XOR, children=[expert_review, SilentTransition()])
database_search_to_legal = OperatorPOWL(operator=Operator.XOR, children=[database_search, SilentTransition()])
legal_audit_to_cultural = OperatorPOWL(operator=Operator.XOR, children=[legal_audit, SilentTransition()])
cultural_assess_to_data = OperatorPOWL(operator=Operator.XOR, children=[cultural_assess, SilentTransition()])
data_synthesis_to_final = OperatorPOWL(operator=Operator.XOR, children=[report_draft, SilentTransition()])
report_draft_to_archive = OperatorPOWL(operator=Operator.XOR, children=[archival_store, SilentTransition()])
archival_store_to_display = OperatorPOWL(operator=Operator.XOR, children=[display_approve, lender_notify, investigation_flag])

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
root.order.add_edge(artifact_intake, provenance_to_material)
root.order.add_edge(provenance_to_material, material_to_style)
root.order.add_edge(material_to_style, digital_capture_to_cultural)
root.order.add_edge(digital_capture_to_cultural, expert_review_to_legal)
root.order.add_edge(expert_review_to_legal, database_search_to_legal)
root.order.add_edge(database_search_to_legal, legal_audit_to_cultural)
root.order.add_edge(legal_audit_to_cultural, cultural_assess_to_data)
root.order.add_edge(cultural_assess_to_data, data_synthesis_to_final)
root.order.add_edge(data_synthesis_to_final, report_draft_to_archive)
root.order.add_edge(report_draft_to_archive, archival_store_to_display)
root.order.add_edge(archival_store_to_display, display_approve)
root.order.add_edge(archival_store_to_display, lender_notify)
root.order.add_edge(archival_store_to_display, investigation_flag)

print(root)