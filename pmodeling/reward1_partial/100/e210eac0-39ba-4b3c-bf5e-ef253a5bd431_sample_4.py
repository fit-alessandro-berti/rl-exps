root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Regulation Check'),
    Transition(label='Modular Design'),
    Transition(label='Material Sourcing'),
    Transition(label='Energy Integration'),
    Transition(label='Climate Setup'),
    Transition(label='Nutrient Mix'),
    Transition(label='System Assembly'),
    Transition(label='Automation Config'),
    Transition(label='Crop Seeding'),
    Transition(label='Growth Monitoring'),
    Transition(label='Waste Handling'),
    Transition(label='Community Meet'),
    Transition(label='Data Analysis'),
    Transition(label='Feedback Loop'),
    Transition(label='Yield Forecast')
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
root.order.add_edge(root.nodes[14], root.nodes[15])