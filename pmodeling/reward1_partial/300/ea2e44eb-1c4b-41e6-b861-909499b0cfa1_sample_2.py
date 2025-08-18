from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define control-flow operators
choice1 = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, archive_search, expert_consult])
choice2 = OperatorPOWL(operator=Operator.XOR, children=[material_scan, three_d_imaging, stylistic_match])
choice3 = OperatorPOWL(operator=Operator.XOR, children=[database_query, panel_review])
loop = OperatorPOWL(operator=Operator.LOOP, children=[certify_report, condition_assess, storage_plan, catalog_entry, display_prep, loan_arrange, monitor_setup])

# Define root model
root = StrictPartialOrder(nodes=[artifact_intake, choice1, choice2, choice3, loop])
root.order.add_edge(artifact_intake, choice1)
root.order.add_edge(choice1, loop)
root.order.add_edge(choice2, loop)
root.order.add_edge(choice3, loop)