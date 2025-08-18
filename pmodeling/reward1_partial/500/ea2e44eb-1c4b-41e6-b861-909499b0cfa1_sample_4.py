from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the POWL model
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

provenance_check_xor = OperatorPOWL(operator=Operator.XOR, children=[archive_search, expert_consult])
material_scan_xor = OperatorPOWL(operator=Operator.XOR, children=[material_scan, three_d_imaging])
stylistic_match_xor = OperatorPOWL(operator=Operator.XOR, children=[stylistic_match, database_query])
panel_review_xor = OperatorPOWL(operator=Operator.XOR, children=[panel_review, certify_report])
condition_assess_xor = OperatorPOWL(operator=Operator.XOR, children=[condition_assess, storage_plan])
catalog_entry_xor = OperatorPOWL(operator=Operator.XOR, children=[catalog_entry, display_prep])
loan_arrange_xor = OperatorPOWL(operator=Operator.XOR, children=[loan_arrange, monitor_setup])

root = StrictPartialOrder(nodes=[
    artifact_intake,
    provenance_check,
    provenance_check_xor,
    material_scan_xor,
    stylistic_match_xor,
    panel_review_xor,
    condition_assess_xor,
    catalog_entry_xor,
    loan_arrange_xor
])

root.order.add_edge(artifact_intake, provenance_check)
root.order.add_edge(provenance_check, provenance_check_xor)
root.order.add_edge(provenance_check_xor, material_scan_xor)
root.order.add_edge(material_scan_xor, stylistic_match_xor)
root.order.add_edge(stylistic_match_xor, panel_review_xor)
root.order.add_edge(panel_review_xor, condition_assess_xor)
root.order.add_edge(condition_assess_xor, catalog_entry_xor)
root.order.add_edge(catalog_entry_xor, loan_arrange_xor)

# Print the root model for verification
print(root)