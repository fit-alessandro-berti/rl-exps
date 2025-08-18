import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define operators
xor = OperatorPOWL(operator=Operator.XOR, children=[verify_artwork, analyze_provenance])
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[set_reserve, activate_auction, monitor_bids])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[adjust_pricing, enable_fractional, validate_bidders])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[resolve_disputes, distribute_royalties, promote_auction])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[process_payments, confirm_ownership, arrange_shipping])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[track_delivery, report_analytics])

# Define the root POWL model
root = StrictPartialOrder(nodes=[xor, loop1, loop2, loop3, loop4, loop5])
root.order.add_edge(xor, loop1)
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, loop5)

print(root)