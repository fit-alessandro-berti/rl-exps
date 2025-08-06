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

# Define silent transitions
skip = SilentTransition()

# Define loop and choice nodes
verify_loop = OperatorPOWL(operator=Operator.LOOP, children=[verify_artwork, analyze_provenance])
analyze_loop = OperatorPOWL(operator=Operator.LOOP, children=[set_reserve, activate_auction])
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor_bids, adjust_pricing])
fractional_loop = OperatorPOWL(operator=Operator.LOOP, children=[enable_fractional, validate_bidders])
dispute_loop = OperatorPOWL(operator=Operator.LOOP, children=[resolve_disputes, distribute_royalties])
promotion_loop = OperatorPOWL(operator=Operator.LOOP, children=[promote_auction, process_payments])
ownership_loop = OperatorPOWL(operator=Operator.LOOP, children=[confirm_ownership, arrange_shipping])
delivery_loop = OperatorPOWL(operator=Operator.LOOP, children=[track_delivery, report_analytics])

# Define exclusive choices
exclusive_verify = OperatorPOWL(operator=Operator.XOR, children=[verify_loop, skip])
exclusive_analyze = OperatorPOWL(operator=Operator.XOR, children=[analyze_loop, skip])
exclusive_monitor = OperatorPOWL(operator=Operator.XOR, children=[monitor_loop, skip])
exclusive_fractional = OperatorPOWL(operator=Operator.XOR, children=[fractional_loop, skip])
exclusive_dispute = OperatorPOWL(operator=Operator.XOR, children=[dispute_loop, skip])
exclusive_promotion = OperatorPOWL(operator=Operator.XOR, children=[promotion_loop, skip])
exclusive_ownership = OperatorPOWL(operator=Operator.XOR, children=[ownership_loop, skip])
exclusive_delivery = OperatorPOWL(operator=Operator.XOR, children=[delivery_loop, skip])

# Define root node
root = StrictPartialOrder(nodes=[exclusive_verify, exclusive_analyze, exclusive_monitor, exclusive_fractional, exclusive_dispute, exclusive_promotion, exclusive_ownership, exclusive_delivery])
root.order.add_edge(exclusive_verify, exclusive_analyze)
root.order.add_edge(exclusive_analyze, exclusive_monitor)
root.order.add_edge(exclusive_monitor, exclusive_fractional)
root.order.add_edge(exclusive_fractional, exclusive_dispute)
root.order.add_edge(exclusive_dispute, exclusive_promotion)
root.order.add_edge(exclusive_promotion, exclusive_ownership)
root.order.add_edge(exclusive_ownership, exclusive_delivery)