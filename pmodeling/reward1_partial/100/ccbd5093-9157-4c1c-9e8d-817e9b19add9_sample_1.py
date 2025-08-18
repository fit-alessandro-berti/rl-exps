root = StrictPartialOrder(nodes=[
    Transition(label='Scan Markets'),
    Transition(label='Host Workshops'),
    Transition(label='Form Teams'),
    Transition(label='Develop Prototypes'),
    Transition(label='Simulate Tests'),
    Transition(label='Collect Feedback'),
    Transition(label='Review Ethics'),
    Transition(label='Conduct Analysis'),
    Transition(label='Identify Partners'),
    Transition(label='Align Strategy'),
    Transition(label='Launch Pilots'),
    Transition(label='Monitor Trends'),
    Transition(label='AI Analytics'),
    Transition(label='Pivot Plans'),
    Transition(label='Cycle Renewal')
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
root.order.add_edge(root.nodes[12], root.nodes[0])