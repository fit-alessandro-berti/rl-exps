root = StrictPartialOrder(
    nodes=[
        Transition('Site Analysis'),
        Transition('Structural Check'),
        Transition('Rack Install'),
        Transition('System Setup'),
        Transition('Hydroponics Config'),
        Transition('Aeroponics Tune'),
        Transition('Lighting Setup'),
        Transition('Enviro Control'),
        Transition('Sensor Deploy'),
        Transition('Waste Recycle'),
        Transition('Water Reuse'),
        Transition('Staff Training'),
        Transition('Test Grow'),
        Transition('Data Analytics'),
        Transition('Yield Optimize')
    ]
)

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