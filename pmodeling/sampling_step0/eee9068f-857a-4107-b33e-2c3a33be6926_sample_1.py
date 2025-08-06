import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
artifact_intake = Transition(label='Artifact Intake')
provenance_check = Transition(label='Provenance Check')
archive_search = Transition(label='Archive Search')
expert_interview = Transition(label='Expert Interview')
material_scan = Transition(label='Material Scan')
age_analysis = Transition(label='Age Analysis')
stylistic_review = Transition(label='Stylistic Review')
context_mapping = Transition(label='Context Mapping')
legal_clearance = Transition(label='Legal Clearance')
data_compilation = Transition(label='Data Compilation')
report_drafting = Transition(label='Report Drafting')
peer_review = Transition(label='Peer Review')
final_assessment = Transition(label='Final Assessment')
acquisition_plan = Transition(label='Acquisition Plan')
restoration_prep = Transition(label='Restoration Prep')
documentation = Transition(label='Documentation')
data_backup = Transition(label='Data Backup')

# Define the partial order
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, archive_search, expert_interview, material_scan, age_analysis, stylistic_review, context_mapping, legal_clearance])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[data_compilation, report_drafting, peer_review, final_assessment])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[acquisition_plan, restoration_prep])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[documentation, data_backup])

xor1 = OperatorPOWL(operator=Operator.XOR, children=[loop1, loop2])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[loop3, loop4])

root = StrictPartialOrder(nodes=[artifact_intake, xor1, xor2])
root.order.add_edge(artifact_intake, xor1)
root.order.add_edge(xor1, xor2)

# Print the result
print(root)