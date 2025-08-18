root = StrictPartialOrder(nodes=[
    Transition(label='Seed Sourcing'),
    Transition(label='Farm Scheduling'),
    Transition(label='Sensor Monitoring'),
    Transition(label='Nutrient Cycling'),
    Transition(label='Crop Forecasting'),
    Transition(label='Pest Inspection'),
    Transition(label='Harvest Timing'),
    Transition(label='Quality Check'),
    Transition(label='Eco Packaging'),
    Transition(label='Storage Allocation'),
    Transition(label='Order Processing'),
    Transition(label='Route Planning'),
    Transition(label='Vehicle Dispatch'),
    Transition(label='Customer Feedback'),
    Transition(label='Demand Analysis'),
    Transition(label='Waste Management'),
    Transition(label='Community Outreach')
])

# Define the dependencies
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