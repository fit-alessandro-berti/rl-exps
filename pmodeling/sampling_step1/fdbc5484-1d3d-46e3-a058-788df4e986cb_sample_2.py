import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the POWL model
root = StrictPartialOrder(nodes=[
    Transition(label='Asset ID'),
    Transition(label='Value Assess'),
    Transition(label='Risk Scan'),
    Transition(label='Market Review'),
    Transition(label='Initial Offer'),
    Transition(label='Counter Offer'),
    Transition(label='Negotiation'),
    Transition(label='Contract Draft'),
    Transition(label='Legal Review'),
    Transition(label='Digital Sign'),
    Transition(label='Royalty Setup'),
    Transition(label='Transfer Record'),
    Transition(label='Compliance Check'),
    Transition(label='Audit Schedule'),
    Transition(label='Market Feedback'),
    Transition(label='Strategy Update')
])

# Define the partial order
root.order.add_edge(root.nodes[0], root.nodes[1])
root.order.add_edge(root.nodes[1], root.nodes[2])
root.order.add_edge(root.nodes[2], root.nodes[3])
root.order.add_edge(root.nodes[3], root.nodes[4])
root.order.add_edge(root.nodes[4], root.nodes[5])
root.order.add_edge(root.nodes[5], root.nodes[6])
root.order.add_edge(root.nodes[6], root.nodes[7])
root.order.add_edge(root.nodes[7], root.nodes[8])
root.order.add_edge(root.nodes[8], root.nodes[9])
root.order.add_edge(root.nodes[9], root.nodes[10])
root.order.add_edge(root.nodes[10], root.nodes[11])
root.order.add_edge(root.nodes[11], root.nodes[12])
root.order.add_edge(root.nodes[12], root.nodes[13])
root.order.add_edge(root.nodes[13], root.nodes[14])
root.order.add_edge(root.nodes[14], root.nodes[15])
root.order.add_edge(root.nodes[15], root.nodes[16])

# Print the POWL model
print(root)