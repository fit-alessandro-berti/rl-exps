from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions for each activity
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

# Define the root of the POWL model as a strict partial order
root = StrictPartialOrder(nodes=[
    initial_review,
    provenance_check,
    material_test,
    expert_consult,
    database_search,
    condition_report,
    risk_assess,
    market_analysis,
    stakeholder_meet,
    legal_review,
    insurance_quote,
    price_negotiation,
    contract_draft,
    final_approval,
    asset_registration
])

# Optionally, if there are any dependencies between activities, you can add them like this:
# root.order.add_edge(initial_review, provenance_check)
# root.order.add_edge(initial_review, material_test)
# root.order.add_edge(initial_review, expert_consult)
# root.order.add_edge(initial_review, database_search)
# root.order.add_edge(initial_review, condition_report)
# root.order.add_edge(initial_review, risk_assess)
# root.order.add_edge(initial_review, market_analysis)
# root.order.add_edge(initial_review, stakeholder_meet)
# root.order.add_edge(initial_review, legal_review)
# root.order.add_edge(initial_review, insurance_quote)
# root.order.add_edge(initial_review, price_negotiation)
# root.order.add_edge(initial_review, contract_draft)
# root.order.add_edge(initial_review, final_approval)
# root.order.add_edge(initial_review, asset_registration)

# Now 'root' contains the POWL model for the process.