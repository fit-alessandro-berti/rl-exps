root = StrictPartialOrder(nodes=[
    Transition(label='Verify Artwork'),
    Transition(label='Analyze Provenance'),
    Transition(label='Set Reserve'),
    Transition(label='Activate Auction'),
    Transition(label='Monitor Bids'),
    Transition(label='Adjust Pricing'),
    Transition(label='Enable Fractional'),
    Transition(label='Validate Bidders'),
    Transition(label='Resolve Disputes'),
    Transition(label='Distribute Royalties'),
    Transition(label='Promote Auction'),
    Transition(label='Process Payments'),
    Transition(label='Confirm Ownership'),
    Transition(label='Arrange Shipping'),
    Transition(label='Track Delivery'),
    Transition(label='Report Analytics')
])

# Define the partial order dependencies
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