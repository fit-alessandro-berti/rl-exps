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

# Define the process steps
artifact_intake_node = OperatorPOWL(operator=Operator.SILENT, children=[artifact_intake])
provenance_check_node = OperatorPOWL(operator=Operator.SILENT, children=[provenance_check])
material_sampling_node = OperatorPOWL(operator=Operator.SILENT, children=[material_sampling])
scientific_test_node = OperatorPOWL(operator=Operator.SILENT, children=[scientific_test])
expert_review_node = OperatorPOWL(operator=Operator.SILENT, children=[expert_review])
archive_search_node = OperatorPOWL(operator=Operator.SILENT, children=[archive_search])
legal_verify_node = OperatorPOWL(operator=Operator.SILENT, children=[legal_verify])
ownership_confirm_node = OperatorPOWL(operator=Operator.SILENT, children=[ownership_confirm])
compliance_audit_node = OperatorPOWL(operator=Operator.SILENT, children=[compliance_audit])
data_documentation_node = OperatorPOWL(operator=Operator.SILENT, children=[data_documentation])
interim_report_node = OperatorPOWL(operator=Operator.SILENT, children=[interim_report])
department_review_node = OperatorPOWL(operator=Operator.SILENT, children=[department_review])
consensus_meeting_node = OperatorPOWL(operator=Operator.SILENT, children=[consensus_meeting])
final_approval_node = OperatorPOWL(operator=Operator.SILENT, children=[final_approval])
artifact_release_node = OperatorPOWL(operator=Operator.SILENT, children=[artifact_release])

# Define the partial order
root = StrictPartialOrder(nodes=[
    artifact_intake_node,
    provenance_check_node,
    material_sampling_node,
    scientific_test_node,
    expert_review_node,
    archive_search_node,
    legal_verify_node,
    ownership_confirm_node,
    compliance_audit_node,
    data_documentation_node,
    interim_report_node,
    department_review_node,
    consensus_meeting_node,
    final_approval_node,
    artifact_release_node
])

# Add dependencies between nodes
root.order.add_edge(artifact_intake_node, provenance_check_node)
root.order.add_edge(artifact_intake_node, material_sampling_node)
root.order.add_edge(material_sampling_node, scientific_test_node)
root.order.add_edge(provenance_check_node, expert_review_node)
root.order.add_edge(material_sampling_node, expert_review_node)
root.order.add_edge(scientific_test_node, archive_search_node)
root.order.add_edge(expert_review_node, archive_search_node)
root.order.add_edge(archive_search_node, legal_verify_node)
root.order.add_edge(legal_verify_node, ownership_confirm_node)
root.order.add_edge(ownership_confirm_node, compliance_audit_node)
root.order.add_edge(compliance_audit_node, data_documentation_node)
root.order.add_edge(data_documentation_node, interim_report_node)
root.order.add_edge(interim_report_node, department_review_node)
root.order.add_edge(department_review_node, consensus_meeting_node)
root.order.add_edge(consensus_meeting_node, final_approval_node)
root.order.add_edge(final_approval_node, artifact_release_node)

print(root)