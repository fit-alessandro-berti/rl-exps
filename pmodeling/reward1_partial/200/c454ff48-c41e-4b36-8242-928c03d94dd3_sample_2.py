root = StrictPartialOrder(nodes=[
    Transition(label='Site Assess'),
    Transition(label='Permit Obtain'),
    Transition(label='Soil Testing'),
    Transition(label='Crop Select'),
    Transition(label='Irrigation Setup'),
    Transition(label='Drainage Install'),
    Transition(label='Energy Integrate'),
    Transition(label='Staff Train'),
    Transition(label='Pest Control'),
    Transition(label='Logistics Plan'),
    Transition(label='Supply Coordinate'),
    Transition(label='Distribution Map'),
    Transition(label='Community Engage'),
    Transition(label='Monitoring Setup'),
    Transition(label='Yield Optimize')
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