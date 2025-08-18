from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions
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

# Define the partial order
root = StrictPartialOrder(
    nodes=[
        verify_artwork,
        analyze_provenance,
        set_reserve,
        activate_auction,
        monitor_bids,
        adjust_pricing,
        enable_fractional,
        validate_bidders,
        resolve_disputes,
        distribute_royalties,
        promote_auction,
        process_payments,
        confirm_ownership,
        arrange_shipping,
        track_delivery,
        report_analytics
    ],
    order=[
        (verify_artwork, analyze_provenance),
        (analyze_provenance, set_reserve),
        (set_reserve, activate_auction),
        (activate_auction, monitor_bids),
        (monitor_bids, adjust_pricing),
        (adjust_pricing, enable_fractional),
        (enable_fractional, validate_bidders),
        (validate_bidders, resolve_disputes),
        (resolve_disputes, distribute_royalties),
        (distribute_royalties, promote_auction),
        (promote_auction, process_payments),
        (process_payments, confirm_ownership),
        (confirm_ownership, arrange_shipping),
        (arrange_shipping, track_delivery),
        (track_delivery, report_analytics)
    ]
)