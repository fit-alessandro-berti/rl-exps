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

# Define the loops
bid_loop = OperatorPOWL(operator=Operator.LOOP, children=[bid_submit, bid_monitor])
auction_loop = OperatorPOWL(operator=Operator.LOOP, children=[auction_close, smart_deploy])

# Define the exclusive choices
verify_loop = OperatorPOWL(operator=Operator.XOR, children=[identity_check, asset_verify])
deploy_loop = OperatorPOWL(operator=Operator.XOR, children=[smart_deploy, skip])

# Define the POWL model
root = StrictPartialOrder(nodes=[artist_onboard, verify_loop, deploy_loop, bid_loop, auction_loop, reputation_update, fractional_offer, secondary_sale])
root.order.add_edge(artist_onboard, verify_loop)
root.order.add_edge(artist_onboard, deploy_loop)
root.order.add_edge(verify_loop, deploy_loop)
root.order.add_edge(deploy_loop, bid_loop)
root.order.add_edge(bid_loop, auction_loop)
root.order.add_edge(auction_loop, reputation_update)
root.order.add_edge(reputation_update, fractional_offer)
root.order.add_edge(fractional_offer, secondary_sale)

# Print the POWL model
print(root)