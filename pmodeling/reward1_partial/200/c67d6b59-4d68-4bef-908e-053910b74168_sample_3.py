root = StrictPartialOrder(nodes=[
    Transition(label='Client Meet'),
    Transition(label='Design Draft'),
    Transition(label='Vendor Select'),
    Transition(label='Component Order'),
    Transition(label='Parts Inspect'),
    Transition(label='Frame Build'),
    Transition(label='Wiring Setup'),
    Transition(label='Software Load'),
    Transition(label='Flight Sim'),
    Transition(label='Quality Test'),
    Transition(label='Feedback Review'),
    Transition(label='Adjust Design'),
    Transition(label='Compliance Check'),
    Transition(label='Packaging Prep'),
    Transition(label='Final Demo'),
    Transition(label='Ship Drone')
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
root.order.add_edge(root.nodes[14], root.nodes[15])