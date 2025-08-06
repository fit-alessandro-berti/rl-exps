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

# Provenance Check and Material Test are mutually exclusive
xor_provenance_material = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, material_test])

# Expert Consult, Database Search, Condition Report, and Risk Assess are mutually exclusive
xor_expert_database_condition_risk = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, database_search, condition_report, risk_assess])

# Market Analysis, Stakeholder Meet, Legal Review, Insurance Quote, Price Negotiation, and Contract Draft are mutually exclusive
xor_market_stakeholder_legal_insurance_price_draft = OperatorPOWL(operator=Operator.XOR, children=[market_analysis, stakeholder_meet, legal_review, insurance_quote, price_negotiation, contract_draft])

# Final Approval and Asset Registration are mutually exclusive
xor_final_approval_asset_registration = OperatorPOWL(operator=Operator.XOR, children=[final_approval, asset_registration])

# Loop node to repeat the process until final approval
loop = OperatorPOWL(operator=Operator.LOOP, children=[xor_provenance_material, xor_expert_database_condition_risk, xor_market_stakeholder_legal_insurance_price_draft, xor_final_approval_asset_registration])

# Connect the loop node to the final approval node
root = StrictPartialOrder(nodes=[loop, xor_final_approval_asset_registration])
root.order.add_edge(loop, xor_final_approval_asset_registration)

print(root)