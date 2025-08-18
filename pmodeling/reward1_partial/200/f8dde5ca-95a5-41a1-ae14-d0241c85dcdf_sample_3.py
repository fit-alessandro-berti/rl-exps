from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

provenance_check = Transition(label='Provenance Check')
material_scan = Transition(label='Material Scan')
radiocarbon_test = Transition(label='Radiocarbon Test')
style_compare = Transition(label='Style Compare')
database_query = Transition(label='Database Query')
blockchain_prep = Transition(label='Blockchain Prep')
legal_review = Transition(label='Legal Review')
ownership_audit = Transition(label='Ownership Audit')
conservation_plan = Transition(label='Conservation Plan')
expert_panel = Transition(label='Expert Panel')
report_draft = Transition(label='Report Draft')
client_review = Transition(label='Client Review')
authority_submit = Transition(label='Authority Submit')
exhibit_setup = Transition(label='Exhibit Setup')
final_approval = Transition(label='Final Approval')

skip = SilentTransition()

provenance_check_and_material_scan = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, material_scan])
radiocarbon_test_and_database_query = OperatorPOWL(operator=Operator.XOR, children=[radiocarbon_test, database_query])
legal_review_and_ownership_audit = OperatorPOWL(operator=Operator.XOR, children=[legal_review, ownership_audit])
conservation_plan_and_style_compare = OperatorPOWL(operator=Operator.XOR, children=[conservation_plan, style_compare])

loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check_and_material_scan, radiocarbon_test_and_database_query, legal_review_and_ownership_audit, conservation_plan_and_style_compare])

root = StrictPartialOrder(nodes=[loop, blockchain_prep, expert_panel, report_draft, client_review, authority_submit, exhibit_setup, final_approval])
root.order.add_edge(loop, blockchain_prep)
root.order.add_edge(loop, expert_panel)
root.order.add_edge(loop, report_draft)
root.order.add_edge(loop, client_review)
root.order.add_edge(loop, authority_submit)
root.order.add_edge(loop, exhibit_setup)
root.order.add_edge(loop, final_approval)