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

# Define the silent transition for skipping
skip = SilentTransition()

# Define the loop for data compilation
loop = OperatorPOWL(operator=Operator.LOOP, children=[data_compilation, peer_review])

# Define the exclusive choice for final assessment and acquisition plan
xor = OperatorPOWL(operator=Operator.XOR, children=[final_assessment, acquisition_plan])

# Define the root POWL model
root = StrictPartialOrder(nodes=[artifact_intake, provenance_check, archive_search, expert_interview, material_scan, age_analysis, stylistic_review, context_mapping, legal_clearance, loop, xor])
root.order.add_edge(artifact_intake, provenance_check)
root.order.add_edge(artifact_intake, archive_search)
root.order.add_edge(artifact_intake, expert_interview)
root.order.add_edge(artifact_intake, material_scan)
root.order.add_edge(artifact_intake, age_analysis)
root.order.add_edge(artifact_intake, stylistic_review)
root.order.add_edge(artifact_intake, context_mapping)
root.order.add_edge(artifact_intake, legal_clearance)
root.order.add_edge(provenance_check, loop)
root.order.add_edge(archive_search, loop)
root.order.add_edge(expert_interview, loop)
root.order.add_edge(material_scan, loop)
root.order.add_edge(age_analysis, loop)
root.order.add_edge(stylistic_review, loop)
root.order.add_edge(context_mapping, loop)
root.order.add_edge(legal_clearance, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, final_assessment)
root.order.add_edge(xor, acquisition_plan)