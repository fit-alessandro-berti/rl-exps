import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[
    asset_id,
    value_assess,
    risk_scan,
    market_review,
    initial_offer,
    counter_offer,
    negotiation,
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

# Since the activities are sequential, we don't need to define any dependencies
# between them as they are already in the correct order.
# The 'root' variable now contains the POWL model for the described process.

# The final result is saved in the variable 'root'.