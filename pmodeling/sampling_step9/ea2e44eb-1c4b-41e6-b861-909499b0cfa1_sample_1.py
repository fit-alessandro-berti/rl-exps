import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

# Provenance Check
provenance_check_loop = OperatorPOWL(operator=Operator.LOOP, children=[archive_search, expert_consult])
provenance_check_xor = OperatorPOWL(operator=Operator.XOR, children=[provenance_check_loop, skip])

# Material Scan
material_scan_loop = OperatorPOWL(operator=Operator.LOOP, children=[material_scan, three_d_imaging])
material_scan_xor = OperatorPOWL(operator=Operator.XOR, children=[material_scan_loop, skip])

# Stylistic Match
stylistic_match_loop = OperatorPOWL(operator=Operator.LOOP, children=[stylistic_match, database_query])
stylistic_match_xor = OperatorPOWL(operator=Operator.XOR, children=[stylistic_match_loop, skip])

# Panel Review
panel_review_loop = OperatorPOWL(operator=Operator.LOOP, children=[panel_review])
panel_review_xor = OperatorPOWL(operator=Operator.XOR, children=[panel_review_loop, skip])

# Certify Report
certify_report_loop = OperatorPOWL(operator=Operator.LOOP, children=[certify_report])
certify_report_xor = OperatorPOWL(operator=Operator.XOR, children=[certify_report_loop, skip])

# Condition Assess
condition_assess_loop = OperatorPOWL(operator=Operator.LOOP, children=[condition_assess])
condition_assess_xor = OperatorPOWL(operator=Operator.XOR, children=[condition_assess_loop, skip])

# Storage Plan
storage_plan_loop = OperatorPOWL(operator=Operator.LOOP, children=[storage_plan])
storage_plan_xor = OperatorPOWL(operator=Operator.XOR, children=[storage_plan_loop, skip])

# Catalog Entry
catalog_entry_loop = OperatorPOWL(operator=Operator.LOOP, children=[catalog_entry])
catalog_entry_xor = OperatorPOWL(operator=Operator.XOR, children=[catalog_entry_loop, skip])

# Display Prep
display_prep_loop = OperatorPOWL(operator=Operator.LOOP, children=[display_prep])
display_prep_xor = OperatorPOWL(operator=Operator.XOR, children=[display_prep_loop, skip])

# Loan Arrange
loan_arrange_loop = OperatorPOWL(operator=Operator.LOOP, children=[loan_arrange])
loan_arrange_xor = OperatorPOWL(operator=Operator.XOR, children=[loan_arrange_loop, skip])

# Monitor Setup
monitor_setup_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor_setup])
monitor_setup_xor = OperatorPOWL(operator=Operator.XOR, children=[monitor_setup_loop, skip])

root = StrictPartialOrder(nodes=[artifact_intake, provenance_check_xor, material_scan_xor, stylistic_match_xor, panel_review_xor, certify_report_xor, condition_assess_xor, storage_plan_xor, catalog_entry_xor, display_prep_xor, loan_arrange_xor, monitor_setup_xor])
root.order.add_edge(provenance_check, provenance_check_xor)
root.order.add_edge(material_scan, material_scan_xor)
root.order.add_edge(stylistic_match, stylistic_match_xor)
root.order.add_edge(panel_review, panel_review_xor)
root.order.add_edge(certify_report, certify_report_xor)
root.order.add_edge(condition_assess, condition_assess_xor)
root.order.add_edge(storage_plan, storage_plan_xor)
root.order.add_edge(catalog_entry, catalog_entry_xor)
root.order.add_edge(display_prep, display_prep_xor)
root.order.add_edge(loan_arrange, loan_arrange_xor)
root.order.add_edge(monitor_setup, monitor_setup_xor)

print(root)