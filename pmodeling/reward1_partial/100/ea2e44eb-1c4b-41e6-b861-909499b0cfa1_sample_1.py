from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define transitions for each activity
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

# Define exclusive choice operators
provenance_choice = OperatorPOWL(operator=Operator.XOR, children=[archive_search, expert_consult])
material_choice = OperatorPOWL(operator=Operator.XOR, children=[material_scan, three_d_imaging])
stylistic_choice = OperatorPOWL(operator=Operator.XOR, children=[stylistic_match, database_query])

# Define loop for panel review
panel_loop = OperatorPOWL(operator=Operator.LOOP, children=[panel_review, certify_report])

# Define partial order for the entire process
root = StrictPartialOrder(nodes=[artifact_intake, provenance_choice, material_choice, stylistic_choice, panel_loop, condition_assess, storage_plan, catalog_entry, display_prep, loan_arrange, monitor_setup])

# Define dependencies between nodes
root.order.add_edge(artifact_intake, provenance_choice)
root.order.add_edge(artifact_intake, material_choice)
root.order.add_edge(artifact_intake, stylistic_choice)
root.order.add_edge(provenance_choice, panel_loop)
root.order.add_edge(material_choice, panel_loop)
root.order.add_edge(stylistic_choice, panel_loop)
root.order.add_edge(panel_loop, condition_assess)
root.order.add_edge(condition_assess, storage_plan)
root.order.add_edge(storage_plan, catalog_entry)
root.order.add_edge(catalog_entry, display_prep)
root.order.add_edge(display_prep, loan_arrange)
root.order.add_edge(loan_arrange, monitor_setup)

print(root)