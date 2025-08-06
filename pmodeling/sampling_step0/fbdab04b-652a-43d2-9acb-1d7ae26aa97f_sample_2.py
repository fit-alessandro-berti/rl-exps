root = StrictPartialOrder(nodes=[
    Transition(label='Client Consult'),
    Transition(label='Spec Analysis'),
    Transition(label='Module Select'),
    Transition(label='Component Order'),
    Transition(label='Parts Inspect'),
    Transition(label='Frame Assemble'),
    Transition(label='Sensor Install'),
    Transition(label='Motor Attach'),
    Transition(label='Wiring Connect'),
    Transition(label='Software Upload'),
    Transition(label='Calibration Test'),
    Transition(label='Flight Simulate'),
    Transition(label='Quality Review'),
    Transition(label='User Train'),
    Transition(label='Remote Setup'),
    Transition(label='Feedback Collect'),
    Transition(label='Support Schedule')
])

root.order.add_edge(root.nodes[0], root.nodes[1])
root.order.add_edge(root.nodes[1], root.nodes[2])
root.order.add_edge(root.nodes[2], root.nodes[3])
root.order.add_edge(root.nodes[3], root.nodes[4])
root.order.add_edge(root.nodes[4], root.nodes[5])
root.order.add_edge(root.nodes[5], root.nodes[6])
root.order.add_edge(root.nodes[5], root.nodes[7])
root.order.add_edge(root.nodes[5], root.nodes[8])
root.order.add_edge(root.nodes[8], root.nodes[9])
root.order.add_edge(root.nodes[9], root.nodes[10])
root.order.add_edge(root.nodes[10], root.nodes[11])
root.order.add_edge(root.nodes[11], root.nodes[12])
root.order.add_edge(root.nodes[11], root.nodes[13])
root.order.add_edge(root.nodes[11], root.nodes[14])
root.order.add_edge(root.nodes[14], root.nodes[15])
root.order.add_edge(root.nodes[15], root.nodes[16])