import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
verify_artwork     = Transition(label='Verify Artwork')
analyze_provenance = Transition(label='Analyze Provenance')
set_reserve        = Transition(label='Set Reserve')
activate_auction   = Transition(label='Activate Auction')
monitor_bids       = Transition(label='Monitor Bids')
adjust_pricing     = Transition(label='Adjust Pricing')
enable_fractional  = Transition(label='Enable Fractional')
validate_bidders   = Transition(label='Validate Bidders')
resolve_disputes   = Transition(label='Resolve Disputes')
distribute_royalties = Transition(label='Distribute Royalties')
promote_auction    = Transition(label='Promote Auction')
process_payments   = Transition(label='Process Payments')
confirm_ownership  = Transition(label='Confirm Ownership')
arrange_shipping   = Transition(label='Arrange Shipping')
track_delivery     = Transition(label='Track Delivery')
report_analytics   = Transition(label='Report Analytics')

# Define the auction core loop: Monitor Bids -> Adjust Pricing -> Enable Fractional
auction_core = StrictPartialOrder(nodes=[monitor_bids, adjust_pricing, enable_fractional])
auction_core.order.add_edge(monitor_bids, adjust_pricing)
auction_core.order.add_edge(adjust_pricing, enable_fractional)

# Define the dispute resolution loop: Resolve Disputes -> Validate Bidders
dispute_loop = OperatorPOWL(operator=Operator.LOOP, children=[resolve_disputes, validate_bidders])

# Build the overall root partial order
root = StrictPartialOrder(nodes=[
    verify_artwork,
    analyze_provenance,
    set_reserve,
    activate_auction,
    auction_core,
    dispute_loop,
    distribute_royalties,
    promote_auction,
    process_payments,
    confirm_ownership,
    arrange_shipping,
    track_delivery,
    report_analytics
])

# Add edges defining the control-flow relationships
root.order.add_edge(verify_artwork, analyze_provenance)
root.order.add_edge(analyze_provenance, set_reserve)
root.order.add_edge(set_reserve, activate_auction)
root.order.add_edge(activate_auction, auction_core)
root.order.add_edge(auction_core, dispute_loop)
root.order.add_edge(dispute_loop, distribute_royalties)
root.order.add_edge(distribute_royalties, promote_auction)
root.order.add_edge(promote_auction, process_payments)
root.order.add_edge(process_payments, confirm_ownership)
root.order.add_edge(confirm_ownership, arrange_shipping)
root.order.add_edge(arrange_shipping, track_delivery)
root.order.add_edge(track_delivery, report_analytics)