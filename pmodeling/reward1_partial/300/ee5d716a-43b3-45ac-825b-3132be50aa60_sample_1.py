from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions for no-operation
skip = SilentTransition()

# Define loops and choices for the process
verify_analyze_loop = OperatorPOWL(operator=Operator.LOOP, children=[verify_artwork, analyze_provenance])
set_reserve_loop = OperatorPOWL(operator=Operator.LOOP, children=[set_reserve, activate_auction])
monitor_bid_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor_bids, adjust_pricing])
fractional_loop = OperatorPOWL(operator=Operator.LOOP, children=[enable_fractional, validate_bidders])
dispute_loop = OperatorPOWL(operator=Operator.LOOP, children=[resolve_disputes, distribute_royalties])
promotion_loop = OperatorPOWL(operator=Operator.LOOP, children=[promote_auction, process_payments])
ownership_loop = OperatorPOWL(operator=Operator.LOOP, children=[confirm_ownership, arrange_shipping])
delivery_loop = OperatorPOWL(operator=Operator.LOOP, children=[track_delivery, report_analytics])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[verify_analyze_loop, set_reserve_loop, monitor_bid_loop, fractional_loop, dispute_loop, promotion_loop, ownership_loop, delivery_loop])
root.order.add_edge(verify_analyze_loop, set_reserve_loop)
root.order.add_edge(set_reserve_loop, activate_auction)
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