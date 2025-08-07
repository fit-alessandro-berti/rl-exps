import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
artist_onboard    = Transition(label='Artist Onboard')
identity_check    = Transition(label='Identity Check')
asset_verify      = Transition(label='Asset Verify')
smart_deploy      = Transition(label='Smart Deploy')
wallet_link       = Transition(label='Wallet Link')
bid_submit        = Transition(label='Bid Submit')
price_adjust      = Transition(label='Price Adjust')
bid_monitor       = Transition(label='Bid Monitor')
auction_close     = Transition(label='Auction Close')
ownership_transfer= Transition(label='Ownership Transfer')
fund_release      = Transition(label='Fund Release')
dispute_review    = Transition(label='Dispute Review')
reputation_update = Transition(label='Reputation Update')
fractional_offer  = Transition(label='Fractional Offer')
secondary_sale    = Transition(label='Secondary Sale')

# Silent transition for loop exit
skip = SilentTransition()

# Loop for dynamic price adjustment and bid monitoring
loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[price_adjust, bid_monitor]
)

# Exclusive choice for fractional or secondary sale
xor = OperatorPOWL(
    operator=Operator.XOR,
    children=[fractional_offer, secondary_sale]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    artist_onboard,
    identity_check,
    asset_verify,
    smart_deploy,
    wallet_link,
    bid_submit,
    loop,
    auction_close,
    ownership_transfer,
    fund_release,
    dispute_review,
    reputation_update,
    xor
])

# Define the control-flow dependencies
root.order.add_edge(artist_onboard, identity_check)
root.order.add_edge(identity_check, asset_verify)
root.order.add_edge(asset_verify, smart_deploy)
root.order.add_edge(smart_deploy, wallet_link)
root.order.add_edge(wallet_link, bid_submit)

# Loop body: after each bid, either exit or adjust price and monitor bids again
root.order.add_edge(bid_submit, loop)

# After loop exit, finalize auction
root.order.add_edge(loop, auction_close)

# Finalize ownership and fund release after auction close
root.order.add_edge(auction_close, ownership_transfer)
root.order.add_edge(auction_close, fund_release)

# Optionally, handle dispute review and reputation update
root.order.add_edge(ownership_transfer, dispute_review)
root.order.add_edge(fund_release, dispute_review)
root.order.add_edge(dispute_review, reputation_update)

# For fractional or secondary sale, execute after both transfer and release
root.order.add_edge(ownership_transfer, xor)
root.order.add_edge(fund_release, xor)