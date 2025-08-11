import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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
skip_provenance = SilentTransition()
skip_material = SilentTransition()
skip_scientific = SilentTransition()
skip_expert = SilentTransition()
skip_archive = SilentTransition()
skip_legal = SilentTransition()
skip_compliance = SilentTransition()
skip_documentation = SilentTransition()
skip_interim = SilentTransition()
skip_department = SilentTransition()
skip_consensus = SilentTransition()
skip_final = SilentTransition()

# Define partial orders
loop_provenance = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, skip_provenance])
loop_material = OperatorPOWL(operator=Operator.LOOP, children=[material_sampling, skip_material])
loop_scientific = OperatorPOWL(operator=Operator.LOOP, children=[scientific_test, skip_scientific])
loop_expert = OperatorPOWL(operator=Operator.LOOP, children=[expert_review, skip_expert])
loop_archive = OperatorPOWL(operator=Operator.LOOP, children=[archive_search, skip_archive])
loop_legal = OperatorPOWL(operator=Operator.LOOP, children=[legal_verify, skip_legal])
loop_compliance = OperatorPOWL(operator=Operator.LOOP, children=[compliance_audit, skip_compliance])
loop_documentation = OperatorPOWL(operator=Operator.LOOP, children=[data_documentation, skip_documentation])
loop_interim = OperatorPOWL(operator=Operator.LOOP, children=[interim_report, skip_interim])
loop_department = OperatorPOWL(operator=Operator.LOOP, children=[department_review, skip_department])
loop_consensus = OperatorPOWL(operator=Operator.LOOP, children=[consensus_meeting, skip_consensus])
loop_final = OperatorPOWL(operator=Operator.LOOP, children=[final_approval, skip_final])

# Define XORs
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[loop_provenance, artifact_intake])
xor_material = OperatorPOWL(operator=Operator.XOR, children=[loop_material, xor_provenance])
xor_scientific = OperatorPOWL(operator=Operator.XOR, children=[loop_scientific, xor_material])
xor_expert = OperatorPOWL(operator=Operator.XOR, children=[loop_expert, xor_scientific])
xor_archive = OperatorPOWL(operator=Operator.XOR, children=[loop_archive, xor_expert])
xor_legal = OperatorPOWL(operator=Operator.XOR, children=[loop_legal, xor_archive])
xor_compliance = OperatorPOWL(operator=Operator.XOR, children=[loop_compliance, xor_legal])
xor_documentation = OperatorPOWL(operator=Operator.XOR, children=[loop_documentation, xor_compliance])
xor_interim = OperatorPOWL(operator=Operator.XOR, children=[loop_interim, xor_documentation])
xor_department = OperatorPOWL(operator=Operator.XOR, children=[loop_department, xor_interim])
xor_consensus = OperatorPOWL(operator=Operator.XOR, children=[loop_consensus, xor_department])
xor_final = OperatorPOWL(operator=Operator.XOR, children=[loop_final, xor_consensus])

# Define root
root = StrictPartialOrder(nodes=[xor_final, artifact_release])
root.order.add_edge(xor_final, artifact_release)

# Print the POWL model
print(root)