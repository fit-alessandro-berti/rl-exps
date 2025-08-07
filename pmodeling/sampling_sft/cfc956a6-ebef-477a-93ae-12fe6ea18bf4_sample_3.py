import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities as POWL transitions
artist_onboard     = Transition(label='Artist Onboard')
asset_verify       = Transition(label='Asset Verify')
identity_check     = Transition(label='Identity Check')
smart_deploy       = Transition(label='Smart Deploy')
bid_monitor        = Transition(label='Bid Monitor')
price_adjust       = Transition(label='Price Adjust')
wallet_link        = Transition(label='Wallet Link')
bid_submit         = Transition(label='Bid Submit')
auction_close      = Transition(label='Auction Close')
ownership_transfer = Transition(label='Ownership Transfer')
fund_release       = Transition(label='Fund Release')
dispute_review     = Transition(label='Dispute Review')
reputation_update  = Transition(label='Reputation Update')
fractional_offer   = Transition(label='Fractional Offer')
secondary_sale     = Transition(label='Secondary Sale')

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    artist_onboard, asset_verify, identity_check, smart_deploy,
    bid_monitor, price_adjust, wallet_link, bid_submit,
    auction_close, ownership_transfer, fund_release,
    dispute_review, reputation_update, fractional_offer, secondary_sale
])

# Define the control‐flow dependencies
root.order.add_edge(artist_onboard, asset_verify)
root.order.add_edge(asset_verify, identity_check)
root.order.add_edge(identity_check, smart_deploy)

# After deployment, monitor bids and adjust prices in parallel
root.order.add_edge(smart_deploy, bid_monitor)
root.order.add_edge(smart_deploy, price_adjust)

# Both monitor and price adjustments can happen concurrently
root.order.add_edge(bid_monitor, auction_close)
root.order.add_edge(price_adjust, auction_close)

# Auction closure triggers transfer and fund release
root.order.add_edge(auction_close, ownership_transfer)
root.order.add_edge(auction_close, fund_release)

# Parallel dispute review and reputation update
root.order.add_edge(auction_close, dispute_review)
root.order.add_edge(auction_close, reputation_update)

# After dispute review, fractional and secondary sales can occur
root.order.add_edge(dispute_review, fractional_offer)
root.order.add_edge(dispute_review, secondary_sale)
root.order.add_edge(reputation_update, fractional_offer)
root.order.add_edge(reputation_update, secondary_sale)