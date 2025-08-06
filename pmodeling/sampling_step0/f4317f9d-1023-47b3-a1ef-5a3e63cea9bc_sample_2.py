import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define the silent transitions
skip = SilentTransition()

# Define the POWL model
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[chemical_test, aging_verify, record_match, database_query])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[panel_review, forger_risk, market_value, approval_stage])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[report_draft, certification, secure_packing, transport_prep])

xor1 = OperatorPOWL(operator=Operator.XOR, children=[loop1, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[xor1, material_scan])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[xor2, style_compare])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[xor3, ai_imaging])

root = StrictPartialOrder(nodes=[xor4, provenance_check])
root.order.add_edge(xor4, provenance_check)

# Return the root of the POWL model
root