from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

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

skip = SilentTransition()

provenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, archive_search])
material_loop = OperatorPOWL(operator=Operator.LOOP, children=[material_sampling, scientific_test, expert_review, compliance_audit])
legal_loop = OperatorPOWL(operator=Operator.LOOP, children=[legal_verify, ownership_confirm])

data_documentation_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_documentation, interim_report])

department_review_loop = OperatorPOWL(operator=Operator.LOOP, children=[department_review, consensus_meeting])
final_approval_loop = OperatorPOWL(operator=Operator.LOOP, children=[final_approval, artifact_release])

root = StrictPartialOrder(nodes=[
    artifact_intake,
    provenance_loop,
    material_loop,
    legal_loop,
    data_documentation_loop,
    department_review_loop,
    final_approval_loop,
])

root.order.add_edge(artifact_intake, provenance_loop)
root.order.add_edge(provenance_loop, material_loop)
root.order.add_edge(material_loop, legal_loop)
root.order.add_edge(legal_loop, data_documentation_loop)
root.order.add_edge(data_documentation_loop, department_review_loop)
root.order.add_edge(department_review_loop, final_approval_loop)
root.order.add_edge(final_approval_loop, artifact_release)