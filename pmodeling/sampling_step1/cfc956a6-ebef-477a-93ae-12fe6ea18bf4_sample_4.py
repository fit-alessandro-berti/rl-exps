from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
artist_onboard = Transition(label='Artist Onboard')
verify_asset = Transition(label='Asset Verify')
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

# Define silent transition (tau)
skip = SilentTransition()

# Define partial order
root = StrictPartialOrder(nodes=[
    artist_onboard, verify_asset, identity_check, smart_deploy,
    bid_monitor, price_adjust, wallet_link, bid_submit, auction_close,
    ownership_transfer, fund_release, dispute_review, reputation_update,
    fractional_offer, secondary_sale
])

# Define dependencies
root.order.add_edge(artist_onboard, verify_asset)
root.order.add_edge(verify_asset, identity_check)
root.order.add_edge(identity_check, smart_deploy)
root.order.add_edge(smart_deploy, bid_monitor)
root.order.add_edge(bid_monitor, price_adjust)
root.order.add_edge(price_adjust, wallet_link)
root.order.add_edge(wallet_link, bid_submit)
root.order.add_edge(bid_submit, auction_close)
root.order.add_edge(auction_close, ownership_transfer)
root.order.add_edge(ownership_transfer, fund_release)
root.order.add_edge(fund_release, dispute_review)
root.order.add_edge(dispute_review, reputation_update)
root.order.add_edge(reputation_update, fractional_offer)
root.order.add_edge(fractional_offer, secondary_sale)

print(root)