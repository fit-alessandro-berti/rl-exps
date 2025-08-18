import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
artist_onboard = Transition(label='Artist Onboard')
verify_asset = Transition(label='Asset Verify')
identity_check = Transition(label='Identity Check')
deploy_smart_contract = Transition(label='Smart Deploy')
monitor_bids = Transition(label='Bid Monitor')
adjust_price = Transition(label='Price Adjust')
link_wallet = Transition(label='Wallet Link')
submit_bid = Transition(label='Bid Submit')
close_auction = Transition(label='Auction Close')
transfer_ownership = Transition(label='Ownership Transfer')
release_funds = Transition(label='Fund Release')
review_dispute = Transition(label='Dispute Review')
update_reputation = Transition(label='Reputation Update')
offer_fractional = Transition(label='Fractional Offer')
secondary_sale = Transition(label='Secondary Sale')

# Define partial order
root = StrictPartialOrder(nodes=[
    artist_onboard, verify_asset, identity_check, deploy_smart_contract,
    monitor_bids, adjust_price, link_wallet, submit_bid, close_auction,
    transfer_ownership, release_funds, review_dispute, update_reputation,
    offer_fractional, secondary_sale
])

# Define dependencies
root.order.add_edge(artist_onboard, verify_asset)
root.order.add_edge(verify_asset, identity_check)
root.order.add_edge(identity_check, deploy_smart_contract)
root.order.add_edge(deploy_smart_contract, monitor_bids)
root.order.add_edge(monitor_bids, adjust_price)
root.order.add_edge(adjust_price, link_wallet)
root.order.add_edge(link_wallet, submit_bid)
root.order.add_edge(submit_bid, close_auction)
root.order.add_edge(close_auction, transfer_ownership)
root.order.add_edge(transfer_ownership, release_funds)
root.order.add_edge(release_funds, review_dispute)
root.order.add_edge(review_dispute, update_reputation)
root.order.add_edge(update_reputation, offer_fractional)
root.order.add_edge(offer_fractional, secondary_sale)