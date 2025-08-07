import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
onboard = Transition(label='Artist Onboard')
verify = Transition(label='Asset Verify')
identity = Transition(label='Identity Check')
deploy = Transition(label='Smart Deploy')
monitor = Transition(label='Bid Monitor')
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

# Silent transition for loop exits
skip = SilentTransition()

# Loop for dynamic pricing: monitor, then optionally adjust & repeat
pricing_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[monitor, adjust]
)

# Exclusive choice for secondary sale or fractional offer
secondary_xor = OperatorPOWL(
    operator=Operator.XOR,
    children=[secondary, fractional]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    onboard,
    verify,
    identity,
    deploy,
    pricing_loop,
    link,
    submit,
    close,
    transfer,
    release,
    review,
    update,
    secondary_xor
])

# Define the control-flow edges
root.order.add_edge(onboard, verify)
root.order.add_edge(verify, identity)
root.order.add_edge(identity, deploy)
root.order.add_edge(deploy, pricing_loop)
root.order.add_edge(pricing_loop, link)
root.order.add_edge(link, submit)
root.order.add_edge(submit, close)
root.order.add_edge(close, transfer)
root.order.add_edge(transfer, release)
root.order.add_edge(release, review)
root.order.add_edge(review, update)
root.order.add_edge(update, secondary_xor)
root.order.add_edge(secondary_xor, skip)  # exit loop or secondary offer