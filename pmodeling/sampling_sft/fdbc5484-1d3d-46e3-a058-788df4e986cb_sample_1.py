import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
asset_id       = Transition(label='Asset ID')
value_assess   = Transition(label='Value Assess')
risk_scan      = Transition(label='Risk Scan')
market_review  = Transition(label='Market Review')
initial_offer  = Transition(label='Initial Offer')
counter_offer  = Transition(label='Counter Offer')
negotiation    = Transition(label='Negotiation')
contract_draft = Transition(label='Contract Draft')
legal_review   = Transition(label='Legal Review')
digital_sign   = Transition(label='Digital Sign')
royalty_setup  = Transition(label='Royalty Setup')
transfer_record= Transition(label='Transfer Record')
compliance_check=Transition(label='Compliance Check')
audit_schedule = Transition(label='Audit Schedule')
market_feedback=Transition(label='Market Feedback')
strategy_update=Transition(label='Strategy Update')

# Define the audit loop: audit_schedule followed by either compliance_check or skip
audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[audit_schedule, compliance_check])

# Build the top-level partial order
root = StrictPartialOrder(nodes=[
    asset_id, value_assess, risk_scan, market_review,
    initial_offer, counter_offer, negotiation,
    contract_draft, legal_review, digital_sign,
    royalty_setup, transfer_record, audit_loop,
    market_feedback, strategy_update
])

# Define the sequence of activities
root.order.add_edge(asset_id, value_assess)
root.order.add_edge(asset_id, risk_scan)
root.order.add_edge(value_assess, market_review)
root.order.add_edge(risk_scan, market_review)
root.order.add_edge(market_review, initial_offer)
root.order.add_edge(initial_offer, counter_offer)
root.order.add_edge(counter_offer, negotiation)
root.order.add_edge(negotiation, contract_draft)
root.order.add_edge(contract_draft, legal_review)
root.order.add_edge(legal_review, digital_sign)
root.order.add_edge(digital_sign, royalty_setup)
root.order.add_edge(royalty_setup, transfer_record)
root.order.add_edge(transfer_record, audit_loop)
root.order.add_edge(audit_loop, market_feedback)
root.order.add_edge(market_feedback, strategy_update)

# Print the root model for verification
print(root)