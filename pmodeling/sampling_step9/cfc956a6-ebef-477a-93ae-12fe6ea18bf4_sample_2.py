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

artist_onboard_loop = OperatorPOWL(operator=Operator.LOOP, children=[artist_onboard])
identity_check_loop = OperatorPOWL(operator=Operator.LOOP, children=[identity_check])
smart_deploy_loop = OperatorPOWL(operator=Operator.LOOP, children=[smart_deploy])
bid_monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[bid_monitor])
price_adjust_loop = OperatorPOWL(operator=Operator.LOOP, children=[price_adjust])
wallet_link_loop = OperatorPOWL(operator=Operator.LOOP, children=[wallet_link])
bid_submit_loop = OperatorPOWL(operator=Operator.LOOP, children=[bid_submit])
auction_close_loop = OperatorPOWL(operator=Operator.LOOP, children=[auction_close])
ownership_transfer_loop = OperatorPOWL(operator=Operator.LOOP, children=[ownership_transfer])
fund_release_loop = OperatorPOWL(operator=Operator.LOOP, children=[fund_release])
dispute_review_loop = OperatorPOWL(operator=Operator.LOOP, children=[dispute_review])
reputation_update_loop = OperatorPOWL(operator=Operator.LOOP, children=[reputation_update])
fractional_offer_loop = OperatorPOWL(operator=Operator.LOOP, children=[fractional_offer])
secondary_sale_loop = OperatorPOWL(operator=Operator.LOOP, children=[secondary_sale])

xor1 = OperatorPOWL(operator=Operator.XOR, children=[auction_close, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[auction_close, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[auction_close, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[auction_close, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[auction_close, skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[auction_close, skip])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[auction_close, skip])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[auction_close, skip])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[auction_close, skip])
xor10 = OperatorPOWL(operator=Operator.XOR, children=[auction_close, skip])

root = StrictPartialOrder(nodes=[
    artist_onboard_loop,
    identity_check_loop,
    smart_deploy_loop,
    bid_monitor_loop,
    price_adjust_loop,
    wallet_link_loop,
    bid_submit_loop,
    auction_close_loop,
    ownership_transfer_loop,
    fund_release_loop,
    dispute_review_loop,
    reputation_update_loop,
    fractional_offer_loop,
    secondary_sale_loop,
    xor1,
    xor2,
    xor3,
    xor4,
    xor5,
    xor6,
    xor7,
    xor8,
    xor9,
    xor10
])

root.order.add_edge(artist_onboard_loop, identity_check_loop)
root.order.add_edge(identity_check_loop, smart_deploy_loop)
root.order.add_edge(smart_deploy_loop, bid_monitor_loop)
root.order.add_edge(bid_monitor_loop, price_adjust_loop)
root.order.add_edge(price_adjust_loop, wallet_link_loop)
root.order.add_edge(wallet_link_loop, bid_submit_loop)
root.order.add_edge(bid_submit_loop, auction_close_loop)
root.order.add_edge(auction_close_loop, ownership_transfer_loop)
root.order.add_edge(ownership_transfer_loop, fund_release_loop)
root.order.add_edge(fund_release_loop, dispute_review_loop)
root.order.add_edge(dispute_review_loop, reputation_update_loop)
root.order.add_edge(reputation_update_loop, fractional_offer_loop)
root.order.add_edge(fractional_offer_loop, secondary_sale_loop)
root.order.add_edge(secondary_sale_loop, xor1)
root.order.add_edge(secondary_sale_loop, xor2)
root.order.add_edge(secondary_sale_loop, xor3)
root.order.add_edge(secondary_sale_loop, xor4)
root.order.add_edge(secondary_sale_loop, xor5)
root.order.add_edge(secondary_sale_loop, xor6)
root.order.add_edge(secondary_sale_loop, xor7)
root.order.add_edge(secondary_sale_loop, xor8)
root.order.add_edge(secondary_sale_loop, xor9)
root.order.add_edge(secondary_sale_loop, xor10)