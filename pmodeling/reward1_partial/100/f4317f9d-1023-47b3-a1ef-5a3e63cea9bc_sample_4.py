import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define the exclusive choice for Material Scan and AI Imaging
exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[material_scan, ai_imaging])

# Define the loop for Chemical Test and Record Match
loop_chemical_record = OperatorPOWL(operator=Operator.LOOP, children=[chemical_test, record_match])

# Define the exclusive choice for Database Query and Panel Review
exclusive_choice_2 = OperatorPOWL(operator=Operator.XOR, children=[database_query, panel_review])

# Define the loop for Forger Risk and Market Value
loop_forger_market = OperatorPOWL(operator=Operator.LOOP, children=[forger_risk, market_value])

# Define the exclusive choice for Report Draft and Certification
exclusive_choice_3 = OperatorPOWL(operator=Operator.XOR, children=[report_draft, certification])

# Define the exclusive choice for Approval Stage and Secure Packing
exclusive_choice_4 = OperatorPOWL(operator=Operator.XOR, children=[approval_stage, secure_packing])

# Define the exclusive choice for Transport Prep and Final Actions
exclusive_choice_5 = OperatorPOWL(operator=Operator.XOR, children=[transport_prep, exclusive_choice_4])

# Define the root partial order
root = StrictPartialOrder(nodes=[exclusive_choice, loop_chemical_record, exclusive_choice_2, loop_forger_market, exclusive_choice_3, exclusive_choice_5])
root.order.add_edge(exclusive_choice, loop_chemical_record)
root.order.add_edge(exclusive_choice, exclusive_choice_2)
root.order.add_edge(loop_chemical_record, exclusive_choice_2)
root.order.add_edge(exclusive_choice_2, loop_forger_market)
root.order.add_edge(loop_forger_market, exclusive_choice_3)
root.order.add_edge(exclusive_choice_3, exclusive_choice_4)
root.order.add_edge(exclusive_choice_4, exclusive_choice_5)
root.order.add_edge(exclusive_choice_5, transport_prep)