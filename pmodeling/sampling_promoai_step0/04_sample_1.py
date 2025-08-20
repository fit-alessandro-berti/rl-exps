root = StrictPartialOrder(nodes=[
    Transition(label='Define campaign objectives'),
    Transition(label='Create content'),
    Transition(label='Design visuals'),
    Transition(label='Select promotion channels'),
    Transition(label='Launch campaign'),
    Transition(label='Collect leads in CRM system'),
    Transition(label='Track performance in real-time'),
    Transition(label='Sales teams follows up on leads'),
    Transition(label='Analyze performance for future optimization'),
    Transition(label='Campaign period ends')
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