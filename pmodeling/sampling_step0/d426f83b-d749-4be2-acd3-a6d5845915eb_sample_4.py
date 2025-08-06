root = StrictPartialOrder(nodes=[
    Transition(label='Asset Intake'),
    Transition(label='Provenance Check'),
    Transition(label='Material Sampling'),
    Transition(label='Radiocarbon Test'),
    Transition(label='Style Compare'),
    Transition(label='Historical Search'),
    Transition(label='Expert Consult'),
    Transition(label='Condition Review'),
    Transition(label='Scientific Analysis'),
    Transition(label='Data Compilation'),
    Transition(label='Peer Review'),
    Transition(label='Report Draft'),
    Transition(label='Certification'),
    Transition(label='Digital Archive'),
    Transition(label='Client Delivery')
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