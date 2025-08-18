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
market_review_loop = OperatorPOWL(operator=Operator.LOOP, children=[initial_offer, counter_offer])
negotiation_xor = OperatorPOWL(operator=Operator.XOR, children=[negotiation, skip])
contract_draft_loop = OperatorPOWL(operator=Operator.LOOP, children=[contract_draft, legal_review])
legal_review_loop = OperatorPOWL(operator=Operator.LOOP, children=[legal_review, digital_sign])
royalty_setup_loop = OperatorPOWL(operator=Operator.LOOP, children=[royalty_setup, skip])
transfer_record_loop = OperatorPOWL(operator=Operator.LOOP, children=[transfer_record, compliance_check])
audit_schedule_loop = OperatorPOWL(operator=Operator.LOOP, children=[audit_schedule, market_feedback])
strategy_update_loop = OperatorPOWL(operator=Operator.LOOP, children=[strategy_update, skip])

# Define the root partial order
root = StrictPartialOrder(nodes=[asset_id, value_assess, risk_scan, market_review, market_review_loop, negotiation_xor, contract_draft, contract_draft_loop, legal_review, legal_review_loop, royalty_setup, royalty_setup_loop, transfer_record, transfer_record_loop, audit_schedule, audit_schedule_loop, market_feedback, strategy_update, strategy_update_loop])
root.order.add_edge(asset_id, value_assess)
root.order.add_edge(value_assess, risk_scan)
root.order.add_edge(risk_scan, market_review)
root.order.add_edge(market_review, market_review_loop)
root.order.add_edge(market_review_loop, negotiation_xor)
root.order.add_edge(negotiation_xor, contract_draft)
root.order.add_edge(contract_draft, contract_draft_loop)
root.order.add_edge(contract_draft_loop, legal_review)
root.order.add_edge(legal_review, legal_review_loop)
root.order.add_edge(legal_review_loop, royalty_setup)
root.order.add_edge(royalty_setup, royalty_setup_loop)
root.order.add_edge(royalty_setup_loop, transfer_record)
root.order.add_edge(transfer_record, transfer_record_loop)
root.order.add_edge(transfer_record_loop, audit_schedule)
root.order.add_edge(audit_schedule, audit_schedule_loop)
root.order.add_edge(audit_schedule_loop, market_feedback)
root.order.add_edge(market_feedback, strategy_update)
root.order.add_edge(strategy_update, strategy_update_loop)

print(root)