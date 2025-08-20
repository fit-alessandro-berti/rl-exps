root = StrictPartialOrder(nodes=[
    Transition(label='Customer searches for ticket'),
    Transition(label='Select route'),
    Transition(label='Select date and time'),
    Transition(label='Provide personal information'),
    Transition(label='Provide payment details'),
    Transition(label='Generate ticket'),
    Transition(label='Send ticket via email'),
    Transition(label='Send ticket via SMS'),
    Transition(label='Send instructions'),
    Transition(label='Send reminder'),
    Transition(label='Post-travel feedback or services'),
    Transition(label='Customer completes journey')
])

root.order.add_edge(root.nodes[0], root.nodes[1])
root.order.add_edge(root.nodes[0], root.nodes[2])
root.order.add_edge(root.nodes[0], root.nodes[3])
root.order.add_edge(root.nodes[0], root.nodes[4])
root.order.add_edge(root.nodes[0], root.nodes[5])
root.order.add_edge(root.nodes[1], root.nodes[2])
root.order.add_edge(root.nodes[2], root.nodes[3])
root.order.add_edge(root.nodes[3], root.nodes[4])
root.order.add_edge(root.nodes[4], root.nodes[5])
root.order.add_edge(root.nodes[5], root.nodes[6])
root.order.add_edge(root.nodes[5], root.nodes[7])
root.order.add_edge(root.nodes[5], root.nodes[8])
root.order.add_edge(root.nodes[5], root.nodes[9])
root.order.add_edge(root.nodes[5], root.nodes[10])
root.order.add_edge(root.nodes[10], root.nodes[11])