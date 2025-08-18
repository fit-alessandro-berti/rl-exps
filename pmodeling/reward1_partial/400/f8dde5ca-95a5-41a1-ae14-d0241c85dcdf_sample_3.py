import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the process
provenance_check_node = StrictPartialOrder(nodes=[provenance_check])
material_scan_node = StrictPartialOrder(nodes=[material_scan])
radiocarbon_test_node = StrictPartialOrder(nodes=[radiocarbon_test])
style_compare_node = StrictPartialOrder(nodes=[style_compare])
database_query_node = StrictPartialOrder(nodes=[database_query])
blockchain_prep_node = StrictPartialOrder(nodes=[blockchain_prep])
legal_review_node = StrictPartialOrder(nodes=[legal_review])
ownership_audit_node = StrictPartialOrder(nodes=[ownership_audit])
conservation_plan_node = StrictPartialOrder(nodes=[conservation_plan])
expert_panel_node = StrictPartialOrder(nodes=[expert_panel])
report_draft_node = StrictPartialOrder(nodes=[report_draft])
client_review_node = StrictPartialOrder(nodes=[client_review])
authority_submit_node = StrictPartialOrder(nodes=[authority_submit])
exhibit_setup_node = StrictPartialOrder(nodes=[exhibit_setup])
final_approval_node = StrictPartialOrder(nodes=[final_approval])

# Define the control flow
provenance_check_node.order.add_edge(provenance_check_node, material_scan_node)
provenance_check_node.order.add_edge(provenance_check_node, radiocarbon_test_node)
provenance_check_node.order.add_edge(provenance_check_node, style_compare_node)
provenance_check_node.order.add_edge(provenance_check_node, database_query_node)
provenance_check_node.order.add_edge(provenance_check_node, blockchain_prep_node)
provenance_check_node.order.add_edge(provenance_check_node, legal_review_node)
provenance_check_node.order.add_edge(provenance_check_node, ownership_audit_node)
provenance_check_node.order.add_edge(provenance_check_node, conservation_plan_node)
provenance_check_node.order.add_edge(provenance_check_node, expert_panel_node)
provenance_check_node.order.add_edge(provenance_check_node, report_draft_node)
provenance_check_node.order.add_edge(provenance_check_node, client_review_node)
provenance_check_node.order.add_edge(provenance_check_node, authority_submit_node)
provenance_check_node.order.add_edge(provenance_check_node, exhibit_setup_node)
provenance_check_node.order.add_edge(provenance_check_node, final_approval_node)

# Set the root
root = provenance_check_node

print(root)