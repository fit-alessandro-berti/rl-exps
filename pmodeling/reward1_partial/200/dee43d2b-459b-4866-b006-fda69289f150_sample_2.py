root = StrictPartialOrder(nodes=[
    Transition(label='Seed Selection'),
    Transition(label='Nutrient Mix'),
    Transition(label='Planting Setup'),
    Transition(label='Climate Control'),
    Transition(label='Water Cycling'),
    Transition(label='Growth Monitoring'),
    Transition(label='Pest Detection'),
    Transition(label='Light Adjustment'),
    Transition(label='Data Analysis'),
    Transition(label='Harvest Planning'),
    Transition(label='Crop Harvest'),
    Transition(label='Yield Sorting'),
    Transition(label='Packaging Prep'),
    Transition(label='Distribution Plan'),
    Transition(label='Regulation Check'),
    Transition(label='Waste Recycling'),
    Transition(label='System Maintenance')
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
root.order.add_edge(root.nodes[15], root.nodes[16])