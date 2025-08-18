import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
onboard = Transition(label='Artist Onboard')
verify = Transition(label='Asset Verify')
check = Transition(label='Identity Check')
deploy = Transition(label='Smart Deploy')
bid_monitor = Transition(label='Bid Monitor')
adjust = Transition(label='Price Adjust')
link = Transition(label='Wallet Link')
submit = Transition(label='Bid Submit')
close = Transition(label='Auction Close')
transfer = Transition(label='Ownership Transfer')
release = Transition(label='Fund Release')
review = Transition(label='Dispute Review')
update = Transition(label='Reputation Update')
fractional = Transition(label='Fractional Offer')
secondary = Transition(label='Secondary Sale')

# Define the POWL model
root = StrictPartialOrder(nodes=[onboard, verify, check, deploy, bid_monitor, adjust, link, submit, close, transfer, release, review, update, fractional, secondary])
root.order.add_edge(onboard, verify)
root.order.add_edge(verify, check)
root.order.add_edge(check, deploy)
root.order.add_edge(deploy, bid_monitor)
root.order.add_edge(bid_monitor, adjust)
root.order.add_edge(adjust, link)
root.order.add_edge(link, submit)
root.order.add_edge(submit, close)
root.order.add_edge(close, transfer)
root.order.add_edge(transfer, release)
root.order.add_edge(release, review)
root.order.add_edge(review, update)
root.order.add_edge(update, fractional)
root.order.add_edge(fractional, secondary)