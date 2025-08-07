import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define the POWL model
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

# Since there are no explicit dependencies in the provided process description, we don't need to define any edges.

# Print the root of the POWL model
print(root)