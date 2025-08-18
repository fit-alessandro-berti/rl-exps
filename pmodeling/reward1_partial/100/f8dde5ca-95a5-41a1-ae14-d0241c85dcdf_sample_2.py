from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions (activities) with their names
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

# Define the silent transition
skip = SilentTransition()

# Define the partial order structure
loop = OperatorPOWL(operator=Operator.LOOP, children=[material_scan, radiocarbon_test, style_compare, database_query])
xor = OperatorPOWL(operator=Operator.XOR, children=[blockchain_prep, legal_review, ownership_audit, conservation_plan])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[expert_panel, report_draft, client_review, authority_submit])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[exhibit_setup, final_approval])

# Create the root node
root = StrictPartialOrder(nodes=[loop, xor, xor2, xor3])
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)

print(root)