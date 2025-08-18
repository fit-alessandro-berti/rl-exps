import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
artifact_intake = Transition(label='Artifact Intake')
provenance_check = Transition(label='Provenance Check')
material_scan = Transition(label='Material Scan')
style_compare = Transition(label='Style Compare')
digital_capture = Transition(label='Digital Capture')
expert_review = Transition(label='Expert Review')
database_search = Transition(label='Database Search')
legal_audit = Transition(label='Legal Audit')
cultural_assess = Transition(label='Cultural Assess')
data_synthesis = Transition(label='Data Synthesis')
report_draft = Transition(label='Report Draft')
archival_store = Transition(label='Archival Store')
display_approve = Transition(label='Display Approve')
lender_notify = Transition(label='Lender Notify')
investigation_flag = Transition(label='Investigation Flag')

# Define the POWL model
xor1 = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, material_scan, style_compare])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[digital_capture, expert_review, database_search])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[legal_audit, cultural_assess, data_synthesis])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[report_draft, archival_store, display_approve])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[lender_notify, investigation_flag])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[xor1, xor2, xor3, xor4, xor5])

root = StrictPartialOrder(nodes=[artifact_intake, xor6])
root.order.add_edge(artifact_intake, xor6)

print(root)