import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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
skip = SilentTransition()

# Define loops and choices
panel_review_loop = OperatorPOWL(operator=Operator.LOOP, children=[panel_review, approval_stage])
market_value_loop = OperatorPOWL(operator=Operator.LOOP, children=[market_value, certification])
transport_prep_loop = OperatorPOWL(operator=Operator.LOOP, children=[transport_prep, secure_packing])

# Define the root node
root = StrictPartialOrder(nodes=[panel_review_loop, market_value_loop, transport_prep_loop])
root.order.add_edge(panel_review_loop, market_value_loop)
root.order.add_edge(market_value_loop, transport_prep_loop)

# Print the root node
print(root)