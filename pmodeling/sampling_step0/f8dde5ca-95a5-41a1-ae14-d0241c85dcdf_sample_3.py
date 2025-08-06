import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define the POWL model
root = StrictPartialOrder()

# Add activities to the model
root.nodes.append(provenance_check)
root.nodes.append(material_scan)
root.nodes.append(radiocarbon_test)
root.nodes.append(style_compare)
root.nodes.append(database_query)
root.nodes.append(blockchain_prep)
root.nodes.append(legal_review)
root.nodes.append(ownership_audit)
root.nodes.append(conservation_plan)
root.nodes.append(expert_panel)
root.nodes.append(report_draft)
root.nodes.append(client_review)
root.nodes.append(authority_submit)
root.nodes.append(exhibit_setup)
root.nodes.append(final_approval)

# Define the structure of the POWL model
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

# Add the loop for the expert panel
expert_panel_loop = OperatorPOWL(operator=Operator.LOOP, children=[expert_panel])
root.nodes.append(expert_panel_loop)
root.order.add_edge(root.nodes[13], expert_panel_loop)
root.order.add_edge(expert_panel_loop, expert_panel)

# Add the XOR for the authority submit and final approval
authority_submit_xor = OperatorPOWL(operator=Operator.XOR, children=[authority_submit, final_approval])
root.nodes.append(authority_submit_xor)
root.order.add_edge(root.nodes[14], authority_submit_xor)
root.order.add_edge(root.nodes[15], authority_submit_xor)

# Print the root of the POWL model
print(root)