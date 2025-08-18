import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the process
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
xor1 = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, material_scan])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[style_compare, digital_capture])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[expert_review, database_search])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[legal_audit, cultural_assess])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[data_synthesis, report_draft])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[archival_store, display_approve])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[lender_notify, investigation_flag])

# Define the partial order
root = StrictPartialOrder(nodes=[artifact_intake, xor1, xor2, xor3, xor4, xor5, xor6, xor7])
root.order.add_edge(artifact_intake, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)

print(root)