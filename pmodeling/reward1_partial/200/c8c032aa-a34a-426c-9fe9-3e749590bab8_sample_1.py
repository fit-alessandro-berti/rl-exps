root = StrictPartialOrder(nodes=[
    Transition(label='Light Sourcing'),
    Transition(label='Nutrient Order'),
    Transition(label='Climate Setup'),
    Transition(label='Growth Planning'),
    Transition(label='Seed Planting'),
    Transition(label='Irrigation Check'),
    Transition(label='Pest Monitoring'),
    Transition(label='Energy Tracking'),
    Transition(label='Quality Testing'),
    Transition(label='Data Analysis'),
    Transition(label='Equipment Repair'),
    Transition(label='Packaging Prep'),
    Transition(label='Inventory Update'),
    Transition(label='Delivery Scheduling'),
    Transition(label='Customer Feedback'),
    Transition(label='Market Forecast')
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