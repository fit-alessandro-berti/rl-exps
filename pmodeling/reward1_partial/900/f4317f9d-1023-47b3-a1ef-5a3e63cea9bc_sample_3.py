import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the control flow operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[chemical_test, database_query])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[record_match, database_query])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[aging_verify, database_query])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[panel_review, database_query])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[forger_risk, database_query])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[market_value, database_query])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[report_draft, database_query])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[certification, database_query])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[approval_stage, database_query])
xor10 = OperatorPOWL(operator=Operator.XOR, children=[secure_packing, database_query])
xor11 = OperatorPOWL(operator=Operator.XOR, children=[transport_prep, database_query])

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    provenance_check, material_scan, style_compare, ai_imaging, xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8, xor9, xor10, xor11])

# Define the control flow dependencies
root.order.add_edge(provenance_check, material_scan)
root.order.add_edge(material_scan, style_compare)
root.order.add_edge(style_compare, ai_imaging)
root.order.add_edge(ai_imaging, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)
root.order.add_edge(xor8, xor9)
root.order.add_edge(xor9, xor10)
root.order.add_edge(xor10, xor11)
root.order.add_edge(xor11, certification)

# Print the root POWL model
print(root)