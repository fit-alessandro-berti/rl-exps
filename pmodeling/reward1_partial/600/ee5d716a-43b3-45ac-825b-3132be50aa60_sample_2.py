import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
verify_artwork = Transition(label='Verify Artwork')
analyze_provenance = Transition(label='Analyze Provenance')
set_reserve = Transition(label='Set Reserve')
activate_auction = Transition(label='Activate Auction')
monitor_bids = Transition(label='Monitor Bids')
adjust_pricing = Transition(label='Adjust Pricing')
enable_fractional = Transition(label='Enable Fractional')
validate_bidders = Transition(label='Validate Bidders')
resolve_disputes = Transition(label='Resolve Disputes')
distribute_royalties = Transition(label='Distribute Royalties')
promote_auction = Transition(label='Promote Auction')
process_payments = Transition(label='Process Payments')
confirm_ownership = Transition(label='Confirm Ownership')
arrange_shipping = Transition(label='Arrange Shipping')
track_delivery = Transition(label='Track Delivery')
report_analytics = Transition(label='Report Analytics')

# Define the loop for monitoring bids
loop_monitor_bids = OperatorPOWL(operator=Operator.LOOP, children=[monitor_bids])

# Define the exclusive choice for adjusting pricing and enabling fractional
xor_adjust_pricing_fractional = OperatorPOWL(operator=Operator.XOR, children=[adjust_pricing, enable_fractional])

# Define the exclusive choice for validating bidders and resolving disputes
xor_validate_bidders_disputes = OperatorPOWL(operator=Operator.XOR, children=[validate_bidders, resolve_disputes])

# Define the exclusive choice for distributing royalties and promoting auction
xor_distribute_royalties_promote_auction = OperatorPOWL(operator=Operator.XOR, children=[distribute_royalties, promote_auction])

# Define the exclusive choice for processing payments, confirming ownership, arranging shipping, tracking delivery, and reporting analytics
xor_payments_ownership_shipping_delivery_analytics = OperatorPOWL(operator=Operator.XOR, children=[process_payments, confirm_ownership, arrange_shipping, track_delivery, report_analytics])

# Define the partial order
root = StrictPartialOrder(nodes=[verify_artwork, analyze_provenance, set_reserve, activate_auction, loop_monitor_bids, xor_adjust_pricing_fractional, xor_validate_bidders_disputes, xor_distribute_royalties_promote_auction, xor_payments_ownership_shipping_delivery_analytics])
root.order.add_edge(verify_artwork, analyze_provenance)
root.order.add_edge(analyze_provenance, set_reserve)
root.order.add_edge(set_reserve, activate_auction)
root.order.add_edge(activate_auction, loop_monitor_bids)
root.order.add_edge(loop_monitor_bids, xor_adjust_pricing_fractional)
root.order.add_edge(xor_adjust_pricing_fractional, xor_validate_bidders_disputes)
root.order.add_edge(xor_validate_bidders_disputes, xor_distribute_royalties_promote_auction)
root.order.add_edge(xor_distribute_royalties_promote_auction, xor_payments_ownership_shipping_delivery_analytics)

print(root)