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

# Define the partial order
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

# Add dependencies if needed
# For example, if Material Scan depends on Provenance Check:
root.order.add_edge(provenance_check, material_scan)

# If you want to add more dependencies, you can do so similarly.
# For instance, if Style Compare depends on Database Query:
# root.order.add_edge(database_query, style_compare)

# If there are concurrent activities, you can define them as silent transitions.
# For example, if Blockchain Prep and Legal Review can be done concurrently:
# blockchain_prep = SilentTransition()
# legal_review = SilentTransition()
# root.nodes.extend([blockchain_prep, legal_review])
# root.order.add_edge(provenance_check, material_scan)
# root.order.add_edge(material_scan, radiocarbon_test)
# root.order.add_edge(material_scan, style_compare)
# root.order.add_edge(material_scan, database_query)
# root.order.add_edge(database_query, expert_panel)
# root.order.add_edge(database_query, client_review)
# root.order.add_edge(database_query, authority_submit)
# root.order.add_edge(database_query, exhibit_setup)
# root.order.add_edge(database_query, final_approval)

# This is the final POWL model
print(root)