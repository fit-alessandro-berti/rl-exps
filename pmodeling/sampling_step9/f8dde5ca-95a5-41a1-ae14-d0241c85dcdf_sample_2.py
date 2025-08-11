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

# Define exclusive choice for legal review and ownership audit
xor = OperatorPOWL(operator=Operator.XOR, children=[legal_review, ownership_audit])

# Define loop for material scan and style compare
loop = OperatorPOWL(operator=Operator.LOOP, children=[material_scan, style_compare])

# Define partial order for all activities
root = StrictPartialOrder(nodes=[loop, xor, provenance_check, radiocarbon_test, database_query, blockchain_prep, conservation_plan, expert_panel, report_draft, client_review, authority_submit, exhibit_setup, final_approval])
root.order.add_edge(loop, xor)
root.order.add_edge(loop, provenance_check)
root.order.add_edge(loop, radiocarbon_test)
root.order.add_edge(loop, database_query)
root.order.add_edge(loop, blockchain_prep)
root.order.add_edge(loop, conservation_plan)
root.order.add_edge(loop, expert_panel)
root.order.add_edge(loop, report_draft)
root.order.add_edge(loop, client_review)
root.order.add_edge(loop, authority_submit)
root.order.add_edge(loop, exhibit_setup)
root.order.add_edge(loop, final_approval)