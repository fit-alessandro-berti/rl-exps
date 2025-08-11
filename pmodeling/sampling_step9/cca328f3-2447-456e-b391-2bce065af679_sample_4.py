import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator
# Define the transitions
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

# Define silent transitions
skip = SilentTransition()

# Define loop nodes
loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[material_scan, digital_capture])
loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[expert_review, database_search])
loop_3 = OperatorPOWL(operator=Operator.LOOP, children=[legal_audit, cultural_assess])

# Define XOR nodes
xor_1 = OperatorPOWL(operator=Operator.XOR, children=[cultural_assess, skip])
xor_2 = OperatorPOWL(operator=Operator.XOR, children=[data_synthesis, skip])
xor_3 = OperatorPOWL(operator=Operator.XOR, children=[report_draft, skip])

# Define the root
root = StrictPartialOrder(nodes=[artifact_intake, provenance_check, loop_1, loop_2, loop_3, xor_1, xor_2, xor_3, display_approve, lender_notify, investigation_flag])
root.order.add_edge(artifact_intake, provenance_check)
root.order.add_edge(provenance_check, loop_1)
root.order.add_edge(loop_1, loop_2)
root.order.add_edge(loop_2, loop_3)
root.order.add_edge(loop_3, xor_1)
root.order.add_edge(xor_1, xor_2)
root.order.add_edge(xor_2, xor_3)
root.order.add_edge(xor_3, display_approve)
root.order.add_edge(xor_3, lender_notify)
root.order.add_edge(xor_3, investigation_flag)