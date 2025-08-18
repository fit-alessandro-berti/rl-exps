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

# Define the silent transitions (empty labels)
skip = SilentTransition()

# Define the loop for the artifact intake and provenance check
loop_artifact_intake_provenance = OperatorPOWL(operator=Operator.LOOP, children=[artifact_intake, provenance_check])

# Define the exclusive choice for material scan and digital capture
xor_material_scan_digital_capture = OperatorPOWL(operator=Operator.XOR, children=[material_scan, digital_capture])

# Define the exclusive choice for expert review and legal audit
xor_expert_review_legal_audit = OperatorPOWL(operator=Operator.XOR, children=[expert_review, legal_audit])

# Define the exclusive choice for cultural assess and database search
xor_cultural_assess_database_search = OperatorPOWL(operator=Operator.XOR, children=[cultural_assess, database_search])

# Define the loop for the data synthesis and report draft
loop_data_synthesis_report_draft = OperatorPOWL(operator=Operator.LOOP, children=[data_synthesis, report_draft])

# Define the exclusive choice for archival store and display approve
xor_archival_store_display_approve = OperatorPOWL(operator=Operator.XOR, children=[archival_store, display_approve])

# Define the exclusive choice for lender notify and investigation flag
xor_lender_notify_investigation_flag = OperatorPOWL(operator=Operator.XOR, children=[lender_notify, investigation_flag])

# Define the root partial order
root = StrictPartialOrder(nodes=[loop_artifact_intake_provenance, xor_material_scan_digital_capture, xor_expert_review_legal_audit, xor_cultural_assess_database_search, loop_data_synthesis_report_draft, xor_archival_store_display_approve, xor_lender_notify_investigation_flag])

# Add dependencies
root.order.add_edge(loop_artifact_intake_provenance, xor_material_scan_digital_capture)
root.order.add_edge(loop_artifact_intake_provenance, xor_expert_review_legal_audit)
root.order.add_edge(xor_material_scan_digital_capture, loop_data_synthesis_report_draft)
root.order.add_edge(xor_expert_review_legal_audit, loop_data_synthesis_report_draft)
root.order.add_edge(loop_data_synthesis_report_draft, xor_archival_store_display_approve)
root.order.add_edge(loop_data_synthesis_report_draft, xor_lender_notify_investigation_flag)
root.order.add_edge(xor_archival_store_display_approve, xor_lender_notify_investigation_flag)

# Print the root partial order
print(root)