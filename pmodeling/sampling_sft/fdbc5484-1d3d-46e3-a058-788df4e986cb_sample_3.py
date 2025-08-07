import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
asset_id         = Transition(label='Asset ID')
value_assess     = Transition(label='Value Assess')
risk_scan        = Transition(label='Risk Scan')
market_review    = Transition(label='Market Review')
initial_offer    = Transition(label='Initial Offer')
counter_offer    = Transition(label='Counter Offer')
negotiation      = Transition(label='Negotiation')
contract_draft   = Transition(label='Contract Draft')
legal_review     = Transition(label='Legal Review')
digital_sign     = Transition(label='Digital Sign')
royalty_setup    = Transition(label='Royalty Setup')
transfer_record  = Transition(label='Transfer Record')
compliance_check = Transition(label='Compliance Check')
audit_schedule   = Transition(label='Audit Schedule')
market_feedback  = Transition(label='Market Feedback')
strategy_update  = Transition(label='Strategy Update')

# Loop for negotiation rounds
loop_negotiation = OperatorPOWL(
    operator=Operator.LOOP,
    children=[initial_offer, counter_offer, negotiation]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    asset_id,
    value_assess,
    risk_scan,
    market_review,
    loop_negotiation,
    contract_draft,
    legal_review,
    digital_sign,
    royalty_setup,
    transfer_record,
    compliance_check,
    audit_schedule,
    market_feedback,
    strategy_update
])

# Define the control-flow dependencies
root.order.add_edge(asset_id,     value_assess)
root.order.add_edge(value_assess, risk_scan)
root.order.add_edge(risk_scan,    market_review)
root.order.add_edge(market_review, loop_negotiation)

# After the negotiation loop, all subsequent activities are concurrent
for next_activity in [
    contract_draft,
    legal_review,
    digital_sign,
    royalty_setup,
    transfer_record,
    compliance_check,
    audit_schedule,
    market_feedback,
    strategy_update
]:
    root.order.add_edge(loop_negotiation, next_activity)

print(root)