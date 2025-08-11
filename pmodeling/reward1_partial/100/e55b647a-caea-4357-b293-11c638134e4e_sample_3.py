from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define activities
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

# Define silent transitions
skip = SilentTransition()

# Define loop nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, scientific_test, expert_review, archive_search, legal_verify, ownership_confirm, compliance_audit, data_documentation, interim_report, department_review])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, scientific_test, expert_review, archive_search, legal_verify, ownership_confirm, compliance_audit, data_documentation, interim_report, department_review, consensus_meeting])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, scientific_test, expert_review, archive_search, legal_verify, ownership_confirm, compliance_audit, data_documentation, interim_report, department_review, consensus_meeting, final_approval])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, scientific_test, expert_review, archive_search, legal_verify, ownership_confirm, compliance_audit, data_documentation, interim_report, department_review, consensus_meeting, final_approval, artifact_release])

# Define exclusive choice nodes
xor1 = OperatorPOWL(operator=Operator.XOR, children=[skip, loop1])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[skip, loop2])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[skip, loop3])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[skip, loop4])

# Define root node
root = StrictPartialOrder(nodes=[artifact_intake, xor1, xor2, xor3, xor4])

# Define dependencies
root.order.add_edge(artifact_intake, xor1)
root.order.add_edge(artifact_intake, xor2)
root.order.add_edge(artifact_intake, xor3)
root.order.add_edge(artifact_intake, xor4)

# Print the root node
print(root)