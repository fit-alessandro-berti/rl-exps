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
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[material_scan, style_compare])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[database_search, legal_audit])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[cultural_assess, data_synthesis])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[report_draft, archival_store])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[display_approve, lender_notify])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[investigation_flag, SilentTransition()])

root = StrictPartialOrder(nodes=[artifact_intake, provenance_check, loop1, loop2, loop3, xor1, xor2, xor3])
root.order.add_edge(artifact_intake, provenance_check)
root.order.add_edge(provenance_check, loop1)
root.order.add_edge(provenance_check, loop2)
root.order.add_edge(loop1, loop3)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, xor1)
root.order.add_edge(loop3, xor2)
root.order.add_edge(xor1, xor3)
root.order.add_edge(xor2, xor3)

print(root)