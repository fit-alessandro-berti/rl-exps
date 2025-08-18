import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define loop and XOR nodes
loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor, adjust, link, submit])
xor = OperatorPOWL(operator=Operator.XOR, children=[close, review, update])

# Define the root node
root = StrictPartialOrder(nodes=[onboard, verify, identity, deploy, loop, xor])
root.order.add_edge(onboard, verify)
root.order.add_edge(verify, identity)
root.order.add_edge(identity, deploy)
root.order.add_edge(deploy, loop)
root.order.add_edge(loop, xor)