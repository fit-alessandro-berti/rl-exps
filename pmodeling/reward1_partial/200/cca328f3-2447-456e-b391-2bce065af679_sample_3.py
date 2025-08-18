import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

provenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, material_scan])
material_loop = OperatorPOWL(operator=Operator.LOOP, children=[style_compare, digital_capture])
expert_loop = OperatorPOWL(operator=Operator.LOOP, children=[expert_review, database_search, legal_audit, cultural_assess])
data_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_synthesis, report_draft])
archive_loop = OperatorPOWL(operator=Operator.LOOP, children=[archival_store, display_approve, lender_notify, investigation_flag])

root = StrictPartialOrder(nodes=[artifact_intake, provenance_loop, material_loop, expert_loop, data_loop, archive_loop])
root.order.add_edge(artifact_intake, provenance_loop)
root.order.add_edge(artifact_intake, material_loop)
root.order.add_edge(artifact_intake, expert_loop)
root.order.add_edge(artifact_intake, data_loop)
root.order.add_edge(artifact_intake, archive_loop)