root = StrictPartialOrder(nodes=[
    Transition(label='Provenance Check'),
    Transition(label='Material Scan'),
    Transition(label='Style Compare'),
    Transition(label='AI Imaging'),
    Transition(label='Chemical Test'),
    Transition(label='Aging Verify'),
    Transition(label='Record Match'),
    Transition(label='Database Query'),
    Transition(label='Panel Review'),
    Transition(label='Forgery Risk'),
    Transition(label='Market Value'),
    Transition(label='Report Draft'),
    Transition(label='Certification'),
    Transition(label='Approval Stage'),
    Transition(label='Secure Packing'),
    Transition(label='Transport Prep')
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