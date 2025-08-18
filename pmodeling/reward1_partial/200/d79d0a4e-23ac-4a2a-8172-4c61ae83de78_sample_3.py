root = StrictPartialOrder(nodes=[
    Transition(label='Spec Review'),
    Transition(label='Component Pick'),
    Transition(label='Frame Build'),
    Transition(label='Motor Mount'),
    Transition(label='Sensor Fit'),
    Transition(label='Wiring Setup'),
    Transition(label='Software Load'),
    Transition(label='Calibration Test'),
    Transition(label='Stress Check'),
    Transition(label='Firmware Flash'),
    Transition(label='Feedback Loop'),
    Transition(label='Package Prep'),
    Transition(label='Doc Compile'),
    Transition(label='Ship Arrange'),
    Transition(label='Remote Setup')
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