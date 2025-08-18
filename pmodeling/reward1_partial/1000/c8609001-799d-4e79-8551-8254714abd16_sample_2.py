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

# Define partial order structure
root = StrictPartialOrder(
    nodes=[
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
    ],
    order={
        initial_review: provenance_check,
        provenance_check: material_test,
        material_test: expert_consult,
        expert_consult: database_search,
        database_search: condition_report,
        condition_report: risk_assess,
        risk_assess: market_analysis,
        market_analysis: stakeholder_meet,
        stakeholder_meet: legal_review,
        legal_review: insurance_quote,
        insurance_quote: price_negotiation,
        price_negotiation: contract_draft,
        contract_draft: final_approval,
        final_approval: asset_registration
    }
)