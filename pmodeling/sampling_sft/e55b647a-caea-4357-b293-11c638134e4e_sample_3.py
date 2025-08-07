import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
artifact_intake    = Transition(label='Artifact Intake')
provenance_check   = Transition(label='Provenance Check')
material_sampling  = Transition(label='Material Sampling')
scientific_test    = Transition(label='Scientific Test')
expert_review      = Transition(label='Expert Review')
archive_search     = Transition(label='Archive Search')
legal_verify       = Transition(label='Legal Verify')
ownership_confirm  = Transition(label='Ownership Confirm')
compliance_audit   = Transition(label='Compliance Audit')
data_documentation = Transition(label='Data Documentation')
interim_report     = Transition(label='Interim Report')
department_review  = Transition(label='Department Review')
consensus_meeting  = Transition(label='Consensus Meeting')
final_approval     = Transition(label='Final Approval')
artifact_release   = Transition(label='Artifact Release')

# Build the testing & verification partial order
test_po = StrictPartialOrder(nodes=[
    material_sampling, scientific_test, expert_review
])
test_po.order.add_edge(material_sampling, scientific_test)
test_po.order.add_edge(scientific_test, expert_review)

# Build the provenance & legal partial order
provenance_po = StrictPartialOrder(nodes=[
    provenance_check, archive_search, legal_verify, ownership_confirm, compliance_audit
])
provenance_po.order.add_edge(provenance_check, archive_search)
provenance_po.order.add_edge(archive_search, legal_verify)
provenance_po.order.add_edge(legal_verify, ownership_confirm)
provenance_po.order.add_edge(ownership_confirm, compliance_audit)

# Build the review & approval loop
# A: documentation & interim report
review_body = StrictPartialOrder(nodes=[
    data_documentation, interim_report
])
review_body.order.add_edge(data_documentation, interim_report)

# B: department review then optional consensus & final approval
review_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    department_review,
    OperatorPOWL(operator=Operator.XOR, children=[
        consensus_meeting,
        final_approval
    ])
])

# Assemble the root partial order
root = StrictPartialOrder(nodes=[
    artifact_intake,
    provenance_po,
    test_po,
    review_body,
    review_loop,
    artifact_release
])

# Define the control‐flow edges
root.order.add_edge(artifact_intake, provenance_po)
root.order.add_edge(artifact_intake, test_po)

root.order.add_edge(provenance_po, review_body)
root.order.add_edge(test_po, review_body)

root.order.add_edge(review_body, review_loop)
root.order.add_edge(review_loop, artifact_release)