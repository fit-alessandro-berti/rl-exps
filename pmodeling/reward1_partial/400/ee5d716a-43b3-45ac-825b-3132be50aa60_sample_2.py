import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the process structure
verify_artwork_order = OperatorPOWL(operator=Operator.LOOP, children=[verify_artwork, analyze_provenance, set_reserve])
activate_auction_order = OperatorPOWL(operator=Operator.LOOP, children=[activate_auction, monitor_bids, adjust_pricing, enable_fractional, validate_bidders])
resolve_disputes_order = OperatorPOWL(operator=Operator.LOOP, children=[resolve_disputes])
distribute_royalties_order = OperatorPOWL(operator=Operator.LOOP, children=[distribute_royalties])
promote_auction_order = OperatorPOWL(operator=Operator.LOOP, children=[promote_auction])
process_payments_order = OperatorPOWL(operator=Operator.LOOP, children=[process_payments])
confirm_ownership_order = OperatorPOWL(operator=Operator.LOOP, children=[confirm_ownership])
arrange_shipping_order = OperatorPOWL(operator=Operator.LOOP, children=[arrange_shipping])
track_delivery_order = OperatorPOWL(operator=Operator.LOOP, children=[track_delivery])
report_analytics_order = OperatorPOWL(operator=Operator.LOOP, children=[report_analytics])

# Create the root node
root = StrictPartialOrder(nodes=[
    verify_artwork_order,
    activate_auction_order,
    resolve_disputes_order,
    distribute_royalties_order,
    promote_auction_order,
    process_payments_order,
    confirm_ownership_order,
    arrange_shipping_order,
    track_delivery_order,
    report_analytics_order
])

# Add dependencies
root.order.add_edge(verify_artwork_order, analyze_provenance)
root.order.add_edge(verify_artwork_order, set_reserve)
root.order.add_edge(activate_auction_order, monitor_bids)
root.order.add_edge(activate_auction_order, adjust_pricing)
root.order.add_edge(activate_auction_order, enable_fractional)
root.order.add_edge(activate_auction_order, validate_bidders)
root.order.add_edge(resolve_disputes_order, resolve_disputes)
root.order.add_edge(distribute_royalties_order, distribute_royalties)
root.order.add_edge(promote_auction_order, promote_auction)
root.order.add_edge(process_payments_order, process_payments)
root.order.add_edge(confirm_ownership_order, confirm_ownership)
root.order.add_edge(arrange_shipping_order, arrange_shipping)
root.order.add_edge(track_delivery_order, track_delivery)
root.order.add_edge(report_analytics_order, report_analytics)