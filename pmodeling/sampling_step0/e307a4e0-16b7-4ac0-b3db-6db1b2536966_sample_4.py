root = StrictPartialOrder(nodes=[
    Transition(label='Initial Assess'),
    Transition(label='Artifact Scan'),
    Transition(label='Condition Map'),
    Transition(label='Material Test'),
    Transition(label='Cleaning Phase'),
    Transition(label='Stability Check'),
    Transition(label='Minor Repair'),
    Transition(label='Structural Reinforce'),
    Transition(label='Surface Restore'),
    Transition(label='Coating Apply'),
    Transition(label='Ethics Review'),
    Transition(label='Provenance Verify'),
    Transition(label='Client Update'),
    Transition(label='Final Report'),
    Transition(label='Archive Store')
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