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

# Define the control-flow operators
xor = OperatorPOWL(operator=Operator.XOR, children=[cultural_assess, display_approve])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[lender_notify, investigation_flag])
loop = OperatorPOWL(operator=Operator.LOOP, children=[database_search, legal_audit])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[expert_review, report_draft])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[style_compare, digital_capture])

# Define the root POWL model
root = StrictPartialOrder(nodes=[artifact_intake, provenance_check, material_scan, xor, loop, loop2, loop3, xor2, archival_store])
root.order.add_edge(artifact_intake, provenance_check)
root.order.add_edge(provenance_check, material_scan)
root.order.add_edge(material_scan, xor)
root.order.add_edge(xor, loop)
root.order.add_edge(loop, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, xor2)
root.order.add_edge(xor2, archival_store)

print(root)