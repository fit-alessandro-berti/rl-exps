import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

# Provenance Check and Archive Search
provenance_check_and_archive_search = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, archive_search])

# Expert Interview and Material Scan
expert_interview_and_material_scan = OperatorPOWL(operator=Operator.XOR, children=[expert_interview, material_scan])

# Age Analysis and Stylistic Review
age_analysis_and_stylistic_review = OperatorPOWL(operator=Operator.XOR, children=[age_analysis, stylistic_review])

# Context Mapping and Legal Clearance
context_mapping_and_legal_clearance = OperatorPOWL(operator=Operator.XOR, children=[context_mapping, legal_clearance])

# Parallel Steps for Non-Invasive Testing
parallel_steps = OperatorPOWL(operator=Operator.XOR, children=[age_analysis_and_stylistic_review, context_mapping_and_legal_clearance])

# Parallel Steps for Stylistic Comparison
parallel_stylistic_steps = OperatorPOWL(operator=Operator.XOR, children=[stylistic_review, context_mapping])

# Parallel Steps for Data Compilation
parallel_data_compilation_steps = OperatorPOWL(operator=Operator.XOR, children=[data_compilation, report_drafting])

# Parallel Steps for Peer Review
parallel_peer_review_steps = OperatorPOWL(operator=Operator.XOR, children=[peer_review, final_assessment])

# Final Authentication Decision
final_authentication_decision = OperatorPOWL(operator=Operator.XOR, children=[acquisition_plan, restoration_prep])

# Parallel Steps for Documentation and Data Backup
parallel_documentation_and_data_backup = OperatorPOWL(operator=Operator.XOR, children=[documentation, data_backup])

# Loop for Non-Invasive Testing
loop_non_invasive_testing = OperatorPOWL(operator=Operator.LOOP, children=[parallel_steps, parallel_stylistic_steps])

# Loop for Data Compilation and Peer Review
loop_data_compilation_and_peer_review = OperatorPOWL(operator=Operator.LOOP, children=[parallel_data_compilation_steps, parallel_peer_review_steps])

# Loop for Final Authentication Decision
loop_final_authentication_decision = OperatorPOWL(operator=Operator.LOOP, children=[final_authentication_decision])

root = StrictPartialOrder(nodes=[loop_non_invasive_testing, loop_data_compilation_and_peer_review, loop_final_authentication_decision])
root.order.add_edge(loop_non_invasive_testing, loop_data_compilation_and_peer_review)
root.order.add_edge(loop_data_compilation_and_peer_review, loop_final_authentication_decision)