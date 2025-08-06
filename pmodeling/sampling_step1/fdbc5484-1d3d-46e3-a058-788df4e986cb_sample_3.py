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

# Define silent transitions
skip = SilentTransition()

# Define partial order nodes
asset_id_node = StrictPartialOrder(nodes=[asset_id, value_assess, risk_scan, market_review, initial_offer, counter_offer, negotiation, contract_draft, legal_review, digital_sign, royalty_setup, transfer_record, compliance_check, audit_schedule, market_feedback, strategy_update])
asset_id_node.order.add_edge(asset_id, value_assess)
asset_id_node.order.add_edge(value_assess, risk_scan)
asset_id_node.order.add_edge(risk_scan, market_review)
asset_id_node.order.add_edge(market_review, initial_offer)
asset_id_node.order.add_edge(initial_offer, counter_offer)
asset_id_node.order.add_edge(counter_offer, negotiation)
asset_id_node.order.add_edge(negotiation, contract_draft)
asset_id_node.order.add_edge(contract_draft, legal_review)
asset_id_node.order.add_edge(legal_review, digital_sign)
asset_id_node.order.add_edge(digital_sign, royalty_setup)
asset_id_node.order.add_edge(royalty_setup, transfer_record)
asset_id_node.order.add_edge(transfer_record, compliance_check)
asset_id_node.order.add_edge(compliance_check, audit_schedule)
asset_id_node.order.add_edge(audit_schedule, market_feedback)
asset_id_node.order.add_edge(market_feedback, strategy_update)

# Set 'root' variable
root = asset_id_node