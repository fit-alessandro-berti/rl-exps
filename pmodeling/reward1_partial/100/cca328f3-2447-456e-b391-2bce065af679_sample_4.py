import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions for each activity
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

# Define the silent transitions
skip = SilentTransition()

# Define the exclusive choice for the expert review and database search
xor = OperatorPOWL(operator=Operator.XOR, children=[expert_review, database_search])

# Define the loop for the material scan and digital capture
loop = OperatorPOWL(operator=Operator.LOOP, children=[material_scan, digital_capture])

# Define the strict partial order
root = StrictPartialOrder(nodes=[artifact_intake, provenance_check, loop, xor, data_synthesis, report_draft, archival_store, display_approve, lender_notify, investigation_flag])

# Define the order dependencies
root.order.add_edge(artifact_intake, provenance_check)
root.order.add_edge(provenance_check, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, data_synthesis)
root.order.add_edge(data_synthesis, report_draft)
root.order.add_edge(report_draft, archival_store)
root.order.add_edge(archival_store, display_approve)
root.order.add_edge(archival_store, lender_notify)
root.order.add_edge(archival_store, investigation_flag)

print(root)