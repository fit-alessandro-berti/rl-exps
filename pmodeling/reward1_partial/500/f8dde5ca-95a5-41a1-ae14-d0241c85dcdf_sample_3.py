import pm4py
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

provenance_check_xor = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, skip])
material_scan_xor = OperatorPOWL(operator=Operator.XOR, children=[material_scan, skip])
radiocarbon_test_xor = OperatorPOWL(operator=Operator.XOR, children=[radiocarbon_test, skip])
style_compare_xor = OperatorPOWL(operator=Operator.XOR, children=[style_compare, skip])
database_query_xor = OperatorPOWL(operator=Operator.XOR, children=[database_query, skip])
blockchain_prep_xor = OperatorPOWL(operator=Operator.XOR, children=[blockchain_prep, skip])
legal_review_xor = OperatorPOWL(operator=Operator.XOR, children=[legal_review, skip])
ownership_audit_xor = OperatorPOWL(operator=Operator.XOR, children=[ownership_audit, skip])
conservation_plan_xor = OperatorPOWL(operator=Operator.XOR, children=[conservation_plan, skip])
expert_panel_xor = OperatorPOWL(operator=Operator.XOR, children=[expert_panel, skip])
report_draft_xor = OperatorPOWL(operator=Operator.XOR, children=[report_draft, skip])
client_review_xor = OperatorPOWL(operator=Operator.XOR, children=[client_review, skip])
authority_submit_xor = OperatorPOWL(operator=Operator.XOR, children=[authority_submit, skip])
exhibit_setup_xor = OperatorPOWL(operator=Operator.XOR, children=[exhibit_setup, skip])
final_approval_xor = OperatorPOWL(operator=Operator.XOR, children=[final_approval, skip])

root = StrictPartialOrder(nodes=[
    provenance_check_xor,
    material_scan_xor,
    radiocarbon_test_xor,
    style_compare_xor,
    database_query_xor,
    blockchain_prep_xor,
    legal_review_xor,
    ownership_audit_xor,
    conservation_plan_xor,
    expert_panel_xor,
    report_draft_xor,
    client_review_xor,
    authority_submit_xor,
    exhibit_setup_xor,
    final_approval_xor
])

root.order.add_edge(provenance_check_xor, material_scan_xor)
root.order.add_edge(material_scan_xor, radiocarbon_test_xor)
root.order.add_edge(radiocarbon_test_xor, style_compare_xor)
root.order.add_edge(style_compare_xor, database_query_xor)
root.order.add_edge(database_query_xor, blockchain_prep_xor)
root.order.add_edge(blockchain_prep_xor, legal_review_xor)
root.order.add_edge(legal_review_xor, ownership_audit_xor)
root.order.add_edge(ownership_audit_xor, conservation_plan_xor)
root.order.add_edge(conservation_plan_xor, expert_panel_xor)
root.order.add_edge(expert_panel_xor, report_draft_xor)
root.order.add_edge(report_draft_xor, client_review_xor)
root.order.add_edge(client_review_xor, authority_submit_xor)
root.order.add_edge(authority_submit_xor, exhibit_setup_xor)
root.order.add_edge(exhibit_setup_xor, final_approval_xor)