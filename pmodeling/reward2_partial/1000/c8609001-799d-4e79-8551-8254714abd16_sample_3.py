from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the process
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

# Define the partial order
root = StrictPartialOrder(nodes=[
    initial_review, provenance_check, material_test, expert_consult,
    database_search, condition_report, risk_assess, market_analysis,
    stakeholder_meet, legal_review, insurance_quote, price_negotiation,
    contract_draft, final_approval, asset_registration
])

# Define the order dependencies
root.order.add_edge(initial_review, provenance_check)
root.order.add_edge(provenance_check, material_test)
root.order.add_edge(material_test, expert_consult)
root.order.add_edge(expert_consult, database_search)
root.order.add_edge(database_search, condition_report)
root.order.add_edge(condition_report, risk_assess)
root.order.add_edge(risk_assess, market_analysis)
root.order.add_edge(market_analysis, stakeholder_meet)
root.order.add_edge(stakeholder_meet, legal_review)
root.order.add_edge(legal_review, insurance_quote)
root.order.add_edge(insurance_quote, price_negotiation)
root.order.add_edge(price_negotiation, contract_draft)
root.order.add_edge(contract_draft, final_approval)
root.order.add_edge(final_approval, asset_registration)

# Print the POWL model
print(root)