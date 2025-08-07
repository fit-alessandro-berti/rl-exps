import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define exclusive choices
exclusive_choice_1 = OperatorPOWL(operator=Operator.XOR, children=[smart_deploy, skip])
exclusive_choice_2 = OperatorPOWL(operator=Operator.XOR, children=[auction_close, skip])
exclusive_choice_3 = OperatorPOWL(operator=Operator.XOR, children=[dispute_review, skip])
exclusive_choice_4 = OperatorPOWL(operator=Operator.XOR, children=[reputation_update, skip])
exclusive_choice_5 = OperatorPOWL(operator=Operator.XOR, children=[fractional_offer, skip])
exclusive_choice_6 = OperatorPOWL(operator=Operator.XOR, children=[secondary_sale, skip])

# Define loops
loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[bid_monitor, price_adjust])
loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[bid_submit, exclusive_choice_2])

# Define root partial order
root = StrictPartialOrder(nodes=[artist_onboard, asset_verify, identity_check, exclusive_choice_1, exclusive_choice_2, exclusive_choice_3, exclusive_choice_4, exclusive_choice_5, exclusive_choice_6, loop_1, loop_2])
root.order.add_edge(artist_onboard, asset_verify)
root.order.add_edge(asset_verify, identity_check)
root.order.add_edge(identity_check, exclusive_choice_1)
root.order.add_edge(exclusive_choice_1, smart_deploy)
root.order.add_edge(smart_deploy, exclusive_choice_2)
root.order.add_edge(exclusive_choice_2, auction_close)
root.order.add_edge(auction_close, exclusive_choice_3)
root.order.add_edge(exclusive_choice_3, dispute_review)
root.order.add_edge(dispute_review, exclusive_choice_4)
root.order.add_edge(exclusive_choice_4, reputation_update)
root.order.add_edge(reputation_update, exclusive_choice_5)
root.order.add_edge(exclusive_choice_5, fractional_offer)
root.order.add_edge(fractional_offer, exclusive_choice_6)
root.order.add_edge(exclusive_choice_6, secondary_sale)
root.order.add_edge(exclusive_choice_2, loop_1)
root.order.add_edge(loop_1, loop_2)
root.order.add_edge(loop_2, exclusive_choice_2)

print(root)