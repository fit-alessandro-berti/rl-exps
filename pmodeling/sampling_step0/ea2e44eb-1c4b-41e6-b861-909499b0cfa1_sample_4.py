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

# Define silent transitions
skip = SilentTransition()

# Define sub-processes
provenance_subprocess = OperatorPOWL(operator=Operator.XOR, children=[archive_search, expert_consult])
material_subprocess = OperatorPOWL(operator=Operator.XOR, children=[material_scan, three_d_imaging])
stylistic_subprocess = OperatorPOWL(operator=Operator.XOR, children=[stylistic_match, database_query])

# Define main process
provenance_check_node = Transition(label='Provenance Check')
provenance_check_node.order.add_edge(provenance_subprocess, provenance_check)

material_scan_node = Transition(label='Material Scan')
material_scan_node.order.add_edge(material_subprocess, material_scan)

stylistic_match_node = Transition(label='Stylistic Match')
stylistic_match_node.order.add_edge(stylistic_subprocess, stylistic_match)

panel_review_node = Transition(label='Panel Review')
panel_review_node.order.add_edge(provenance_check, provenance_subprocess)
panel_review_node.order.add_edge(material_scan, material_subprocess)
panel_review_node.order.add_edge(stylistic_match, stylistic_subprocess)

certify_report_node = Transition(label='Certify Report')
certify_report_node.order.add_edge(panel_review, panel_review_node)

condition_assess_node = Transition(label='Condition Assess')
condition_assess_node.order.add_edge(certify_report, certify_report_node)

storage_plan_node = Transition(label='Storage Plan')
storage_plan_node.order.add_edge(certify_report, certify_report_node)

catalog_entry_node = Transition(label='Catalog Entry')
catalog_entry_node.order.add_edge(certify_report, certify_report_node)

display_prep_node = Transition(label='Display Prep')
display_prep_node.order.add_edge(certify_report, certify_report_node)

loan_arrange_node = Transition(label='Loan Arrange')
loan_arrange_node.order.add_edge(certify_report, certify_report_node)

monitor_setup_node = Transition(label='Monitor Setup')
monitor_setup_node.order.add_edge(certify_report, certify_report_node)

root = StrictPartialOrder(nodes=[artifact_intake, provenance_check_node, material_scan_node, stylistic_match_node, panel_review_node, certify_report_node, condition_assess_node, storage_plan_node, catalog_entry_node, display_prep_node, loan_arrange_node, monitor_setup_node])