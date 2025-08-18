from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

# Workflow structure
root = StrictPartialOrder(nodes=[
    verify_artwork, analyze_provenance, set_reserve, activate_auction, monitor_bids,
    adjust_pricing, enable_fractional, validate_bidders, resolve_disputes, distribute_royalties,
    promote_auction, process_payments, confirm_ownership, arrange_shipping, track_delivery,
    report_analytics
])

# Define dependencies
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

# Define dependencies for each activity
# Example: Adjust Pricing depends on Monitor Bids and Enable Fractional
root.order.add_edge(monitor_bids, adjust_pricing)
root.order.add_edge(enable_fractional, adjust_pricing)

# Example: Resolve Disputes depends on Validate Bidders and Distribute Royalties
root.order.add_edge(validate_bidders, resolve_disputes)
root.order.add_edge(distribute_royalties, resolve_disputes)

# Example: Process Payments depends on Confirm Ownership and Arrange Shipping
root.order.add_edge(confirm_ownership, process_payments)
root.order.add_edge(arrange_shipping, process_payments)

# Example: Arrange Shipping depends on Track Delivery and Report Analytics
root.order.add_edge(track_delivery, arrange_shipping)
root.order.add_edge(report_analytics, arrange_shipping)

# Example: Track Delivery depends on Confirm Ownership and Process Payments
root.order.add_edge(confirm_ownership, track_delivery)
root.order.add_edge(process_payments, track_delivery)

# Example: Confirm Ownership depends on Verify Artwork, Analyze Provenance, Set Reserve, Activate Auction, Monitor Bids, Adjust Pricing, Enable Fractional, Validate Bidders, Resolve Disputes, Distribute Royalties, Promote Auction, and Process Payments
root.order.add_edge(verify_artwork, confirm_ownership)
root.order.add_edge(analyze_provenance, confirm_ownership)
root.order.add_edge(set_reserve, confirm_ownership)
root.order.add_edge(activate_auction, confirm_ownership)
root.order.add_edge(monitor_bids, confirm_ownership)
root.order.add_edge(adjust_pricing, confirm_ownership)
root.order.add_edge(enable_fractional, confirm_ownership)
root.order.add_edge(validate_bidders, confirm_ownership)
root.order.add_edge(resolve_disputes, confirm_ownership)
root.order.add_edge(distribute_royalties, confirm_ownership)
root.order.add_edge(promote_auction, confirm_ownership)
root.order.add_edge(process_payments, confirm_ownership)

# Example: Promote Auction depends on Verify Artwork, Analyze Provenance, Set Reserve, Activate Auction, Monitor Bids, Adjust Pricing, Enable Fractional, Validate Bidders, Resolve Disputes, Distribute Royalties, and Process Payments
root.order.add_edge(verify_artwork, promote_auction)
root.order.add_edge(analyze_provenance, promote_auction)
root.order.add_edge(set_reserve, promote_auction)
root.order.add_edge(activate_auction, promote_auction)
root.order.add_edge(monitor_bids, promote_auction)
root.order.add_edge(adjust_pricing, promote_auction)
root.order.add_edge(enable_fractional, promote_auction)
root.order.add_edge(validate_bidders, promote_auction)
root.order.add_edge(resolve_disputes, promote_auction)
root.order.add_edge(distribute_royalties, promote_auction)
root.order.add_edge(process_payments, promote_auction)

# Example: Process Payments depends on Confirm Ownership, Arrange Shipping, and Track Delivery
root.order.add_edge(confirm_ownership, process_payments)
root.order.add_edge(arrange_shipping, process_payments)
root.order.add_edge(track_delivery, process_payments)