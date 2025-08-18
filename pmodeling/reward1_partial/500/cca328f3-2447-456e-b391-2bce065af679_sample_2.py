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

# Define the workflow
root = StrictPartialOrder(
    nodes=[
        artifact_intake, provenance_check, material_scan, style_compare,
        digital_capture, expert_review, database_search, legal_audit,
        cultural_assess, data_synthesis, report_draft, archival_store,
        display_approve, lender_notify, investigation_flag
    ],
    order={
        artifact_intake: [provenance_check],
        provenance_check: [material_scan, style_compare],
        material_scan: [digital_capture],
        style_compare: [expert_review],
        digital_capture: [database_search, legal_audit],
        expert_review: [database_search, legal_audit],
        database_search: [cultural_assess, data_synthesis],
        legal_audit: [cultural_assess, data_synthesis],
        cultural_assess: [data_synthesis],
        data_synthesis: [report_draft],
        report_draft: [archival_store, display_approve, lender_notify, investigation_flag]
    }
)

print(root)