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

# Define the workflow
artist_onboard_to_asset_verify = OperatorPOWL(operator=Operator.LOOP, children=[artist_onboard, asset_verify])
asset_verify_to_identity_check = OperatorPOWL(operator=Operator.LOOP, children=[asset_verify, identity_check])
identity_check_to_smart_deploy = OperatorPOWL(operator=Operator.LOOP, children=[identity_check, smart_deploy])
smart_deploy_to_bid_monitor = OperatorPOWL(operator=Operator.LOOP, children=[smart_deploy, bid_monitor])
bid_monitor_to_price_adjust = OperatorPOWL(operator=Operator.LOOP, children=[bid_monitor, price_adjust])
price_adjust_to_wallet_link = OperatorPOWL(operator=Operator.LOOP, children=[price_adjust, wallet_link])
wallet_link_to_bid_submit = OperatorPOWL(operator=Operator.LOOP, children=[wallet_link, bid_submit])
bid_submit_to_auction_close = OperatorPOWL(operator=Operator.LOOP, children=[bid_submit, auction_close])
auction_close_to_ownership_transfer = OperatorPOWL(operator=Operator.LOOP, children=[auction_close, ownership_transfer])
ownership_transfer_to_fund_release = OperatorPOWL(operator=Operator.LOOP, children=[ownership_transfer, fund_release])
fund_release_to_dispute_review = OperatorPOWL(operator=Operator.LOOP, children=[fund_release, dispute_review])
dispute_review_to_reputation_update = OperatorPOWL(operator=Operator.LOOP, children=[dispute_review, reputation_update])
reputation_update_to_fractional_offer = OperatorPOWL(operator=Operator.LOOP, children=[reputation_update, fractional_offer])
fractional_offer_to_secondary_sale = OperatorPOWL(operator=Operator.LOOP, children=[fractional_offer, secondary_sale])

# Connect the nodes in the workflow
root = StrictPartialOrder(nodes=[
    artist_onboard_to_asset_verify,
    asset_verify_to_identity_check,
    identity_check_to_smart_deploy,
    smart_deploy_to_bid_monitor,
    bid_monitor_to_price_adjust,
    price_adjust_to_wallet_link,
    wallet_link_to_bid_submit,
    bid_submit_to_auction_close,
    auction_close_to_ownership_transfer,
    ownership_transfer_to_fund_release,
    fund_release_to_dispute_review,
    dispute_review_to_reputation_update,
    reputation_update_to_fractional_offer,
    fractional_offer_to_secondary_sale
])

# Add dependencies between nodes
root.order.add_edge(artist_onboard_to_asset_verify, asset_verify_to_identity_check)
root.order.add_edge(asset_verify_to_identity_check, identity_check_to_smart_deploy)
root.order.add_edge(identity_check_to_smart_deploy, smart_deploy_to_bid_monitor)
root.order.add_edge(smart_deploy_to_bid_monitor, bid_monitor_to_price_adjust)
root.order.add_edge(bid_monitor_to_price_adjust, price_adjust_to_wallet_link)
root.order.add_edge(price_adjust_to_wallet_link, wallet_link_to_bid_submit)
root.order.add_edge(wallet_link_to_bid_submit, bid_submit_to_auction_close)
root.order.add_edge(bid_submit_to_auction_close, auction_close_to_ownership_transfer)
root.order.add_edge(auction_close_to_ownership_transfer, ownership_transfer_to_fund_release)
root.order.add_edge(ownership_transfer_to_fund_release, fund_release_to_dispute_review)
root.order.add_edge(fund_release_to_dispute_review, dispute_review_to_reputation_update)
root.order.add_edge(dispute_review_to_reputation_update, reputation_update_to_fractional_offer)
root.order.add_edge(reputation_update_to_fractional_offer, fractional_offer_to_secondary_sale)

print(root)