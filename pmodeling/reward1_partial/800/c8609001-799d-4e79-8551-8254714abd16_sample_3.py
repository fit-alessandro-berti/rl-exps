import pm4py
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

skip = SilentTransition()

provenance_check_loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check])
material_test_loop = OperatorPOWL(operator=Operator.LOOP, children=[material_test])
risk_assess_loop = OperatorPOWL(operator=Operator.LOOP, children=[risk_assess])
market_analysis_loop = OperatorPOWL(operator=Operator.LOOP, children=[market_analysis])
stakeholder_meet_loop = OperatorPOWL(operator=Operator.LOOP, children=[stakeholder_meet])
legal_review_loop = OperatorPOWL(operator=Operator.LOOP, children=[legal_review])
insurance_quote_loop = OperatorPOWL(operator=Operator.LOOP, children=[insurance_quote])
price_negotiation_loop = OperatorPOWL(operator=Operator.LOOP, children=[price_negotiation])
contract_draft_loop = OperatorPOWL(operator=Operator.LOOP, children=[contract_draft])
final_approval_loop = OperatorPOWL(operator=Operator.LOOP, children=[final_approval])

root = StrictPartialOrder(nodes=[initial_review, provenance_check_loop, material_test_loop, expert_consult, database_search, condition_report, risk_assess_loop, market_analysis_loop, stakeholder_meet_loop, legal_review_loop, insurance_quote_loop, price_negotiation_loop, contract_draft_loop, final_approval_loop, asset_registration])
root.order.add_edge(initial_review, provenance_check_loop)
root.order.add_edge(provenance_check_loop, material_test_loop)
root.order.add_edge(material_test_loop, expert_consult)
root.order.add_edge(expert_consult, database_search)
root.order.add_edge(database_search, condition_report)
root.order.add_edge(condition_report, risk_assess_loop)
root.order.add_edge(risk_assess_loop, market_analysis_loop)
root.order.add_edge(market_analysis_loop, stakeholder_meet_loop)
root.order.add_edge(stakeholder_meet_loop, legal_review_loop)
root.order.add_edge(legal_review_loop, insurance_quote_loop)
root.order.add_edge(insurance_quote_loop, price_negotiation_loop)
root.order.add_edge(price_negotiation_loop, contract_draft_loop)
root.order.add_edge(contract_draft_loop, final_approval_loop)
root.order.add_edge(final_approval_loop, asset_registration)

# Print the final POWL model
print(root)