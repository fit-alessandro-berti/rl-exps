import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transition
skip = SilentTransition()

# Define the POWL model
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, material_test, expert_consult, database_search, condition_report, risk_assess, market_analysis])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[stakeholder_meet, legal_review, insurance_quote, price_negotiation, contract_draft, final_approval])
xor = OperatorPOWL(operator=Operator.XOR, children=[asset_registration, skip])
root = StrictPartialOrder(nodes=[loop1, loop2, xor])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, xor)

print(root)