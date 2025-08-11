import pm4py
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

# Define the process
artifact_intake_to_provenance_check = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, provenance_check])
provenance_check_to_material_sampling = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, material_sampling])
material_sampling_to_scientific_test = OperatorPOWL(operator=Operator.XOR, children=[material_sampling, scientific_test])
scientific_test_to_expert_review = OperatorPOWL(operator=Operator.XOR, children=[scientific_test, expert_review])
expert_review_to_archive_search = OperatorPOWL(operator=Operator.XOR, children=[expert_review, archive_search])
archive_search_to_legal_verify = OperatorPOWL(operator=Operator.XOR, children=[archive_search, legal_verify])
legal_verify_to_ownership_confirm = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, ownership_confirm])
ownership_confirm_to_compliance_audit = OperatorPOWL(operator=Operator.XOR, children=[ownership_confirm, compliance_audit])
compliance_audit_to_data_documentation = OperatorPOWL(operator=Operator.XOR, children=[compliance_audit, data_documentation])
data_documentation_to_interim_report = OperatorPOWL(operator=Operator.XOR, children=[data_documentation, interim_report])
interim_report_to_department_review = OperatorPOWL(operator=Operator.XOR, children=[interim_report, department_review])
department_review_to_consensus_meeting = OperatorPOWL(operator=Operator.XOR, children=[department_review, consensus_meeting])
consensus_meeting_to_final_approval = OperatorPOWL(operator=Operator.XOR, children=[consensus_meeting, final_approval])
final_approval_to_artifact_release = OperatorPOWL(operator=Operator.XOR, children=[final_approval, artifact_release])

# Define the order
root = StrictPartialOrder(nodes=[artifact_intake_to_provenance_check, provenance_check_to_material_sampling, material_sampling_to_scientific_test, scientific_test_to_expert_review, expert_review_to_archive_search, archive_search_to_legal_verify, legal_verify_to_ownership_confirm, ownership_confirm_to_compliance_audit, compliance_audit_to_data_documentation, data_documentation_to_interim_report, interim_report_to_department_review, department_review_to_consensus_meeting, consensus_meeting_to_final_approval, final_approval_to_artifact_release])

# Add edges
root.order.add_edge(artifact_intake_to_provenance_check, provenance_check_to_material_sampling)
root.order.add_edge(provenance_check_to_material_sampling, material_sampling_to_scientific_test)
root.order.add_edge(material_sampling_to_scientific_test, scientific_test_to_expert_review)
root.order.add_edge(scientific_test_to_expert_review, expert_review_to_archive_search)
root.order.add_edge(expert_review_to_archive_search, archive_search_to_legal_verify)
root.order.add_edge(archive_search_to_legal_verify, legal_verify_to_ownership_confirm)
root.order.add_edge(legal_verify_to_ownership_confirm, ownership_confirm_to_compliance_audit)
root.order.add_edge(ownership_confirm_to_compliance_audit, compliance_audit_to_data_documentation)
root.order.add_edge(compliance_audit_to_data_documentation, data_documentation_to_interim_report)
root.order.add_edge(data_documentation_to_interim_report, interim_report_to_department_review)
root.order.add_edge(interim_report_to_department_review, department_review_to_consensus_meeting)
root.order.add_edge(department_review_to_consensus_meeting, consensus_meeting_to_final_approval)
root.order.add_edge(consensus_meeting_to_final_approval, final_approval_to_artifact_release)

print(root)