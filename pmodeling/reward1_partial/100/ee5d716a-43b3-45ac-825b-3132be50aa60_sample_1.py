import pm4py

# Define transitions (activities)
verify_artwork = pm4py.objects.powl.obj.Transition(label='Verify Artwork')
analyze_provenance = pm4py.objects.powl.obj.Transition(label='Analyze Provenance')
set_reserve = pm4py.objects.powl.obj.Transition(label='Set Reserve')
activate_auction = pm4py.objects.powl.obj.Transition(label='Activate Auction')
monitor_bids = pm4py.objects.powl.obj.Transition(label='Monitor Bids')
adjust_pricing = pm4py.objects.powl.obj.Transition(label='Adjust Pricing')
enable_fractional = pm4py.objects.powl.obj.Transition(label='Enable Fractional')
validate_bidders = pm4py.objects.powl.obj.Transition(label='Validate Bidders')
resolve_disputes = pm4py.objects.powl.obj.Transition(label='Resolve Disputes')
distribute_royalties = pm4py.objects.powl.obj.Transition(label='Distribute Royalties')
promote_auction = pm4py.objects.powl.obj.Transition(label='Promote Auction')
process_payments = pm4py.objects.powl.obj.Transition(label='Process Payments')
confirm_ownership = pm4py.objects.powl.obj.Transition(label='Confirm Ownership')
arrange_shipping = pm4py.objects.powl.obj.Transition(label='Arrange Shipping')
track_delivery = pm4py.objects.powl.obj.Transition(label='Track Delivery')
report_analytics = pm4py.objects.powl.obj.Transition(label='Report Analytics')

# Define the POWL model
root = pm4py.objects.powl.obj.StrictPartialOrder(
    nodes=[
        verify_artwork, analyze_provenance, set_reserve, activate_auction,
        monitor_bids, adjust_pricing, enable_fractional, validate_bidders,
        resolve_disputes, distribute_royalties, promote_auction, process_payments,
        confirm_ownership, arrange_shipping, track_delivery, report_analytics
    ]
)

# Define the edges (dependencies)
root.order.add_edge(verify_artwork, analyze_provenance)
root.order.add_edge(analyze_provenance, set_reserve)
root.order.add_edge(set_reserve, activate_auction)
root.order.add_edge(activate_auction, monitor_bids)
root.order.add_edge(monitor_bids, adjust_pricing)
root.order.add_edge(adjust_pricing, enable_fractional)
root.order.add_edge(enable_fractional, validate_bidders)
root.order.add_edge(validate_bidders, resolve_disputes)
root.order.add_edge(resolve_disputes, distribute_royalties)
root.order.add_edge(distribute_royalties, promote_auction)
root.order.add_edge(promote_auction, process_payments)
root.order.add_edge(process_payments, confirm_ownership)
root.order.add_edge(confirm_ownership, arrange_shipping)
root.order.add_edge(arrange_shipping, track_delivery)
root.order.add_edge(track_delivery, report_analytics)

print(root)