import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) for the process
provenance_check = Transition(label='Provenance Check')
material_scan = Transition(label='Material Scan')
style_compare = Transition(label='Style Compare')
ai_imaging = Transition(label='AI Imaging')
chemical_test = Transition(label='Chemical Test')
aging_verify = Transition(label='Aging Verify')
record_match = Transition(label='Record Match')
database_query = Transition(label='Database Query')
panel_review = Transition(label='Panel Review')
forger_risk = Transition(label='Forgery Risk')
market_value = Transition(label='Market Value')
report_draft = Transition(label='Report Draft')
certification = Transition(label='Certification')
approval_stage = Transition(label='Approval Stage')
secure_packing = Transition(label='Secure Packing')
transport_prep = Transition(label='Transport Prep')

# Define the loop and XOR nodes
# The loop node represents the sequential execution of 'Material Scan', 'Style Compare', 'AI Imaging', 'Chemical Test', and 'Aging Verify'.
loop = OperatorPOWL(operator=Operator.LOOP, children=[material_scan, style_compare, ai_imaging, chemical_test, aging_verify])
# The XOR node represents the choice between 'Record Match' and 'Database Query'.
xor = OperatorPOWL(operator=Operator.XOR, children=[record_match, database_query])
# The XOR node represents the choice between 'Panel Review' and 'Forgery Risk'.
xor2 = OperatorPOWL(operator=Operator.XOR, children=[panel_review, forger_risk])
# The XOR node represents the choice between 'Market Value' and 'Report Draft'.
xor3 = OperatorPOWL(operator=Operator.XOR, children=[market_value, report_draft])
# The XOR node represents the choice between 'Certification' and 'Approval Stage'.
xor4 = OperatorPOWL(operator=Operator.XOR, children=[certification, approval_stage])
# The XOR node represents the choice between 'Secure Packing' and 'Transport Prep'.
xor5 = OperatorPOWL(operator=Operator.XOR, children=[secure_packing, transport_prep])

# Define the partial order graph
root = StrictPartialOrder(nodes=[loop, xor, xor2, xor3, xor4, xor5])
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)

# Print the final POWL model
print(root)