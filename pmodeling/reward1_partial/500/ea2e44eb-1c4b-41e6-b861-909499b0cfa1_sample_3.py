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

provenance_check_children = [archive_search, expert_consult]
provenance_check = OperatorPOWL(operator=Operator.LOOP, children=provenance_check_children)

material_scan_children = [three_d_imaging]
material_scan = OperatorPOWL(operator=Operator.LOOP, children=material_scan_children)

stylistic_match_children = [database_query]
stylistic_match = OperatorPOWL(operator=Operator.LOOP, children=stylistic_match_children)

panel_review_children = [certify_report, condition_assess, storage_plan]
panel_review = OperatorPOWL(operator=Operator.XOR, children=panel_review_children)

root = StrictPartialOrder(nodes=[artifact_intake, provenance_check, material_scan, stylistic_match, panel_review, catalog_entry, display_prep, loan_arrange, monitor_setup])
root.order.add_edge(artifact_intake, provenance_check)
root.order.add_edge(provenance_check, material_scan)
root.order.add_edge(material_scan, stylistic_match)
root.order.add_edge(stylistic_match, panel_review)
root.order.add_edge(panel_review, catalog_entry)
root.order.add_edge(panel_review, display_prep)
root.order.add_edge(panel_review, loan_arrange)
root.order.add_edge(panel_review, monitor_setup)