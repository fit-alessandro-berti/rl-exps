root = StrictPartialOrder(nodes=[
    Transition(label='Verify Provenance'),
    Transition(label='Assess Condition'),
    Transition(label='Negotiate Terms'),
    Transition(label='Arrange Transport'),
    Transition(label='Customs Clearance'),
    Transition(label='Secure Insurance'),
    Transition(label='Schedule Handlers'),
    Transition(label='Install Artwork'),
    Transition(label='Monitor Climate'),
    Transition(label='Manage Security'),
    Transition(label='Facilitate Access'),
    Transition(label='Document Display'),
    Transition(label='Coordinate Events'),
    Transition(label='Inspect Periodically'),
    Transition(label='Plan Return'),
    Transition(label='Deinstall Artwork'),
    Transition(label='Finalize Reports')
])

# Define dependencies between activities
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