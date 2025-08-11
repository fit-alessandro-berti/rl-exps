import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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
skip = SilentTransition()

# Define the process
loop = OperatorPOWL(operator=Operator.LOOP, children=[artifact_intake, provenance_check, material_scan, style_compare, digital_capture])
xor = OperatorPOWL(operator=Operator.XOR, children=[expert_review, database_search, legal_audit, cultural_assess])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[data_synthesis, report_draft])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[archival_store, display_approve, lender_notify, investigation_flag])
root = StrictPartialOrder(nodes=[loop, xor, xor2, xor3])
root.order.add_edge(loop, xor)
root.order.add_edge(loop, xor2)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor, xor3)
root.order.add_edge(xor2, xor3)

# Print the final POWL model
print(root)