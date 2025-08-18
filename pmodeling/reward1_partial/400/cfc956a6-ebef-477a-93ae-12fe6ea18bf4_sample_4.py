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

# Define silent transitions
skip = SilentTransition()

# Define loops and choices
smart_loop = OperatorPOWL(operator=Operator.LOOP, children=[smart_deploy, identity_check])
verify_loop = OperatorPOWL(operator=Operator.LOOP, children=[asset_verify, smart_loop])
bid_loop = OperatorPOWL(operator=Operator.LOOP, children=[bid_submit, bid_monitor])
price_loop = OperatorPOWL(operator=Operator.LOOP, children=[price_adjust, wallet_link])
dispute_loop = OperatorPOWL(operator=Operator.LOOP, children=[dispute_review, reputation_update])
fractional_loop = OperatorPOWL(operator=Operator.LOOP, children=[fractional_offer, secondary_sale])

# Define the root process
root = StrictPartialOrder(nodes=[artist_onboard, verify_loop, bid_loop, price_loop, smart_loop, dispute_loop, fractional_loop])
root.order.add_edge(artist_onboard, verify_loop)
root.order.add_edge(verify_loop, bid_loop)
root.order.add_edge(bid_loop, price_loop)
root.order.add_edge(price_loop, smart_loop)
root.order.add_edge(smart_loop, dispute_loop)
root.order.add_edge(dispute_loop, fractional_loop)

print(root)