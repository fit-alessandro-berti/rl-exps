from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL transitions
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

# Define the POWL operators
xor_operator = OperatorPOWL(operator=Operator.XOR, children=[
    OperatorPOWL(operator=Operator.LOOP, children=[bid_submit, bid_monitor, price_adjust]),
    OperatorPOWL(operator=Operator.LOOP, children=[identity_check, smart_deploy, wallet_link])
])
loop_operator = OperatorPOWL(operator=Operator.LOOP, children=[auction_close, ownership_transfer, fund_release])
xor_operator_2 = OperatorPOWL(operator=Operator.XOR, children=[
    OperatorPOWL(operator=Operator.LOOP, children=[dispute_review, reputation_update]),
    OperatorPOWL(operator=Operator.LOOP, children=[fractional_offer, secondary_sale])
])

# Define the POWL root
root = StrictPartialOrder(nodes=[artist_onboard, asset_verify, xor_operator, loop_operator, xor_operator_2])
root.order.add_edge(artist_onboard, asset_verify)
root.order.add_edge(asset_verify, xor_operator)
root.order.add_edge(xor_operator, loop_operator)
root.order.add_edge(loop_operator, xor_operator_2)

print(root)