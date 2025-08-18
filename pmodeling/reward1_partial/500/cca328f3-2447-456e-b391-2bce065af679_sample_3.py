import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define the loop for cross-referencing and legal audit
loop = OperatorPOWL(operator=Operator.LOOP, children=[database_search, legal_audit])

# Define the exclusive choice for cultural assessment and display approval
xor = OperatorPOWL(operator=Operator.XOR, children=[cultural_assess, display_approve])

# Define the partial order
root = StrictPartialOrder(nodes=[artifact_intake, provenance_check, material_scan, style_compare, digital_capture, expert_review, loop, xor, report_draft, archival_store, lender_notify, investigation_flag])
root.order.add_edge(artifact_intake, provenance_check)
root.order.add_edge(provenance_check, material_scan)
root.order.add_edge(material_scan, style_compare)
root.order.add_edge(style_compare, digital_capture)
root.order.add_edge(digital_capture, expert_review)
root.order.add_edge(expert_review, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, report_draft)
root.order.add_edge(report_draft, archival_store)
root.order.add_edge(archival_store, lender_notify)
root.order.add_edge(lender_notify, investigation_flag)