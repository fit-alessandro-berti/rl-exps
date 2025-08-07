import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
artifact_intake = Transition(label='Artifact Intake')
provenance_check = Transition(label='Provenance Check')
material_sampling = Transition(label='Material Sampling')
scientific_test = Transition(label='Scientific Test')
expert_review = Transition(label='Expert Review')
archive_search = Transition(label='Archive Search')
legal_verify = Transition(label='Legal Verify')
ownership_confirm = Transition(label='Ownership Confirm')
compliance_audit = Transition(label='Compliance Audit')
data_documentation = Transition(label='Data Documentation')
interim_report = Transition(label='Interim Report')
department_review = Transition(label='Department Review')
consensus_meeting = Transition(label='Consensus Meeting')
final_approval = Transition(label='Final Approval')
artifact_release = Transition(label='Artifact Release')

# Define the partial order model
root = StrictPartialOrder(nodes=[
    artifact_intake,
    provenance_check,
    material_sampling,
    scientific_test,
    expert_review,
    archive_search,
    legal_verify,
    ownership_confirm,
    compliance_audit,
    data_documentation,
    interim_report,
    department_review,
    consensus_meeting,
    final_approval,
    artifact_release
])

# Add dependencies to the partial order model
root.order.add_edge(artifact_intake, provenance_check)
root.order.add_edge(artifact_intake, material_sampling)
root.order.add_edge(artifact_intake, scientific_test)
root.order.add_edge(artifact_intake, expert_review)
root.order.add_edge(artifact_intake, archive_search)
root.order.add_edge(artifact_intake, legal_verify)
root.order.add_edge(artifact_intake, ownership_confirm)
root.order.add_edge(artifact_intake, compliance_audit)
root.order.add_edge(artifact_intake, data_documentation)
root.order.add_edge(artifact_intake, interim_report)
root.order.add_edge(artifact_intake, department_review)
root.order.add_edge(artifact_intake, consensus_meeting)
root.order.add_edge(artifact_intake, final_approval)
root.order.add_edge(artifact_intake, artifact_release)

# Now 'root' contains the POWL model for the process