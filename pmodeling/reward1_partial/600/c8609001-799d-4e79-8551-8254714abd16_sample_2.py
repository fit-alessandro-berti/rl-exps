import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

# Define the process model
provenance_check_node = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, skip])
material_test_node = OperatorPOWL(operator=Operator.XOR, children=[material_test, skip])
expert_consult_node = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, skip])
database_search_node = OperatorPOWL(operator=Operator.XOR, children=[database_search, skip])
condition_report_node = OperatorPOWL(operator=Operator.XOR, children=[condition_report, skip])
risk_assess_node = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, skip])
market_analysis_node = OperatorPOWL(operator=Operator.XOR, children=[market_analysis, skip])
stakeholder_meet_node = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_meet, skip])
legal_review_node = OperatorPOWL(operator=Operator.XOR, children=[legal_review, skip])
insurance_quote_node = OperatorPOWL(operator=Operator.XOR, children=[insurance_quote, skip])
price_negotiation_node = OperatorPOWL(operator=Operator.XOR, children=[price_negotiation, skip])
contract_draft_node = OperatorPOWL(operator=Operator.XOR, children=[contract_draft, skip])
final_approval_node = OperatorPOWL(operator=Operator.XOR, children=[final_approval, skip])
asset_registration_node = OperatorPOWL(operator=Operator.XOR, children=[asset_registration, skip])

# Define the partial order
root = StrictPartialOrder(nodes=[initial_review, provenance_check_node, material_test_node, expert_consult_node, database_search_node, condition_report_node, risk_assess_node, market_analysis_node, stakeholder_meet_node, legal_review_node, insurance_quote_node, price_negotiation_node, contract_draft_node, final_approval_node, asset_registration_node])
root.order.add_edge(initial_review, provenance_check_node)
root.order.add_edge(provenance_check_node, material_test_node)
root.order.add_edge(material_test_node, expert_consult_node)
root.order.add_edge(expert_consult_node, database_search_node)
root.order.add_edge(database_search_node, condition_report_node)
root.order.add_edge(condition_report_node, risk_assess_node)
root.order.add_edge(risk_assess_node, market_analysis_node)
root.order.add_edge(market_analysis_node, stakeholder_meet_node)
root.order.add_edge(stakeholder_meet_node, legal_review_node)
root.order.add_edge(legal_review_node, insurance_quote_node)
root.order.add_edge(insurance_quote_node, price_negotiation_node)
root.order.add_edge(price_negotiation_node, contract_draft_node)
root.order.add_edge(contract_draft_node, final_approval_node)
root.order.add_edge(final_approval_node, asset_registration_node)

# Print the root model
print(root)