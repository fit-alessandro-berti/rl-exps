root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Load Test'),
    Transition(label='Climate Study'),
    Transition(label='Permit Check'),
    Transition(label='System Design'),
    Transition(label='Equipment Buy'),
    Transition(label='Sensor Setup'),
    Transition(label='Irrigation Fit'),
    Transition(label='Solar Install'),
    Transition(label='Staff Train'),
    Transition(label='Pilot Plant'),
    Transition(label='Data Monitor'),
    Transition(label='Crop Harvest'),
    Transition(label='Maintenance Plan'),
    Transition(label='Community Meet')
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