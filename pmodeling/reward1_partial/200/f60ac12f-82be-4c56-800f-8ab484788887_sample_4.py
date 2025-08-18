root = StrictPartialOrder(nodes=[
    Transition(label='Milk Sourcing'),
    Transition(label='Culture Blending'),
    Transition(label='Milk Pasteurize'),
    Transition(label='Curd Cutting'),
    Transition(label='Whey Drain'),
    Transition(label='Mold Inoculate'),
    Transition(label='Press Cheese'),
    Transition(label='Salt Brine'),
    Transition(label='Age Monitor'),
    Transition(label='Quality Test'),
    Transition(label='Packaging Prep'),
    Transition(label='Label Design'),
    Transition(label='Order Allocation'),
    Transition(label='Transport Arrange'),
    Transition(label='Retail Sync'),
    Transition(label='Customer Review'),
    Transition(label='Feedback Analyze')
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