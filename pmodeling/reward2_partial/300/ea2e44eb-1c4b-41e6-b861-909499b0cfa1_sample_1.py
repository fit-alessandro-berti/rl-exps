import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define POWL nodes
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

# Define POWL operators
provenance_check_operator = OperatorPOWL(operator=Operator.XOR, children=[archive_search, expert_consult])
material_scan_operator = OperatorPOWL(operator=Operator.XOR, children=[three_d_imaging, database_query])
panel_review_operator = OperatorPOWL(operator=Operator.XOR, children=[certify_report, condition_assess])
storage_plan_operator = OperatorPOWL(operator=Operator.XOR, children=[display_prep, loan_arrange])
monitor_setup_operator = OperatorPOWL(operator=Operator.XOR, children=[storage_plan, monitor_setup])

# Define POWL partial order
root = StrictPartialOrder(nodes=[
    artifact_intake,
    provenance_check,
    provenance_check_operator,
    material_scan,
    material_scan_operator,
    stylistic_match,
    panel_review,
    panel_review_operator,
    storage_plan,
    storage_plan_operator,
    monitor_setup_operator
])

# Define dependencies
root.order.add_edge(artifact_intake, provenance_check)
root.order.add_edge(provenance_check, provenance_check_operator)
root.order.add_edge(provenance_check, material_scan)
root.order.add_edge(material_scan, material_scan_operator)
root.order.add_edge(material_scan, stylistic_match)
root.order.add_edge(stylistic_match, panel_review)
root.order.add_edge(panel_review, panel_review_operator)
root.order.add_edge(panel_review, storage_plan)
root.order.add_edge(storage_plan, storage_plan_operator)
root.order.add_edge(storage_plan, monitor_setup)
root.order.add_edge(monitor_setup, monitor_setup_operator)

# Print the POWL model
print(root)