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
skip = SilentTransition()

# Define the POWL model
loop_verify_analyze = OperatorPOWL(operator=Operator.LOOP, children=[verify_artwork, analyze_provenance])
loop_set_reserve = OperatorPOWL(operator=Operator.LOOP, children=[set_reserve, activate_auction])
loop_monitor_bids = OperatorPOWL(operator=Operator.LOOP, children=[monitor_bids, adjust_pricing])
loop_enable_fractional = OperatorPOWL(operator=Operator.LOOP, children=[enable_fractional, validate_bidders])
loop_resolve_disputes = OperatorPOWL(operator=Operator.LOOP, children=[resolve_disputes, distribute_royalties])
loop_promote_auction = OperatorPOWL(operator=Operator.LOOP, children=[promote_auction, process_payments])
loop_confirm_ownership = OperatorPOWL(operator=Operator.LOOP, children=[confirm_ownership, arrange_shipping])
loop_track_delivery = OperatorPOWL(operator=Operator.LOOP, children=[track_delivery, report_analytics])
xor_verify_analyze = OperatorPOWL(operator=Operator.XOR, children=[loop_verify_analyze, loop_set_reserve])
xor_monitor_bids = OperatorPOWL(operator=Operator.XOR, children=[loop_monitor_bids, loop_enable_fractional])
xor_resolve_disputes = OperatorPOWL(operator=Operator.XOR, children=[loop_resolve_disputes, loop_promote_auction])
xor_confirm_ownership = OperatorPOWL(operator=Operator.XOR, children=[loop_confirm_ownership, loop_track_delivery])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[xor_verify_analyze, xor_monitor_bids, xor_resolve_disputes, xor_confirm_ownership])
root.order.add_edge(xor_verify_analyze, xor_monitor_bids)
root.order.add_edge(xor_monitor_bids, xor_resolve_disputes)
root.order.add_edge(xor_resolve_disputes, xor_confirm_ownership)

print(root)