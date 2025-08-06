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

# Define silent transitions for empty labels
skip = SilentTransition()

# Define operators and partial order
loop_blockchain = OperatorPOWL(operator=Operator.LOOP, children=[blockchain_prep])
xor_legal_review = OperatorPOWL(operator=Operator.XOR, children=[legal_review, skip])
xor_style_compare = OperatorPOWL(operator=Operator.XOR, children=[style_compare, skip])
xor_ownership_audit = OperatorPOWL(operator=Operator.XOR, children=[ownership_audit, skip])
xor_conservation_plan = OperatorPOWL(operator=Operator.XOR, children=[conservation_plan, skip])
xor_exhibit_setup = OperatorPOWL(operator=Operator.XOR, children=[exhibit_setup, skip])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[
    provenance_check, 
    material_scan, 
    radiocarbon_test, 
    xor_style_compare,
    xor_ownership_audit,
    xor_conservation_plan,
    xor_exhibit_setup,
    loop_blockchain,
    xor_legal_review,
    expert_panel,
    report_draft,
    client_review,
    authority_submit,
    final_approval
])

# Define dependencies between nodes
root.order.add_edge(provenance_check, material_scan)
root.order.add_edge(material_scan, radiocarbon_test)
root.order.add_edge(radiocarbon_test, xor_style_compare)
root.order.add_edge(xor_style_compare, xor_ownership_audit)
root.order.add_edge(xor_ownership_audit, xor_conservation_plan)
root.order.add_edge(xor_conservation_plan, xor_exhibit_setup)
root.order.add_edge(xor_exhibit_setup, loop_blockchain)
root.order.add_edge(loop_blockchain, xor_legal_review)
root.order.add_edge(xor_legal_review, expert_panel)
root.order.add_edge(expert_panel, report_draft)
root.order.add_edge(report_draft, client_review)
root.order.add_edge(client_review, authority_submit)
root.order.add_edge(authority_submit, final_approval)

print(root)