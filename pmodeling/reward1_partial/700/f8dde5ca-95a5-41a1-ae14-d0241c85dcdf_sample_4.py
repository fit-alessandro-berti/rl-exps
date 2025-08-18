import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

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

# Define the operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[database_query, blockchain_prep])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[legal_review, ownership_audit])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[conservation_plan, expert_panel])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[report_draft, client_review])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[authority_submit, exhibit_setup])

# Define the partial order
root = StrictPartialOrder(nodes=[provenance_check, material_scan, radiocarbon_test, style_compare, xor1, xor2, xor3, xor4, xor5, final_approval])

# Define the order dependencies
root.order.add_edge(provenance_check, material_scan)
root.order.add_edge(material_scan, radiocarbon_test)
root.order.add_edge(radiocarbon_test, style_compare)
root.order.add_edge(style_compare, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, final_approval)

print(root)