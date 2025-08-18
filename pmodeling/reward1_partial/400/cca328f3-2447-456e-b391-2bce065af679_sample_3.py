import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the process
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
    artifact_intake, provenance_check, material_scan, style_compare,
    digital_capture, expert_review, database_search, legal_audit,
    cultural_assess, data_synthesis, report_draft, archival_store,
    display_approve, lender_notify, investigation_flag
])

# Define the dependencies between activities
root.order.add_edge(artifact_intake, provenance_check)
root.order.add_edge(artifact_intake, material_scan)
root.order.add_edge(artifact_intake, digital_capture)
root.order.add_edge(artifact_intake, expert_review)
root.order.add_edge(provenance_check, database_search)
root.order.add_edge(material_scan, legal_audit)
root.order.add_edge(style_compare, cultural_assess)
root.order.add_edge(data_synthesis, report_draft)
root.order.add_edge(data_synthesis, archival_store)
root.order.add_edge(report_draft, display_approve)
root.order.add_edge(report_draft, lender_notify)
root.order.add_edge(report_draft, investigation_flag)

# Print the final result
print(root)