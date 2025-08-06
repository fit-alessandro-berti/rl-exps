from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define silent transitions
skip = SilentTransition()

# Define process tree
provenance_check_to_material_scan = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, material_scan])
material_scan_to_radiocarbon_test = OperatorPOWL(operator=Operator.XOR, children=[material_scan, radiocarbon_test])
radiocarbon_test_to_style_compare = OperatorPOWL(operator=Operator.XOR, children=[radiocarbon_test, style_compare])
style_compare_to_database_query = OperatorPOWL(operator=Operator.XOR, children=[style_compare, database_query])
database_query_to_blockchain_prep = OperatorPOWL(operator=Operator.XOR, children=[database_query, blockchain_prep])
blockchain_prep_to_legal_review = OperatorPOWL(operator=Operator.XOR, children=[blockchain_prep, legal_review])
legal_review_to_ownership_audit = OperatorPOWL(operator=Operator.XOR, children=[legal_review, ownership_audit])
ownership_audit_to_conservation_plan = OperatorPOWL(operator=Operator.XOR, children=[ownership_audit, conservation_plan])
conservation_plan_to_expert_panel = OperatorPOWL(operator=Operator.XOR, children=[conservation_plan, expert_panel])
expert_panel_to_report_draft = OperatorPOWL(operator=Operator.XOR, children=[expert_panel, report_draft])
report_draft_to_client_review = OperatorPOWL(operator=Operator.XOR, children=[report_draft, client_review])
client_review_to_authority_submit = OperatorPOWL(operator=Operator.XOR, children=[client_review, authority_submit])
authority_submit_to_exhibit_setup = OperatorPOWL(operator=Operator.XOR, children=[authority_submit, exhibit_setup])
exhibit_setup_to_final_approval = OperatorPOWL(operator=Operator.XOR, children=[exhibit_setup, final_approval])

# Define root
root = StrictPartialOrder(nodes=[
    provenance_check,
    material_scan,
    radiocarbon_test,
    style_compare,
    database_query,
    blockchain_prep,
    legal_review,
    ownership_audit,
    conservation_plan,
    expert_panel,
    report_draft,
    client_review,
    authority_submit,
    exhibit_setup,
    final_approval
])

# Define dependencies
root.order.add_edge(provenance_check, material_scan)
root.order.add_edge(material_scan, radiocarbon_test)
root.order.add_edge(radiocarbon_test, style_compare)
root.order.add_edge(style_compare, database_query)
root.order.add_edge(database_query, blockchain_prep)
root.order.add_edge(blockchain_prep, legal_review)
root.order.add_edge(legal_review, ownership_audit)
root.order.add_edge(ownership_audit, conservation_plan)
root.order.add_edge(conservation_plan, expert_panel)
root.order.add_edge(expert_panel, report_draft)
root.order.add_edge(report_draft, client_review)
root.order.add_edge(client_review, authority_submit)
root.order.add_edge(authority_submit, exhibit_setup)
root.order.add_edge(exhibit_setup, final_approval)

print(root)