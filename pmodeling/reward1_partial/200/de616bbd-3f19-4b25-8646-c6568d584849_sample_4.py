root = StrictPartialOrder(nodes=[
    Transition(label='Site Analysis'),
    Transition(label='Structural Check'),
    Transition(label='System Design'),
    Transition(label='Hydroponics Setup'),
    Transition(label='Lighting Install'),
    Transition(label='Sensor Install'),
    Transition(label='Climate Control'),
    Transition(label='Nutrient Monitor'),
    Transition(label='Seed Selection'),
    Transition(label='Germination Start'),
    Transition(label='Auto Planting'),
    Transition(label='Growth Monitoring'),
    Transition(label='AI Analytics'),
    Transition(label='Robotic Harvest'),
    Transition(label='Packaging'),
    Transition(label='Trace Labeling'),
    Transition(label='Logistics Plan')
])

root.order.add_edge(root.nodes[0], root.nodes[1])
root.order.add_edge(root.nodes[1], root.nodes[2])
root.order.add_edge(root.nodes[2], root.nodes[3])
root.order.add_edge(root.nodes[2], root.nodes[4])
root.order.add_edge(root.nodes[2], root.nodes[5])
root.order.add_edge(root.nodes[2], root.nodes[6])
root.order.add_edge(root.nodes[2], root.nodes[7])
root.order.add_edge(root.nodes[2], root.nodes[8])
root.order.add_edge(root.nodes[2], root.nodes[9])
root.order.add_edge(root.nodes[2], root.nodes[10])
root.order.add_edge(root.nodes[2], root.nodes[11])
root.order.add_edge(root.nodes[2], root.nodes[12])
root.order.add_edge(root.nodes[2], root.nodes[13])
root.order.add_edge(root.nodes[2], root.nodes[14])
root.order.add_edge(root.nodes[2], root.nodes[15])