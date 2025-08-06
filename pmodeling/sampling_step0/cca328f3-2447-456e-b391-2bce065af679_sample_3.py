import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define exclusive choice for display approval or lender notification
xor_display_lender = OperatorPOWL(operator=Operator.XOR, children=[display_approve, lender_notify])

# Define exclusive choice for further investigation or archival storage
xor_investigation_archival = OperatorPOWL(operator=Operator.XOR, children=[investigation_flag, archival_store])

# Define loop for data synthesis
loop_data_synthesis = OperatorPOWL(operator=Operator.LOOP, children=[data_synthesis])

# Define partial order for the entire process
root = StrictPartialOrder(nodes=[artifact_intake, provenance_check, material_scan, style_compare, digital_capture, expert_review, database_search, legal_audit, cultural_assess, loop_data_synthesis, xor_display_lender, xor_investigation_archival])

# Define dependencies
root.order.add_edge(artifact_intake, provenance_check)
root.order.add_edge(artifact_intake, material_scan)
root.order.add_edge(artifact_intake, style_compare)
root.order.add_edge(artifact_intake, digital_capture)
root.order.add_edge(provenance_check, expert_review)
root.order.add_edge(material_scan, database_search)
root.order.add_edge(style_compare, database_search)
root.order.add_edge(digital_capture, expert_review)
root.order.add_edge(expert_review, database_search)
root.order.add_edge(database_search, legal_audit)
root.order.add_edge(legal_audit, cultural_assess)
root.order.add_edge(cultural_assess, loop_data_synthesis)
root.order.add_edge(loop_data_synthesis, xor_display_lender)
root.order.add_edge(loop_data_synthesis, xor_investigation_archival)
root.order.add_edge(xor_display_lender, display_approve)
root.order.add_edge(xor_display_lender, lender_notify)
root.order.add_edge(xor_investigation_archival, investigation_flag)
root.order.add_edge(xor_investigation_archival, archival_store)

print(root)