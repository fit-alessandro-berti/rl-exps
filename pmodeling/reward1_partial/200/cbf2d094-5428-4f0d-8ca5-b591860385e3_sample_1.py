root = StrictPartialOrder(nodes=[
    Transition(label='Seed Select'),
    Transition(label='Nutrient Mix'),
    Transition(label='Climate Adjust'),
    Transition(label='Planting Robotic'),
    Transition(label='Growth Monitor'),
    Transition(label='Pest Control'),
    Transition(label='Water Recycle'),
    Transition(label='Light Optimize'),
    Transition(label='Growth Analyze'),
    Transition(label='Harvest Sync'),
    Transition(label='Sterilize Crop'),
    Transition(label='Package Fresh'),
    Transition(label='Demand Forecast'),
    Transition(label='Delivery Plan'),
    Transition(label='Data Feedback')
])

root.order.add_edge(root.nodes[0], root.nodes[1])
root.order.add_edge(root.nodes[0], root.nodes[2])
root.order.add_edge(root.nodes[1], root.nodes[3])
root.order.add_edge(root.nodes[3], root.nodes[4])
root.order.add_edge(root.nodes[4], root.nodes[5])
root.order.add_edge(root.nodes[4], root.nodes[6])
root.order.add_edge(root.nodes[4], root.nodes[7])
root.order.add_edge(root.nodes[5], root.nodes[8])
root.order.add_edge(root.nodes[8], root.nodes[9])
root.order.add_edge(root.nodes[9], root.nodes[10])
root.order.add_edge(root.nodes[10], root.nodes[11])
root.order.add_edge(root.nodes[10], root.nodes[12])
root.order.add_edge(root.nodes[11], root.nodes[13])
root.order.add_edge(root.nodes[13], root.nodes[14])
root.order.add_edge(root.nodes[14], root.nodes[15])