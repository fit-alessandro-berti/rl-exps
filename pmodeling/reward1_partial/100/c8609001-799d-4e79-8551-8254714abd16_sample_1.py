import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the process
xor1 = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_meet, legal_review])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[market_analysis, insurance_quote])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[price_negotiation, contract_draft])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[final_approval, asset_registration])

# Define the partial order
root = StrictPartialOrder(nodes=[initial_review, provenance_check, material_test, expert_consult, database_search, condition_report, risk_assess, xor1, xor2, xor3, xor4])
root.order.add_edge(initial_review, provenance_check)
root.order.add_edge(provenance_check, material_test)
root.order.add_edge(material_test, expert_consult)
root.order.add_edge(expert_consult, database_search)
root.order.add_edge(database_search, condition_report)
root.order.add_edge(condition_report, risk_assess)
root.order.add_edge(risk_assess, xor1)
root.order.add_edge(risk_assess, xor2)
root.order.add_edge(risk_assess, xor3)
root.order.add_edge(risk_assess, xor4)
root.order.add_edge(xor1, legal_review)
root.order.add_edge(xor1, stakeholder_meet)
root.order.add_edge(xor2, insurance_quote)
root.order.add_edge(xor2, market_analysis)
root.order.add_edge(xor3, price_negotiation)
root.order.add_edge(xor3, contract_draft)
root.order.add_edge(xor4, final_approval)
root.order.add_edge(xor4, asset_registration)

print(root)