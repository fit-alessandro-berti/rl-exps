root = StrictPartialOrder(nodes=[
    Transition(label='Opportunity Scan'),
    Transition(label='Idea Workshop'),
    Transition(label='Concept Merge'),
    Transition(label='Resource Align'),
    Transition(label='Prototype Build'),
    Transition(label='Feasibility Test'),
    Transition(label='Pilot Launch'),
    Transition(label='Feedback Gather'),
    Transition(label='Design Adapt'),
    Transition(label='Compliance Check'),
    Transition(label='Scaling Plan'),
    Transition(label='IP Management'),
    Transition(label='Market Sync'),
    Transition(label='Partner Review'),
    Transition(label='Exit Strategy')
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