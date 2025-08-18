import pm4py
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

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[verify_artwork, analyze_provenance, set_reserve])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[activate_auction, monitor_bids, adjust_pricing])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[enable_fractional, validate_bidders])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[resolve_disputes, distribute_royalties])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[promote_auction, process_payments, confirm_ownership])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[arrange_shipping, track_delivery, report_analytics])

xor1 = OperatorPOWL(operator=Operator.XOR, children=[loop1, loop2])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[loop3, loop4])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[loop5, loop6])

root = StrictPartialOrder(nodes=[xor1, xor2, xor3])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor1, xor3)
root.order.add_edge(xor2, xor3)