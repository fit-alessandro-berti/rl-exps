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

# Define silent transitions for concurrent activities
skip = SilentTransition()

# Define loop for data synthesis
loop = OperatorPOWL(operator=Operator.LOOP, children=[data_synthesis, skip])

# Define exclusive choice for reporting
xor = OperatorPOWL(operator=Operator.XOR, children=[report_draft, skip])

# Define partial order
root = StrictPartialOrder(nodes=[artifact_intake, provenance_check, material_scan, style_compare, digital_capture, expert_review, database_search, legal_audit, cultural_assess, loop, xor, archival_store, display_approve, lender_notify, investigation_flag])

# Add dependencies
root.order.add_edge(artifact_intake, provenance_check)
root.order.add_edge(artifact_intake, material_scan)
root.order.add_edge(artifact_intake, style_compare)
root.order.add_edge(artifact_intake, digital_capture)
root.order.add_edge(artifact_intake, expert_review)
root.order.add_edge(artifact_intake, database_search)
root.order.add_edge(artifact_intake, legal_audit)
root.order.add_edge(artifact_intake, cultural_assess)
root.order.add_edge(provenance_check, loop)
root.order.add_edge(material_scan, loop)
root.order.add_edge(style_compare, loop)
root.order.add_edge(digital_capture, loop)
root.order.add_edge(expert_review, loop)
root.order.add_edge(database_search, loop)
root.order.add_edge(legal_audit, loop)
root.order.add_edge(cultural_assess, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, archival_store)
root.order.add_edge(xor, display_approve)
root.order.add_edge(xor, lender_notify)
root.order.add_edge(xor, investigation_flag)

# Print the root
print(root)