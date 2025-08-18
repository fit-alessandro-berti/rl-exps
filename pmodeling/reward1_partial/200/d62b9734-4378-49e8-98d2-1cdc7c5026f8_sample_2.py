root = StrictPartialOrder(nodes=[
    Transition(label='Provenance Check'),
    Transition(label='Image Capture'),
    Transition(label='Material Scan'),
    Transition(label='Expert Review'),
    Transition(label='Historical Cross'),
    Transition(label='Legal Verify'),
    Transition(label='Registry Search'),
    Transition(label='Customs Clear'),
    Transition(label='Condition Assess'),
    Transition(label='Data Log'),
    Transition(label='Chain Custody'),
    Transition(label='Report Draft'),
    Transition(label='Certification'),
    Transition(label='Secure Archive'),
    Transition(label='Auction Prep')
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