import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for the POWL model
initial_review = Transition(label='Initial Review')
provenance_check = Transition(label='Provenance Check')
material_test = Transition(label='Material Test')
expert_consult = Transition(label='Expert Consult')
database_search = Transition(label='Database Search')
condition_report = Transition(label='Condition Report')
risk_assess = Transition(label='Risk Assess')
market_analysis = Transition(label='Market Analysis')
stakeholder_meet = Transition(label='Stakeholder Meet')
legal_review = Transition(label='Legal Review')
insurance_quote = Transition(label='Insurance Quote')
price_negotiation = Transition(label='Price Negotiation')
contract_draft = Transition(label='Contract Draft')
final_approval = Transition(label='Final Approval')
asset_registration = Transition(label='Asset Registration')

# Define the silent transitions for the POWL model
skip1 = SilentTransition()
skip2 = SilentTransition()
skip3 = SilentTransition()
skip4 = SilentTransition()
skip5 = SilentTransition()
skip6 = SilentTransition()

# Define the loop nodes for the POWL model
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[stakeholder_meet, insurance_quote])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[market_analysis, condition_report])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[legal_review, risk_assess])

# Define the XOR nodes for the POWL model
xor1 = OperatorPOWL(operator=Operator.XOR, children=[initial_review, provenance_check])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[material_test, expert_consult])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[database_search, skip1])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[price_negotiation, skip2])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[contract_draft, skip3])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[final_approval, skip4])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[asset_registration, skip5])

# Define the root POWL model
root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5, xor6, xor7, loop1, loop2, loop3])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor1, xor3)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, loop1)
root.order.add_edge(xor7, loop2)
root.order.add_edge(xor7, loop3)
root.order.add_edge(loop1, xor7)
root.order.add_edge(loop2, xor7)
root.order.add_edge(loop3, xor7)