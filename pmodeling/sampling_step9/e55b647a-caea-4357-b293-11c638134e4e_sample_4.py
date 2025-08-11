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

skip = SilentTransition()

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, material_sampling, scientific_test, expert_review])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[archive_search, legal_verify, ownership_confirm, compliance_audit])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[data_documentation, interim_report, department_review])

xor1 = OperatorPOWL(operator=Operator.XOR, children=[consensus_meeting, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[final_approval, skip])

root = StrictPartialOrder(nodes=[loop1, loop2, loop3, xor1, xor2, artifact_release])
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop2, xor2)
root.order.add_edge(loop3, xor1)
root.order.add_edge(loop3, xor2)

# Save the final result in the variable 'root'