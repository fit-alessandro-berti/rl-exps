import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define POWL nodes
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

# Define silent transitions
skip = SilentTransition()

# Define POWL model
loop = OperatorPOWL(operator=Operator.LOOP, children=[material_scan, age_analysis, stylistic_review, context_mapping])
xor = OperatorPOWL(operator=Operator.XOR, children=[legal_clearance, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[data_compilation, report_drafting])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[peer_review, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[final_assessment, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[acquisition_plan, restoration_prep])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[documentation, data_backup])

root = StrictPartialOrder(nodes=[loop, xor, xor2, xor3, xor4, xor5, xor6])
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)

# Print the POWL model
print(root)