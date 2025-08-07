import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the silent transitions
skip = SilentTransition()

# Define the partial order
loop = OperatorPOWL(operator=Operator.LOOP, children=[bid_monitor, price_adjust, wallet_link])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[auction_close, dispute_review])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[ownership_transfer, reputation_update])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[fund_release, secondary_sale])
root = StrictPartialOrder(nodes=[artist_onboard, asset_verify, identity_check, smart_deploy, loop, xor1, xor2, xor3])
root.order.add_edge(artist_onboard, asset_verify)
root.order.add_edge(asset_verify, identity_check)
root.order.add_edge(identity_check, smart_deploy)
root.order.add_edge(smart_deploy, loop)
root.order.add_edge(loop, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, auction_close)
root.order.add_edge(xor1, dispute_review)
root.order.add_edge(xor2, reputation_update)
root.order.add_edge(xor3, fund_release)
root.order.add_edge(xor3, secondary_sale)

# Print the root POWL model
print(root)