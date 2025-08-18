root = StrictPartialOrder(nodes=[
    Transition(label='Inquiry Review'),
    Transition(label='Client Onboard'),
    Transition(label='Concept Draft'),
    Transition(label='Feedback Cycle'),
    Transition(label='Contract Setup'),
    Transition(label='Payment Schedule'),
    Transition(label='Material Sourcing'),
    Transition(label='Artwork Create'),
    Transition(label='Quality Check'),
    Transition(label='Frame Selection'),
    Transition(label='Packaging Prep'),
    Transition(label='Shipment Arrange'),
    Transition(label='Delivery Confirm'),
    Transition(label='Post-Sale Support'),
    Transition(label='Revision Manage'),
    Transition(label='Delay Mitigate')
])

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