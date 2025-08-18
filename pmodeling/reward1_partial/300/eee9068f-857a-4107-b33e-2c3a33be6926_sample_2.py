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

skip = SilentTransition()

provenance_check_xor = OperatorPOWL(operator=Operator.XOR, children=[archive_search, expert_interview, skip])
context_mapping_xor = OperatorPOWL(operator=Operator.XOR, children=[age_analysis, stylistic_review, skip])
legal_clearance_xor = OperatorPOWL(operator=Operator.XOR, children=[legal_clearance, skip])
data_compilation_xor = OperatorPOWL(operator=Operator.XOR, children=[data_compilation, skip])

artifact_intake_loop = OperatorPOWL(operator=Operator.LOOP, children=[artifact_intake])
provenance_check_loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check_xor])
context_mapping_loop = OperatorPOWL(operator=Operator.LOOP, children=[context_mapping_xor])
legal_clearance_loop = OperatorPOWL(operator=Operator.LOOP, children=[legal_clearance_xor])
data_compilation_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_compilation_xor])

report_drafting_xor = OperatorPOWL(operator=Operator.XOR, children=[report_drafting, peer_review, skip])
final_assessment_xor = OperatorPOWL(operator=Operator.XOR, children=[final_assessment, skip])
acquisition_plan_xor = OperatorPOWL(operator=Operator.XOR, children=[acquisition_plan, skip])
restoration_prep_xor = OperatorPOWL(operator=Operator.XOR, children=[restoration_prep, skip])

documentation_loop = OperatorPOWL(operator=Operator.LOOP, children=[documentation])
data_backup_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_backup])

root = StrictPartialOrder(nodes=[artifact_intake_loop, provenance_check_loop, context_mapping_loop, legal_clearance_loop, data_compilation_loop, report_drafting_xor, final_assessment_xor, acquisition_plan_xor, restoration_prep_xor, documentation_loop, data_backup_loop])
root.order.add_edge(artifact_intake_loop, provenance_check_loop)
root.order.add_edge(provenance_check_loop, context_mapping_loop)
root.order.add_edge(context_mapping_loop, legal_clearance_loop)
root.order.add_edge(legal_clearance_loop, data_compilation_loop)
root.order.add_edge(data_compilation_loop, report_drafting_xor)
root.order.add_edge(report_drafting_xor, final_assessment_xor)
root.order.add_edge(final_assessment_xor, acquisition_plan_xor)
root.order.add_edge(acquisition_plan_xor, restoration_prep_xor)
root.order.add_edge(restoration_prep_xor, documentation_loop)
root.order.add_edge(documentation_loop, data_backup_loop)