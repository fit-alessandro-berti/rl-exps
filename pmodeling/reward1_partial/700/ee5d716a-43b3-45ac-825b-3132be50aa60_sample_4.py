import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define control flow operators
exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[
    analyze_provenance,
    SilentTransition()
])
dynamic_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    adjust_pricing,
    enable_fractional,
    validate_bidders,
    resolve_disputes,
    distribute_royalties
])
monitor_and_adjust = OperatorPOWL(operator=Operator.LOOP, children=[
    monitor_bids,
    dynamic_loop
])
artwork_activation = OperatorPOWL(operator=Operator.LOOP, children=[
    activate_auction,
    monitor_and_adjust
])
payment_and_tracking = OperatorPOWL(operator=Operator.LOOP, children=[
    process_payments,
    arrange_shipping,
    track_delivery
])
promotion_and_analytics = OperatorPOWL(operator=Operator.LOOP, children=[
    promote_auction,
    report_analytics
])
final_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    artwork_activation,
    payment_and_tracking,
    promotion_and_analytics
])

# Define root POWL model
root = StrictPartialOrder(nodes=[verify_artwork, final_loop])
root.order.add_edge(verify_artwork, final_loop)