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

# Define silent transitions
skip = SilentTransition()

# Define the process
loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, material_scan])
loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[radiocarbon_test, style_compare])
xor_1 = OperatorPOWL(operator=Operator.XOR, children=[database_query, skip])
xor_2 = OperatorPOWL(operator=Operator.XOR, children=[blockchain_prep, legal_review])
xor_3 = OperatorPOWL(operator=Operator.XOR, children=[ownership_audit, conservation_plan])
xor_4 = OperatorPOWL(operator=Operator.XOR, children=[expert_panel, report_draft])
xor_5 = OperatorPOWL(operator=Operator.XOR, children=[client_review, authority_submit])
xor_6 = OperatorPOWL(operator=Operator.XOR, children=[exhibit_setup, final_approval])

root = StrictPartialOrder(nodes=[loop_1, loop_2, xor_1, xor_2, xor_3, xor_4, xor_5, xor_6])
root.order.add_edge(loop_1, xor_1)
root.order.add_edge(loop_2, xor_2)
root.order.add_edge(xor_1, xor_3)
root.order.add_edge(xor_2, xor_4)
root.order.add_edge(xor_3, xor_5)
root.order.add_edge(xor_4, xor_6)
root.order.add_edge(xor_5, xor_6)
root.order.add_edge(xor_6, xor_6)