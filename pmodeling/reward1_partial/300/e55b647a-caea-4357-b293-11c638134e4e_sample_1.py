from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the process flow
artifact_intake_child = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, material_sampling, scientific_test, expert_review])
archive_search_child = OperatorPOWL(operator=Operator.LOOP, children=[archive_search, legal_verify, ownership_confirm, compliance_audit, data_documentation, interim_report])
department_review_child = OperatorPOWL(operator=Operator.LOOP, children=[department_review, consensus_meeting, final_approval])
artifact_release_child = OperatorPOWL(operator=Operator.LOOP, children=[artifact_release])

# Create the root process
root = StrictPartialOrder(nodes=[artifact_intake_child, archive_search_child, department_review_child, artifact_release_child])
root.order.add_edge(artifact_intake_child, archive_search_child)
root.order.add_edge(archive_search_child, department_review_child)
root.order.add_edge(department_review_child, artifact_release_child)

# Print the root process
print(root)