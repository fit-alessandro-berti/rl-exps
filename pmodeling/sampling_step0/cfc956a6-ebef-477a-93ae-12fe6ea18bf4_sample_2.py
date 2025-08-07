import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
artist_onboard = Transition(label='Artist Onboard')
asset_verify = Transition(label='Asset Verify')
identity_check = Transition(label='Identity Check')
smart_deploy = Transition(label='Smart Deploy')
bid_monitor = Transition(label='Bid Monitor')
price_adjust = Transition(label='Price Adjust')
wallet_link = Transition(label='Wallet Link')
bid_submit = Transition(label='Bid Submit')
auction_close = Transition(label='Auction Close')
ownership_transfer = Transition(label='Ownership Transfer')
fund_release = Transition(label='Fund Release')
dispute_review = Transition(label='Dispute Review')
reputation_update = Transition(label='Reputation Update')
fractional_offer = Transition(label='Fractional Offer')
secondary_sale = Transition(label='Secondary Sale')

# Define silent transitions
skip = SilentTransition()

# Define loop nodes for dynamic pricing and reputation update
loop_pricing = OperatorPOWL(operator=Operator.LOOP, children=[price_adjust, reputation_update])
loop_reputation = OperatorPOWL(operator=Operator.LOOP, children=[dispute_review, reputation_update])

# Define XOR nodes for fractional offer and secondary sale
xor_fractional = OperatorPOWL(operator=Operator.XOR, children=[fractional_offer, skip])
xor_secondary = OperatorPOWL(operator=Operator.XOR, children=[secondary_sale, skip])

# Define the root partial order
root = StrictPartialOrder(nodes=[artist_onboard, asset_verify, identity_check, smart_deploy, bid_monitor, loop_pricing, loop_reputation, xor_fractional, xor_secondary])
root.order.add_edge(artist_onboard, asset_verify)
root.order.add_edge(asset_verify, identity_check)
root.order.add_edge(identity_check, smart_deploy)
root.order.add_edge(smart_deploy, bid_monitor)
root.order.add_edge(bid_monitor, loop_pricing)
root.order.add_edge(loop_pricing, loop_reputation)
root.order.add_edge(loop_reputation, xor_fractional)
root.order.add_edge(xor_fractional, xor_secondary)
root.order.add_edge(xor_secondary, auction_close)
root.order.add_edge(auction_close, ownership_transfer)
root.order.add_edge(ownership_transfer, fund_release)
root.order.add_edge(fund_release, loop_pricing)
root.order.add_edge(loop_pricing, loop_reputation)
root.order.add_edge(loop_reputation, xor_fractional)
root.order.add_edge(xor_fractional, xor_secondary)
root.order.add_edge(xor_secondary, auction_close)
root.order.add_edge(auction_close, ownership_transfer)
root.order.add_edge(ownership_transfer, fund_release)

print(root)