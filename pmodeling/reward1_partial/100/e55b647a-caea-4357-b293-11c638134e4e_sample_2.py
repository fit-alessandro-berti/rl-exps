from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

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

# Define silent transitions
skip = SilentTransition()

# Define partial order components
provenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, archive_search])
scientific_loop = OperatorPOWL(operator=Operator.LOOP, children=[material_sampling, scientific_test])
expert_loop = OperatorPOWL(operator=Operator.LOOP, children=[expert_review, legal_verify])
ownership_loop = OperatorPOWL(operator=Operator.LOOP, children=[ownership_confirm, compliance_audit])
data_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_documentation, interim_report])
review_loop = OperatorPOWL(operator=Operator.LOOP, children=[department_review, consensus_meeting])

# Define the root partial order
root = StrictPartialOrder(nodes=[
    artifact_intake,
    provenance_loop,
    scientific_loop,
    expert_loop,
    ownership_loop,
    data_loop,
    review_loop,
    final_approval,
    artifact_release
])

# Add edges to establish dependencies
root.order.add_edge(artifact_intake, provenance_loop)
root.order.add_edge(provenance_loop, scientific_loop)
root.order.add_edge(scientific_loop, expert_loop)
root.order.add_edge(expert_loop, ownership_loop)
root.order.add_edge(ownership_loop, data_loop)
root.order.add_edge(data_loop, review_loop)
root.order.add_edge(review_loop, final_approval)
root.order.add_edge(final_approval, artifact_release)

# Print the root model
print(root)