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

# Define the process structure
loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, material_scan, radiocarbon_test])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[style_compare, database_query])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[blockchain_prep, legal_review])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[ownership_audit, conservation_plan])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[expert_panel, report_draft])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[client_review, authority_submit])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[exhibit_setup, final_approval])

root = StrictPartialOrder(nodes=[loop, xor1, xor2, xor3, xor4, xor5, xor6])
root.order.add_edge(loop, xor1)
root.order.add_edge(loop, xor2)
root.order.add_edge(loop, xor3)
root.order.add_edge(loop, xor4)
root.order.add_edge(loop, xor5)
root.order.add_edge(loop, xor6)

print(root)