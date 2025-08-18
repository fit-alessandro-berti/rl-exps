root = StrictPartialOrder(nodes=[
    Transition(label='Artifact Intake'),
    Transition(label='Condition Check'),
    Transition(label='Material Test'),
    Transition(label='Archival Search'),
    Transition(label='Style Compare'),
    Transition(label='Expert Review'),
    Transition(label='Restoration Check'),
    Transition(label='Provenance Trace'),
    Transition(label='Legal Verify'),
    Transition(label='Value Appraise'),
    Transition(label='Catalog Entry'),
    Transition(label='Marketing Plan'),
    Transition(label='Auction Setup'),
    Transition(label='Certify Final'),
    Transition(label='Sales Report')
])

root.order.add_edge(root.nodes[0], root.nodes[1])
root.order.add_edge(root.nodes[0], root.nodes[2])
root.order.add_edge(root.nodes[0], root.nodes[3])
root.order.add_edge(root.nodes[1], root.nodes[4])
root.order.add_edge(root.nodes[2], root.nodes[5])
root.order.add_edge(root.nodes[3], root.nodes[6])
root.order.add_edge(root.nodes[4], root.nodes[7])
root.order.add_edge(root.nodes[5], root.nodes[8])
root.order.add_edge(root.nodes[6], root.nodes[9])
root.order.add_edge(root.nodes[7], root.nodes[10])
root.order.add_edge(root.nodes[8], root.nodes[11])
root.order.add_edge(root.nodes[9], root.nodes[12])
root.order.add_edge(root.nodes[10], root.nodes[13])
root.order.add_edge(root.nodes[11], root.nodes[14])
root.order.add_edge(root.nodes[12], root.nodes[15])