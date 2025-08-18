import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

asset_id = Transition(label='Asset ID')
value_assess = Transition(label='Value Assess')
risk_scan = Transition(label='Risk Scan')
market_review = Transition(label='Market Review')
initial_offer = Transition(label='Initial Offer')
counter_offer = Transition(label='Counter Offer')
negotiation = Transition(label='Negotiation')
contract_draft = Transition(label='Contract Draft')
legal_review = Transition(label='Legal Review')
digital_sign = Transition(label='Digital Sign')
royalty_setup = Transition(label='Royalty Setup')
transfer_record = Transition(label='Transfer Record')
compliance_check = Transition(label='Compliance Check')
audit_schedule = Transition(label='Audit Schedule')
market_feedback = Transition(label='Market Feedback')
strategy_update = Transition(label='Strategy Update')

skip = SilentTransition()

loop = OperatorPOWL(operator=Operator.LOOP, children=[
    asset_id,
    value_assess,
    risk_scan,
    market_review,
    initial_offer,
    counter_offer,
    negotiation
])

xor = OperatorPOWL(operator=Operator.XOR, children=[
    contract_draft,
    legal_review,
    digital_sign,
    royalty_setup,
    transfer_record
])

xor2 = OperatorPOWL(operator=Operator.XOR, children=[
    compliance_check,
    audit_schedule,
    market_feedback,
    strategy_update
])

root = StrictPartialOrder(nodes=[loop, xor, xor2])
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor2)