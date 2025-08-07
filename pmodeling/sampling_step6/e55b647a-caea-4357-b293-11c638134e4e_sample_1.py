import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Add dependencies if necessary
# Example: Add dependency from 'Material Sampling' to 'Scientific Test'
# root.order.add_edge(material_sampling, scientific_test)

# Add dependencies from 'Provenance Check' to 'Archive Search'
root.order.add_edge(provenance_check, archive_search)

# Add dependencies from 'Legal Verify' to 'Ownership Confirm'
root.order.add_edge(legal_verify, ownership_confirm)

# Add dependencies from 'Compliance Audit' to 'Interim Report'
root.order.add_edge(compliance_audit, interim_report)

# Add dependencies from 'Department Review' to 'Consensus Meeting'
root.order.add_edge(department_review, consensus_meeting)

# Add dependencies from 'Consensus Meeting' to 'Final Approval'
root.order.add_edge(consensus_meeting, final_approval)

# Add dependencies from 'Final Approval' to 'Artifact Release'
root.order.add_edge(final_approval, artifact_release)

# Print the root to see the model
print(root)