root = StrictPartialOrder(nodes=[
    Transition(label='Receive Artifact'),
    Transition(label='Condition Log'),
    Transition(label='Radiocarbon Test'),
    Transition(label='Spectroscopy Scan'),
    Transition(label='Expert Consult'),
    Transition(label='Provenance Check'),
    Transition(label='Archive Search'),
    Transition(label='Risk Assess'),
    Transition(label='3D Scan'),
    Transition(label='Legal Review'),
    Transition(label='Insurance Setup'),
    Transition(label='Certificate Draft'),
    Transition(label='Certificate Approve'),
    Transition(label='Climate Pack'),
    Transition(label='Conservation Plan'),
    Transition(label='Monitoring Schedule')
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