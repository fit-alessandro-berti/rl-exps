import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the POWL nodes and operators
provenance_check_node = OperatorPOWL(operator=Operator.AND, children=[provenance_check, material_scan])
material_scan_node = OperatorPOWL(operator=Operator.AND, children=[material_scan, radiocarbon_test])
radiocarbon_test_node = OperatorPOWL(operator=Operator.AND, children=[radiocarbon_test, style_compare])
style_compare_node = OperatorPOWL(operator=Operator.AND, children=[style_compare, database_query])
database_query_node = OperatorPOWL(operator=Operator.AND, children=[database_query, blockchain_prep])
blockchain_prep_node = OperatorPOWL(operator=Operator.AND, children=[blockchain_prep, legal_review])
legal_review_node = OperatorPOWL(operator=Operator.AND, children=[legal_review, ownership_audit])
ownership_audit_node = OperatorPOWL(operator=Operator.AND, children=[ownership_audit, conservation_plan])
conservation_plan_node = OperatorPOWL(operator=Operator.AND, children=[conservation_plan, expert_panel])
expert_panel_node = OperatorPOWL(operator=Operator.AND, children=[expert_panel, report_draft])
report_draft_node = OperatorPOWL(operator=Operator.AND, children=[report_draft, client_review])
client_review_node = OperatorPOWL(operator=Operator.AND, children=[client_review, authority_submit])
authority_submit_node = OperatorPOWL(operator=Operator.AND, children=[authority_submit, exhibit_setup])
exhibit_setup_node = OperatorPOWL(operator=Operator.AND, children=[exhibit_setup, final_approval])

# Define the partial order
root = StrictPartialOrder(nodes=[
    provenance_check_node, 
    material_scan_node, 
    radiocarbon_test_node, 
    style_compare_node, 
    database_query_node, 
    blockchain_prep_node, 
    legal_review_node, 
    ownership_audit_node, 
    conservation_plan_node, 
    expert_panel_node, 
    report_draft_node, 
    client_review_node, 
    authority_submit_node, 
    exhibit_setup_node, 
    final_approval
])

# Define the order between nodes
root.order.add_edge(provenance_check_node, material_scan_node)
root.order.add_edge(material_scan_node, radiocarbon_test_node)
root.order.add_edge(radiocarbon_test_node, style_compare_node)
root.order.add_edge(style_compare_node, database_query_node)
root.order.add_edge(database_query_node, blockchain_prep_node)
root.order.add_edge(blockchain_prep_node, legal_review_node)
root.order.add_edge(legal_review_node, ownership_audit_node)
root.order.add_edge(ownership_audit_node, conservation_plan_node)
root.order.add_edge(conservation_plan_node, expert_panel_node)
root.order.add_edge(expert_panel_node, report_draft_node)
root.order.add_edge(report_draft_node, client_review_node)
root.order.add_edge(client_review_node, authority_submit_node)
root.order.add_edge(authority_submit_node, exhibit_setup_node)
root.order.add_edge(exhibit_setup_node, final_approval)

# Print the root of the POWL model
print(root)