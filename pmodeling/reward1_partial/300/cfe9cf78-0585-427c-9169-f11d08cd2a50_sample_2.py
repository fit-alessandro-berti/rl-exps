root = StrictPartialOrder(nodes=[
    Transition(label='Site Analysis'),
    Transition(label='Env Assessment'),
    Transition(label='System Design'),
    Transition(label='Equipment Order'),
    Transition(label='Seed Selection'),
    Transition(label='Install Modules'),
    Transition(label='Calibrate Systems'),
    Transition(label='Staff Training'),
    Transition(label='Plant Seeding'),
    Transition(label='IoT Monitoring'),
    Transition(label='Data Analytics'),
    Transition(label='Nutrient Adjust'),
    Transition(label='Pest Control'),
    Transition(label='Maintenance Check'),
    Transition(label='Market Launch'),
    Transition(label='Logistics Setup'),
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