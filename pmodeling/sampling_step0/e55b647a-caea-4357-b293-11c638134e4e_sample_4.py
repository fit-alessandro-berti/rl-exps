import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the loop and choice nodes
loop_provenance = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, archive_search, legal_verify, ownership_confirm, compliance_audit, data_documentation, interim_report, department_review, consensus_meeting, final_approval])
choice_intake = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, loop_provenance])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[choice_intake, scientific_test, expert_review, artifact_release])
root.order.add_edge(choice_intake, scientific_test)
root.order.add_edge(choice_intake, expert_review)

# Print the root
print(root)