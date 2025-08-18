root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Env Assessment'),
    Transition(label='Reg Compliance'),
    Transition(label='Modular Setup'),
    Transition(label='Crop Selection'),
    Transition(label='IoT Integration'),
    Transition(label='Nutrient Flow'),
    Transition(label='Light Calibration'),
    Transition(label='Staff Training'),
    Transition(label='Pest Control'),
    Transition(label='Market Strategy'),
    Transition(label='Logistics Plan'),
    Transition(label='Yield Analysis'),
    Transition(label='Data Review'),
    Transition(label='Community Engage')
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