import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the control flow operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[identity_check, asset_verify])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[smart_deploy, wallet_link])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[bid_submit, bid_monitor])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[auction_close, price_adjust])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[ownership_transfer, fund_release])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[dispute_review, reputation_update])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[fractional_offer, secondary_sale])

# Define the partial order
root = StrictPartialOrder(nodes=[artist_onboard, xor1, xor2, xor3, xor4, xor5, xor6, xor7])
root.order.add_edge(artist_onboard, xor1)
root.order.add_edge(artist_onboard, xor2)
root.order.add_edge(xor1, xor3)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor4, xor6)
root.order.add_edge(xor5, xor7)
root.order.add_edge(xor6, xor7)