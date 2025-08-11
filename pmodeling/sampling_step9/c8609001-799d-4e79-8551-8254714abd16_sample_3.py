import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define silent activities
skip = SilentTransition()

# Define exclusive choice (XOR) for expert consultation and database search
xor_expert_consult_db = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, database_search])

# Define loop for stakeholder meetings and legal reviews
loop_stakeholder_meet_legal_review = OperatorPOWL(operator=Operator.LOOP, children=[stakeholder_meet, legal_review])

# Define loop for insurance quotes and price negotiations
loop_insurance_quote_price_negotiation = OperatorPOWL(operator=Operator.LOOP, children=[insurance_quote, price_negotiation])

# Define loop for contract drafts and final approvals
loop_contract_draft_final_approval = OperatorPOWL(operator=Operator.LOOP, children=[contract_draft, final_approval])

# Define the POWL model
root = StrictPartialOrder(nodes=[
    initial_review,
    provenance_check,
    material_test,
    xor_expert_consult_db,
    loop_stakeholder_meet_legal_review,
    loop_insurance_quote_price_negotiation,
    loop_contract_draft_final_approval,
    asset_registration
])

# Add edges between nodes
root.order.add_edge(initial_review, provenance_check)
root.order.add_edge(provenance_check, material_test)
root.order.add_edge(material_test, xor_expert_consult_db)
root.order.add_edge(xor_expert_consult_db, loop_stakeholder_meet_legal_review)
root.order.add_edge(loop_stakeholder_meet_legal_review, loop_insurance_quote_price_negotiation)
root.order.add_edge(loop_insurance_quote_price_negotiation, loop_contract_draft_final_approval)
root.order.add_edge(loop_contract_draft_final_approval, asset_registration)

print(root)