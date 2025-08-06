root = StrictPartialOrder(nodes=[
    Transition('Site Review'),
    Transition('Impact Study'),
    Transition('Design Plan'),
    Transition('Structure Mod'),
    Transition('Hydroponics Setup'),
    Transition('Crop Select'),
    Transition('Nutrient Mix'),
    Transition('Pest Control'),
    Transition('Sensor Install'),
    Transition('Staff Train'),
    Transition('Compliance Audit'),
    Transition('Packaging Dev'),
    Transition('Logistics Plan'),
    Transition('Community Engage'),
    Transition('Sustainability Check')
])

# Define the partial order edges
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