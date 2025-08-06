import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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
skip1 = SilentTransition()
skip2 = SilentTransition()
skip3 = SilentTransition()
skip4 = SilentTransition()

# Define parallel paths
parallel1 = OperatorPOWL(operator=Operator.XOR, children=[archive_search, skip1])
parallel2 = OperatorPOWL(operator=Operator.XOR, children=[expert_interview, skip2])
parallel3 = OperatorPOWL(operator=Operator.XOR, children=[material_scan, skip3])
parallel4 = OperatorPOWL(operator=Operator.XOR, children=[age_analysis, skip4])
parallel5 = OperatorPOWL(operator=Operator.XOR, children=[stylistic_review, skip1])
parallel6 = OperatorPOWL(operator=Operator.XOR, children=[context_mapping, skip2])
parallel7 = OperatorPOWL(operator=Operator.XOR, children=[legal_clearance, skip3])

# Define loops
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[parallel1, parallel2])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[parallel3, parallel4])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[parallel5, parallel6])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[parallel7, skip1])

# Define root
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, report_drafting, peer_review, final_assessment, acquisition_plan, restoration_prep, documentation, data_backup])
root.order.add_edge(loop1, report_drafting)
root.order.add_edge(report_drafting, peer_review)
root.order.add_edge(peer_review, final_assessment)
root.order.add_edge(final_assessment, acquisition_plan)
root.order.add_edge(acquisition_plan, restoration_prep)
root.order.add_edge(restoration_prep, documentation)
root.order.add_edge(documentation, data_backup)

print(root)