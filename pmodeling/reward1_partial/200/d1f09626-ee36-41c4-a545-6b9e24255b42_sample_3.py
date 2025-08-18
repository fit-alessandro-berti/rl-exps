root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Load Test'),
    Transition(label='Soil Sample'),
    Transition(label='Climate Check'),
    Transition(label='Crop Select'),
    Transition(label='Irrigation Plan'),
    Transition(label='Energy Setup'),
    Transition(label='Pest Control'),
    Transition(label='Permit Obtain'),
    Transition(label='Stakeholder Meet'),
    Transition(label='Bed Construction'),
    Transition(label='Seed Planting'),
    Transition(label='Water Schedule'),
    Transition(label='Growth Monitor'),
    Transition(label='Harvest Plan'),
    Transition(label='Waste Recycle'),
    Transition(label='Yield Report')
])

# Define the dependencies
root.order.add_edge(root.nodes[0], root.nodes[1])
root.order.add_edge(root.nodes[0], root.nodes[2])
root.order.add_edge(root.nodes[0], root.nodes[3])
root.order.add_edge(root.nodes[0], root.nodes[4])
root.order.add_edge(root.nodes[1], root.nodes[5])
root.order.add_edge(root.nodes[2], root.nodes[6])
root.order.add_edge(root.nodes[3], root.nodes[7])
root.order.add_edge(root.nodes[4], root.nodes[8])
root.order.add_edge(root.nodes[5], root.nodes[9])
root.order.add_edge(root.nodes[6], root.nodes[10])
root.order.add_edge(root.nodes[7], root.nodes[11])
root.order.add_edge(root.nodes[8], root.nodes[12])
root.order.add_edge(root.nodes[9], root.nodes[13])
root.order.add_edge(root.nodes[10], root.nodes[14])
root.order.add_edge(root.nodes[11], root.nodes[15])