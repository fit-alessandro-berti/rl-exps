import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
onboard = Transition(label='Artist Onboard')
verify = Transition(label='Asset Verify')
identity_check = Transition(label='Identity Check')
deploy = Transition(label='Smart Deploy')
bid_monitor = Transition(label='Bid Monitor')
price_adjust = Transition(label='Price Adjust')
wallet_link = Transition(label='Wallet Link')
submit_bid = Transition(label='Bid Submit')
close_auction = Transition(label='Auction Close')
transfer_ownership = Transition(label='Ownership Transfer')
release_funds = Transition(label='Fund Release')
review_dispute = Transition(label='Dispute Review')
update_reputation = Transition(label='Reputation Update')
fractional_offer = Transition(label='Fractional Offer')
secondary_sale = Transition(label='Secondary Sale')

# Define the POWL model
root = StrictPartialOrder(nodes=[onboard, verify, identity_check, deploy, bid_monitor, price_adjust, wallet_link, submit_bid, close_auction, transfer_ownership, release_funds, review_dispute, update_reputation, fractional_offer, secondary_sale])

# Define the order of the activities
root.order.add_edge(onboard, verify)
root.order.add_edge(verify, identity_check)
root.order.add_edge(identity_check, deploy)
root.order.add_edge(deploy, bid_monitor)
root.order.add_edge(bid_monitor, price_adjust)
root.order.add_edge(price_adjust, wallet_link)
root.order.add_edge(wallet_link, submit_bid)
root.order.add_edge(submit_bid, close_auction)
root.order.add_edge(close_auction, transfer_ownership)
root.order.add_edge(transfer_ownership, release_funds)
root.order.add_edge(release_funds, review_dispute)
root.order.add_edge(review_dispute, update_reputation)
root.order.add_edge(update_reputation, fractional_offer)
root.order.add_edge(fractional_offer, secondary_sale)

print(root)