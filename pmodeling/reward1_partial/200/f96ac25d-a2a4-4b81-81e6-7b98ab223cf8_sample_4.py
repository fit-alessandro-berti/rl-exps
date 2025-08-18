root = StrictPartialOrder(nodes=[
    Transition(label='Client Brief'),
    Transition(label='Concept Sketch'),
    Transition(label='Design Review'),
    Transition(label='Material Sourcing'),
    Transition(label='Prototype Build'),
    Transition(label='Vendor Coordination'),
    Transition(label='Quality Check'),
    Transition(label='Client Approval'),
    Transition(label='Packaging Prep'),
    Transition(label='Shipping Arrange'),
    Transition(label='Feedback Collect'),
    Transition(label='Portfolio Update'),
    Transition(label='Contract Sign'),
    Transition(label='IP Management'),
    Transition(label='Future Schedule'),
    Transition(label='Maintenance Plan')
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