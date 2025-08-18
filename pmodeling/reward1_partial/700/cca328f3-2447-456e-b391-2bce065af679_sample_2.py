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

# Define the POWL model structure
root = StrictPartialOrder(
    nodes=[
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
    ],
    order=[
        (artifact_intake, provenance_check),
        (artifact_intake, material_scan),
        (artifact_intake, style_compare),
        (artifact_intake, digital_capture),
        (artifact_intake, expert_review),
        (artifact_intake, database_search),
        (artifact_intake, legal_audit),
        (artifact_intake, cultural_assess),
        (artifact_intake, data_synthesis),
        (artifact_intake, report_draft),
        (artifact_intake, archival_store),
        (artifact_intake, display_approve),
        (artifact_intake, lender_notify),
        (artifact_intake, investigation_flag)
    ]
)

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

# Print the root of the POWL model
print(root)