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

# Define the silent transitions
skip = SilentTransition()

# Define the exclusive choice for artwork verification and provenance analysis
xor_verify_prove = OperatorPOWL(operator=Operator.XOR, children=[verify_artwork, analyze_provenance])

# Define the loop for setting reserve price and activating auction
loop_set_reserve = OperatorPOWL(operator=Operator.LOOP, children=[set_reserve, activate_auction])

# Define the exclusive choice for monitoring bids and adjusting pricing
xor_monitor_adjust = OperatorPOWL(operator=Operator.XOR, children=[monitor_bids, adjust_pricing])

# Define the exclusive choice for enabling fractional ownership bids and validating bidders
xor_fractional_validate = OperatorPOWL(operator=Operator.XOR, children=[enable_fractional, validate_bidders])

# Define the exclusive choice for resolving disputes and distributing royalties
xor_resolve_distribute = OperatorPOWL(operator=Operator.XOR, children=[resolve_disputes, distribute_royalties])

# Define the loop for promoting auction and processing payments
loop_promote_process = OperatorPOWL(operator=Operator.LOOP, children=[promote_auction, process_payments])

# Define the exclusive choice for confirming ownership and arranging shipping
xor_confirm_arrange = OperatorPOWL(operator=Operator.XOR, children=[confirm_ownership, arrange_shipping])

# Define the loop for tracking delivery and reporting analytics
loop_track_report = OperatorPOWL(operator=Operator.LOOP, children=[track_delivery, report_analytics])

# Define the root POWL model
root = StrictPartialOrder(nodes=[xor_verify_prove, loop_set_reserve, xor_monitor_adjust, xor_fractional_validate, xor_resolve_distribute, loop_promote_process, xor_confirm_arrange, loop_track_report])

# Define the edges in the partial order
root.order.add_edge(xor_verify_prove, loop_set_reserve)
root.order.add_edge(loop_set_reserve, xor_monitor_adjust)
root.order.add_edge(xor_monitor_adjust, xor_fractional_validate)
root.order.add_edge(xor_fractional_validate, xor_resolve_distribute)
root.order.add_edge(xor_resolve_distribute, loop_promote_process)
root.order.add_edge(loop_promote_process, xor_confirm_arrange)
root.order.add_edge(xor_confirm_arrange, loop_track_report)
root.order.add_edge(loop_track_report, loop_track_report)

print(root)