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

# Define the silent activities
skip = SilentTransition()

# Define the exclusive choice for the expert review and legal audit
xor = OperatorPOWL(operator=Operator.XOR, children=[expert_review, legal_audit])

# Define the loop for the provenance check, material scan, and style compare
loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, material_scan, style_compare])

# Define the POWL model
root = StrictPartialOrder(nodes=[artifact_intake, loop, xor, digital_capture, report_draft, archival_store, display_approve, lender_notify, investigation_flag])
root.order.add_edge(artifact_intake, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, digital_capture)
root.order.add_edge(digital_capture, report_draft)
root.order.add_edge(report_draft, archival_store)
root.order.add_edge(archival_store, display_approve)
root.order.add_edge(display_approve, lender_notify)
root.order.add_edge(lender_notify, investigation_flag)