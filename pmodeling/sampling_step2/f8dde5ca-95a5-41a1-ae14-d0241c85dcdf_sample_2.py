import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define the partial order model
root = StrictPartialOrder(nodes=[provenance_check, material_scan, radiocarbon_test, style_compare, database_query, blockchain_prep, legal_review, ownership_audit, conservation_plan, expert_panel, report_draft, client_review, authority_submit, exhibit_setup, final_approval])

# Define the dependencies
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