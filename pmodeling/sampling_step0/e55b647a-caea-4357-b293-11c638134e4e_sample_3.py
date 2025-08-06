import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

# Define silent activities
skip = SilentTransition()

# Define choices
provenance_choice = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, skip])
material_choice = OperatorPOWL(operator=Operator.XOR, children=[material_sampling, skip])
test_choice = OperatorPOWL(operator=Operator.XOR, children=[scientific_test, skip])
review_choice = OperatorPOWL(operator=Operator.XOR, children=[expert_review, skip])
archive_choice = OperatorPOWL(operator=Operator.XOR, children=[archive_search, skip])
verify_choice = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, skip])
confirm_choice = OperatorPOWL(operator=Operator.XOR, children=[ownership_confirm, skip])
audit_choice = OperatorPOWL(operator=Operator.XOR, children=[compliance_audit, skip])
document_choice = OperatorPOWL(operator=Operator.XOR, children=[data_documentation, skip])

# Define loops
provenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, provenance_choice])
material_loop = OperatorPOWL(operator=Operator.LOOP, children=[material_sampling, material_choice])
test_loop = OperatorPOWL(operator=Operator.LOOP, children=[scientific_test, test_choice])
review_loop = OperatorPOWL(operator=Operator.LOOP, children=[expert_review, review_choice])
archive_loop = OperatorPOWL(operator=Operator.LOOP, children=[archive_search, archive_choice])
verify_loop = OperatorPOWL(operator=Operator.LOOP, children=[legal_verify, verify_choice])
confirm_loop = OperatorPOWL(operator=Operator.LOOP, children=[ownership_confirm, confirm_choice])
audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[compliance_audit, audit_choice])
document_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_documentation, document_choice])

# Define partial order
root = StrictPartialOrder(nodes=[
    provenance_loop,
    material_loop,
    test_loop,
    review_loop,
    archive_loop,
    verify_loop,
    confirm_loop,
    audit_loop,
    document_loop,
    interim_report,
    department_review,
    consensus_meeting,
    final_approval,
    artifact_release
])

# Define dependencies
root.order.add_edge(provenance_loop, material_loop)
root.order.add_edge(material_loop, test_loop)
root.order.add_edge(test_loop, review_loop)
root.order.add_edge(review_loop, archive_loop)
root.order.add_edge(archive_loop, verify_loop)
root.order.add_edge(verify_loop, confirm_loop)
root.order.add_edge(confirm_loop, audit_loop)
root.order.add_edge(audit_loop, document_loop)
root.order.add_edge(document_loop, interim_report)
root.order.add_edge(interim_report, department_review)
root.order.add_edge(department_review, consensus_meeting)
root.order.add_edge(consensus_meeting, final_approval)
root.order.add_edge(final_approval, artifact_release)

# Return the root
root