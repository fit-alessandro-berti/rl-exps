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

# Define silent transitions (empty labels)
skip = SilentTransition()

# Define loop for auction closing and fund release
auction_loop = OperatorPOWL(operator=Operator.LOOP, children=[auction_close, fund_release])

# Define exclusive choice for dispute review and reputation update
dispute_choice = OperatorPOWL(operator=Operator.XOR, children=[dispute_review, reputation_update])

# Define partial order for the entire process
root = StrictPartialOrder(nodes=[
    artist_onboard,
    asset_verify,
    identity_check,
    smart_deploy,
    bid_monitor,
    price_adjust,
    wallet_link,
    bid_submit,
    auction_loop,
    dispute_choice,
    fractional_offer,
    secondary_sale
])

# Add dependencies between nodes
root.order.add_edge(artist_onboard, asset_verify)
root.order.add_edge(asset_verify, identity_check)
root.order.add_edge(identity_check, smart_deploy)
root.order.add_edge(smart_deploy, bid_monitor)
root.order.add_edge(bid_monitor, price_adjust)
root.order.add_edge(price_adjust, wallet_link)
root.order.add_edge(wallet_link, bid_submit)
root.order.add_edge(bid_submit, auction_loop)
root.order.add_edge(auction_loop, dispute_choice)
root.order.add_edge(dispute_choice, fractional_offer)
root.order.add_edge(fractional_offer, secondary_sale)

# Print the root model
print(root)