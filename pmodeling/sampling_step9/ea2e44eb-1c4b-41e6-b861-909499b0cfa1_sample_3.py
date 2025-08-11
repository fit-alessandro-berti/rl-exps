import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
artifact_intake = Transition(label='Artifact Intake')
provenance_check = Transition(label='Provenance Check')
archive_search = Transition(label='Archive Search')
expert_consult = Transition(label='Expert Consult')
material_scan = Transition(label='Material Scan')
three_d_imaging = Transition(label='3D Imaging')
stylistic_match = Transition(label='Stylistic Match')
database_query = Transition(label='Database Query')
panel_review = Transition(label='Panel Review')
certify_report = Transition(label='Certify Report')
condition_assess = Transition(label='Condition Assess')
storage_plan = Transition(label='Storage Plan')
catalog_entry = Transition(label='Catalog Entry')
display_prep = Transition(label='Display Prep')
loan_arrange = Transition(label='Loan Arrange')
monitor_setup = Transition(label='Monitor Setup')
skip = SilentTransition()

# Define the loop for artifact processing
artifact_loop = OperatorPOWL(operator=Operator.LOOP, children=[artifact_intake, provenance_check, archive_search, expert_consult, material_scan, three_d_imaging, stylistic_match, database_query, panel_review, certify_report, condition_assess])

# Define the exclusive choice for artifact processing
artifact_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[storage_plan, catalog_entry, display_prep, loan_arrange])

# Define the root model
root = StrictPartialOrder(nodes=[artifact_loop, artifact_exclusive_choice])
root.order.add_edge(artifact_loop, artifact_exclusive_choice)

# Print the final result
print(root)