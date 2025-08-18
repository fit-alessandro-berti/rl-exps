root = StrictPartialOrder(nodes=[
    Transition(label='Client Consult'),
    Transition(label='Spec Gathering'),
    Transition(label='Supplier Sourcing'),
    Transition(label='Design Review'),
    Transition(label='Simulation Test'),
    Transition(label='Proto Assembly'),
    Transition(label='Quality Check'),
    Transition(label='Firmware Flash'),
    Transition(label='Sensor Install'),
    Transition(label='Final Testing'),
    Transition(label='Brand Packaging'),
    Transition(label='Shipping Prep'),
    Transition(label='Delivery Schedule'),
    Transition(label='Client Training'),
    Transition(label='Diagnostics Setup')
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