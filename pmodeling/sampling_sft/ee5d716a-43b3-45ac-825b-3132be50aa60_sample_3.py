import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
verify_art = Transition(label='Verify Artwork')
analyze_prov = Transition(label='Analyze Provenance')
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

# Loop for monitoring bids: Monitor Bids, then optionally Adjust Pricing and Enable Fractional
bid_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor_bids, adjust_pricing, enable_fractional])

# Build the partial order
root = StrictPartialOrder(nodes=[
    verify_art,
    analyze_prov,
    set_reserve,
    activate_auction,
    bid_loop,
    validate_bidders,
    resolve_disputes,
    distribute_royalties,
    promote_auction,
    process_payments,
    confirm_ownership,
    arrange_shipping,
    track_delivery,
    report_analytics
])

# Define the control-flow dependencies
root.order.add_edge(verify_art, analyze_prov)
root.order.add_edge(analyze_prov, set_reserve)
root.order.add_edge(set_reserve, activate_auction)
root.order.add_edge(activate_auction, bid_loop)
root.order.add_edge(bid_loop, validate_bidders)
root.order.add_edge(validate_bidders, resolve_disputes)
root.order.add_edge(resolve_disputes, distribute_royalties)
root.order.add_edge(distribute_royalties, promote_auction)
root.order.add_edge(promote_auction, process_payments)
root.order.add_edge(process_payments, confirm_ownership)
root.order.add_edge(confirm_ownership, arrange_shipping)
root.order.add_edge(arrange_shipping, track_delivery)
root.order.add_edge(track_delivery, report_analytics)