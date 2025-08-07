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

# Define the POWL model
root = StrictPartialOrder(nodes=[asset_id, value_assess, risk_scan, market_review, initial_offer, counter_offer, negotiation, contract_draft, legal_review, digital_sign, royalty_setup, transfer_record, compliance_check, audit_schedule, market_feedback, strategy_update])

# Add dependencies if any (in this case, no dependencies are mentioned in the problem description)
# root.order.add_edge(asset_id, value_assess)
# root.order.add_edge(asset_id, risk_scan)
# root.order.add_edge(asset_id, market_review)
# root.order.add_edge(asset_id, initial_offer)
# root.order.add_edge(asset_id, counter_offer)
# root.order.add_edge(asset_id, negotiation)
# root.order.add_edge(asset_id, contract_draft)
# root.order.add_edge(asset_id, legal_review)
# root.order.add_edge(asset_id, digital_sign)
# root.order.add_edge(asset_id, royalty_setup)
# root.order.add_edge(asset_id, transfer_record)
# root.order.add_edge(asset_id, compliance_check)
# root.order.add_edge(asset_id, audit_schedule)
# root.order.add_edge(asset_id, market_feedback)
# root.order.add_edge(asset_id, strategy_update)

# Print the root of the POWL model
print(root)