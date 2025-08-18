root = StrictPartialOrder(nodes=[
    Transition(label='Permit Securing'),
    Transition(label='Structure Check'),
    Transition(label='Soil Testing'),
    Transition(label='Water Analysis'),
    Transition(label='Material Sourcing'),
    Transition(label='Planter Setup'),
    Transition(label='Sensor Install'),
    Transition(label='Irrigation Setup'),
    Transition(label='Vendor Liaison'),
    Transition(label='Staff Training'),
    Transition(label='Pest Control'),
    Transition(label='Produce Marketing'),
    Transition(label='Crop Rotation'),
    Transition(label='Health Audit'),
    Transition(label='Waste Composting')
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