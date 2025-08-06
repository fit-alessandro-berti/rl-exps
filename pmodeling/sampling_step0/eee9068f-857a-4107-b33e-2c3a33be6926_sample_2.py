import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions (e.g., for parallel execution)
skip = SilentTransition()

# Define the POWL model
loop_provenance_check = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check])
xor_archive_search_interview = OperatorPOWL(operator=Operator.XOR, children=[archive_search, expert_interview])
xor_material_scan_age_analysis = OperatorPOWL(operator=Operator.XOR, children=[material_scan, age_analysis])
xor_stylistic_review_context_mapping = OperatorPOWL(operator=Operator.XOR, children=[stylistic_review, context_mapping])
xor_legal_clearance_data_compilation = OperatorPOWL(operator=Operator.XOR, children=[legal_clearance, data_compilation])
xor_report_drafting_peer_review = OperatorPOWL(operator=Operator.XOR, children=[report_drafting, peer_review])
xor_final_assessment_acquisition_plan = OperatorPOWL(operator=Operator.XOR, children=[final_assessment, acquisition_plan])
xor_restoration_prep_documentation = OperatorPOWL(operator=Operator.XOR, children=[restoration_prep, documentation])
xor_data_backup = OperatorPOWL(operator=Operator.XOR, children=[data_backup])

# Construct the POWL model
root = StrictPartialOrder(nodes=[
    loop_provenance_check,
    xor_archive_search_interview,
    xor_material_scan_age_analysis,
    xor_stylistic_review_context_mapping,
    xor_legal_clearance_data_compilation,
    xor_report_drafting_peer_review,
    xor_final_assessment_acquisition_plan,
    xor_restoration_prep_documentation,
    xor_data_backup
])

# Add edges between nodes based on the process flow
root.order.add_edge(loop_provenance_check, xor_archive_search_interview)
root.order.add_edge(loop_provenance_check, xor_material_scan_age_analysis)
root.order.add_edge(xor_archive_search_interview, xor_stylistic_review_context_mapping)
root.order.add_edge(xor_material_scan_age_analysis, xor_legal_clearance_data_compilation)
root.order.add_edge(xor_stylistic_review_context_mapping, xor_report_drafting_peer_review)
root.order.add_edge(xor_legal_clearance_data_compilation, xor_final_assessment_acquisition_plan)
root.order.add_edge(xor_final_assessment_acquisition_plan, xor_restoration_prep_documentation)
root.order.add_edge(xor_restoration_prep_documentation, xor_data_backup)

# Print the final POWL model
print(root)