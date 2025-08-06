import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with exact names
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

# Define the silent transitions (tau labels)
skip = SilentTransition()

# Define the loop nodes
loop_blockchain = OperatorPOWL(operator=Operator.LOOP, children=[blockchain_prep, legal_review])
loop_ownership = OperatorPOWL(operator=Operator.LOOP, children=[ownership_audit, conservation_plan, expert_panel])

# Define the partial order
root = StrictPartialOrder(nodes=[provenance_check, material_scan, radiocarbon_test, style_compare, database_query, loop_blockchain, loop_ownership, report_draft, client_review, authority_submit, exhibit_setup, final_approval])

# Define the order of transitions
root.order.add_edge(provenance_check, material_scan)
root.order.add_edge(material_scan, radiocarbon_test)
root.order.add_edge(radiocarbon_test, style_compare)
root.order.add_edge(style_compare, database_query)
root.order.add_edge(database_query, loop_blockchain)
root.order.add_edge(loop_blockchain, loop_ownership)
root.order.add_edge(loop_ownership, report_draft)
root.order.add_edge(report_draft, client_review)
root.order.add_edge(client_review, authority_submit)
root.order.add_edge(authority_submit, exhibit_setup)
root.order.add_edge(exhibit_setup, final_approval)

print(root)