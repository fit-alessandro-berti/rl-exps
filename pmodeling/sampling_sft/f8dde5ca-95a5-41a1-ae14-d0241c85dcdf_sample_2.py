import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
provenance_check    = Transition(label='Provenance Check')
material_scan       = Transition(label='Material Scan')
radiocarbon_test    = Transition(label='Radiocarbon Test')
style_compare       = Transition(label='Style Compare')
database_query      = Transition(label='Database Query')
blockchain_prep     = Transition(label='Blockchain Prep')
legal_review        = Transition(label='Legal Review')
ownership_audit     = Transition(label='Ownership Audit')
conservation_plan   = Transition(label='Conservation Plan')
expert_panel        = Transition(label='Expert Panel')
report_draft        = Transition(label='Report Draft')
client_review       = Transition(label='Client Review')
authority_submit    = Transition(label='Authority Submit')
exhibit_setup       = Transition(label='Exhibit Setup')
final_approval      = Transition(label='Final Approval')

# Build the loop body: Legal Review -> Ownership Audit -> Conservation Plan
body = StrictPartialOrder(nodes=[legal_review, ownership_audit, conservation_plan])
body.order.add_edge(legal_review, ownership_audit)
body.order.add_edge(ownership_audit, conservation_plan)

# LOOP operator: do Material Scan, then optionally repeat body
loop = OperatorPOWL(operator=Operator.LOOP, children=[material_scan, body])

# Build the root partial order
root = StrictPartialOrder(nodes=[
    provenance_check,
    loop,
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

# Add control-flow edges
root.order.add_edge(provenance_check, loop)
root.order.add_edge(loop, style_compare)
root.order.add_edge(loop, database_query)
root.order.add_edge(loop, blockchain_prep)
root.order.add_edge(style_compare, expert_panel)
root.order.add_edge(database_query, expert_panel)
root.order.add_edge(blockchain_prep, expert_panel)
root.order.add_edge(expert_panel, report_draft)
root.order.add_edge(report_draft, client_review)
root.order.add_edge(client_review, authority_submit)
root.order.add_edge(authority_submit, exhibit_setup)
root.order.add_edge(exhibit_setup, final_approval)