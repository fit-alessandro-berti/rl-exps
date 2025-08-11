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

# Define the silent transitions
skip = SilentTransition()

# Define the loops and XORs
loop_provenance = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, material_scan, style_compare, ai_imaging, chemical_test, aging_verify, record_match, database_query])
loop_auth = OperatorPOWL(operator=Operator.LOOP, children=[panel_review, forger_risk, market_value, report_draft])
xor_approval = OperatorPOWL(operator=Operator.XOR, children=[approval_stage, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[loop_provenance, loop_auth, xor_approval])
root.order.add_edge(loop_provenance, loop_auth)
root.order.add_edge(loop_provenance, xor_approval)
root.order.add_edge(loop_auth, xor_approval)

# Print the POWL model
print(root)