import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define silent transitions
skip = SilentTransition()

# Define the loop for smart contract deployment and bid monitoring
loop = OperatorPOWL(operator=Operator.LOOP, children=[deploy, monitor])

# Define the exclusive choice for price adjustment and wallet linking
xor = OperatorPOWL(operator=Operator.XOR, children=[adjust, link])

# Define the exclusive choice for bid submission and auction closure
xor2 = OperatorPOWL(operator=Operator.XOR, children=[submit, close])

# Define the exclusive choice for ownership transfer and fund release
xor3 = OperatorPOWL(operator=Operator.XOR, children=[transfer, release])

# Define the exclusive choice for dispute review and reputation update
xor4 = OperatorPOWL(operator=Operator.XOR, children=[review, update])

# Define the exclusive choice for fractional offer and secondary sale
xor5 = OperatorPOWL(operator=Operator.XOR, children=[fractional, secondary])

# Define the root POWL model
root = StrictPartialOrder(nodes=[loop, xor, xor2, xor3, xor4, xor5])

# Add dependencies to the root model
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)

# Print the root model
print(root)