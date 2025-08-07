root = StrictPartialOrder(nodes=[
    Transition(label='Seed Select'),
    Transition(label='Climate Map'),
    Transition(label='IoT Setup'),
    Transition(label='Nutrient Mix'),
    Transition(label='Sensor Check'),
    Transition(label='Light Adjust'),
    Transition(label='Water Cycle'),
    Transition(label='Pest Scan'),
    Transition(label='Growth Audit'),
    Transition(label='Harvest Plan'),
    Transition(label='Demand Sync'),
    Transition(label='Quality Grade'),
    Transition(label='Pack Items'),
    Transition(label='Waste Compost'),
    Transition(label='Data Review'),
    Transition(label='Cycle Reset')
])

root.order.add_edge(root.nodes[0], root.nodes[1])
root.order.add_edge(root.nodes[0], root.nodes[2])
root.order.add_edge(root.nodes[1], root.nodes[3])
root.order.add_edge(root.nodes[2], root.nodes[3])
root.order.add_edge(root.nodes[3], root.nodes[4])
root.order.add_edge(root.nodes[3], root.nodes[5])
root.order.add_edge(root.nodes[3], root.nodes[6])
root.order.add_edge(root.nodes[4], root.nodes[7])
root.order.add_edge(root.nodes[7], root.nodes[8])
root.order.add_edge(root.nodes[8], root.nodes[9])
root.order.add_edge(root.nodes[9], root.nodes[10])
root.order.add_edge(root.nodes[10], root.nodes[11])
root.order.add_edge(root.nodes[11], root.nodes[12])
root.order.add_edge(root.nodes[12], root.nodes[13])
root.order.add_edge(root.nodes[13], root.nodes[14])
root.order.add_edge(root.nodes[14], root.nodes[15])