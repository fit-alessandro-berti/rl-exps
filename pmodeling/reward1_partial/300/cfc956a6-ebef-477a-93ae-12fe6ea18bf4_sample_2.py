import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

artist_onboard_loop = OperatorPOWL(operator=Operator.LOOP, children=[artist_onboard, identity_check])
asset_verify_loop = OperatorPOWL(operator=Operator.LOOP, children=[asset_verify, smart_deploy])
bid_monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[bid_monitor, price_adjust])
wallet_link_loop = OperatorPOWL(operator=Operator.LOOP, children=[wallet_link, bid_submit])
auction_close_loop = OperatorPOWL(operator=Operator.LOOP, children=[auction_close, ownership_transfer, fund_release, dispute_review])
reputation_update_loop = OperatorPOWL(operator=Operator.LOOP, children=[reputation_update, fractional_offer, secondary_sale])

root = StrictPartialOrder(nodes=[artist_onboard_loop, asset_verify_loop, bid_monitor_loop, wallet_link_loop, auction_close_loop, reputation_update_loop])
root.order.add_edge(artist_onboard_loop, asset_verify_loop)
root.order.add_edge(asset_verify_loop, bid_monitor_loop)
root.order.add_edge(bid_monitor_loop, wallet_link_loop)
root.order.add_edge(wallet_link_loop, auction_close_loop)
root.order.add_edge(auction_close_loop, reputation_update_loop)