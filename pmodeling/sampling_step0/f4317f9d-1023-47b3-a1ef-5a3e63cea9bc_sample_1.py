import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define silent transitions
skip = SilentTransition()

# Define loop nodes
loop_material = OperatorPOWL(operator=Operator.LOOP, children=[material_scan, style_compare, ai_imaging])
loop_aging = OperatorPOWL(operator=Operator.LOOP, children=[aging_verify, record_match, database_query])
loop_panel = OperatorPOWL(operator=Operator.LOOP, children=[panel_review, forger_risk, market_value])
loop_report = OperatorPOWL(operator=Operator.LOOP, children=[report_draft, certification, approval_stage])
loop_transport = OperatorPOWL(operator=Operator.LOOP, children=[secure_packing, transport_prep])

# Define exclusive choice nodes
xor1 = OperatorPOWL(operator=Operator.XOR, children=[loop_material, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[loop_aging, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[loop_panel, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[loop_report, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[loop_transport, skip])

# Define the root node
root = StrictPartialOrder(nodes=[provenance_check, xor1, xor2, xor3, xor4, xor5])
root.order.add_edge(provenance_check, xor1)
root.order.add_edge(provenance_check, xor2)
root.order.add_edge(provenance_check, xor3)
root.order.add_edge(provenance_check, xor4)
root.order.add_edge(provenance_check, xor5)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, loop_transport)