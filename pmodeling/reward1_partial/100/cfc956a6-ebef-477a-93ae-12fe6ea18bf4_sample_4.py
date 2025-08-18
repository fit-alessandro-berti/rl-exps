from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
artist_onboard = Transition(label='Artist Onboard')
verify_asset = Transition(label='Asset Verify')
identity_check = Transition(label='Identity Check')
smart_deploy = Transition(label='Smart Deploy')
bid_monitor = Transition(label='Bid Monitor')
price_adjust = Transition(label='Price Adjust')
wallet_link = Transition(label='Wallet Link')
submit_bid = Transition(label='Bid Submit')
auction_close = Transition(label='Auction Close')
ownership_transfer = Transition(label='Ownership Transfer')
fund_release = Transition(label='Fund Release')
dispute_review = Transition(label='Dispute Review')
reputation_update = Transition(label='Reputation Update')
fractional_offer = Transition(label='Fractional Offer')
secondary_sale = Transition(label='Secondary Sale')

# Define silent transitions
skip = SilentTransition()

# Define exclusive choice nodes
verify_asset_and_identity = OperatorPOWL(operator=Operator.XOR, children=[verify_asset, identity_check])
deploy_and_monitor = OperatorPOWL(operator=Operator.XOR, children=[smart_deploy, bid_monitor])
adjust_price_and_link = OperatorPOWL(operator=Operator.XOR, children=[price_adjust, wallet_link])
submit_bid_and_close = OperatorPOWL(operator=Operator.XOR, children=[submit_bid, auction_close])
transfer_and_release = OperatorPOWL(operator=Operator.XOR, children=[ownership_transfer, fund_release])
review_and_update = OperatorPOWL(operator=Operator.XOR, children=[dispute_review, reputation_update])
offer_and_sale = OperatorPOWL(operator=Operator.XOR, children=[fractional_offer, secondary_sale])

# Define loop nodes
verify_and_monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[verify_asset_and_identity, deploy_and_monitor])
adjust_and_link_loop = OperatorPOWL(operator=Operator.LOOP, children=[adjust_price_and_link, submit_bid_and_close])
transfer_and_release_loop = OperatorPOWL(operator=Operator.LOOP, children=[transfer_and_release, review_and_update])
offer_and_sale_loop = OperatorPOWL(operator=Operator.LOOP, children=[offer_and_sale, review_and_update])

# Define the root model
root = StrictPartialOrder(nodes=[
    verify_and_monitor_loop,
    adjust_and_link_loop,
    transfer_and_release_loop,
    offer_and_sale_loop
])

# Add edges between nodes
root.order.add_edge(verify_and_monitor_loop, adjust_and_link_loop)
root.order.add_edge(adjust_and_link_loop, transfer_and_release_loop)
root.order.add_edge(transfer_and_release_loop, offer_and_sale_loop)

print(root)