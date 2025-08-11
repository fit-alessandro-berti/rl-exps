import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the loops and exclusive choices
provenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, archive_search, expert_interview])
material_loop = OperatorPOWL(operator=Operator.LOOP, children=[material_scan, age_analysis])
stylistic_loop = OperatorPOWL(operator=Operator.LOOP, children=[stylistic_review, context_mapping])
legal_loop = OperatorPOWL(operator=Operator.LOOP, children=[legal_clearance])
data_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_compilation])
report_loop = OperatorPOWL(operator=Operator.LOOP, children=[report_drafting])
peer_loop = OperatorPOWL(operator=Operator.LOOP, children=[peer_review])
final_loop = OperatorPOWL(operator=Operator.LOOP, children=[final_assessment])
acquisition_loop = OperatorPOWL(operator=Operator.LOOP, children=[acquisition_plan])
restoration_loop = OperatorPOWL(operator=Operator.LOOP, children=[restoration_prep])
documentation_loop = OperatorPOWL(operator=Operator.LOOP, children=[documentation])
data_backup_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_backup])

# Define exclusive choices
exclusive_1 = OperatorPOWL(operator=Operator.XOR, children=[material_loop, legal_loop])
exclusive_2 = OperatorPOWL(operator=Operator.XOR, children=[stylistic_loop, data_loop])
exclusive_3 = OperatorPOWL(operator=Operator.XOR, children=[report_loop, peer_loop])
exclusive_4 = OperatorPOWL(operator=Operator.XOR, children=[final_loop, acquisition_loop])
exclusive_5 = OperatorPOWL(operator=Operator.XOR, children=[restoration_loop, documentation_loop])
exclusive_6 = OperatorPOWL(operator=Operator.XOR, children=[data_backup_loop])

# Define the root POWL model
root = StrictPartialOrder(nodes=[artifact_intake, provenance_loop, material_loop, stylistic_loop, legal_loop, data_loop, report_loop, peer_loop, final_loop, acquisition_loop, restoration_loop, documentation_loop, data_backup_loop, exclusive_1, exclusive_2, exclusive_3, exclusive_4, exclusive_5, exclusive_6])
root.order.add_edge(artifact_intake, provenance_loop)
root.order.add_edge(provenance_loop, exclusive_1)
root.order.add_edge(material_loop, exclusive_2)
root.order.add_edge(stylistic_loop, exclusive_3)
root.order.add_edge(legal_loop, exclusive_4)
root.order.add_edge(data_loop, exclusive_5)
root.order.add_edge(report_loop, exclusive_6)
root.order.add_edge(exclusive_1, exclusive_2)
root.order.add_edge(exclusive_2, exclusive_3)
root.order.add_edge(exclusive_3, exclusive_4)
root.order.add_edge(exclusive_4, exclusive_5)
root.order.add_edge(exclusive_5, exclusive_6)
root.order.add_edge(exclusive_6, final_loop)
root.order.add_edge(final_loop, acquisition_loop)
root.order.add_edge(acquisition_loop, restoration_loop)
root.order.add_edge(restoration_loop, documentation_loop)
root.order.add_edge(documentation_loop, data_backup_loop)