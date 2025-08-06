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

# Define the silent transitions
skip = SilentTransition()

# Define the control-flow operators
provenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, material_scan, style_compare])
digital_capture_loop = OperatorPOWL(operator=Operator.LOOP, children=[digital_capture, expert_review])
database_search_loop = OperatorPOWL(operator=Operator.LOOP, children=[database_search, legal_audit, cultural_assess])
data_synthesis_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_synthesis, report_draft, archival_store])
cross_reference = OperatorPOWL(operator=Operator.XOR, children=[provenance_loop, digital_capture_loop, database_search_loop, data_synthesis_loop])
artifact_approve = OperatorPOWL(operator=Operator.XOR, children=[display_approve, lender_notify, investigation_flag])

# Define the root POWL model
root = StrictPartialOrder(nodes=[artifact_intake, cross_reference, artifact_approve])
root.order.add_edge(artifact_intake, cross_reference)
root.order.add_edge(cross_reference, artifact_approve)

# Print the POWL model
print(root)