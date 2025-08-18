root = StrictPartialOrder(nodes=[
    Transition(label='Site Assess'),
    Transition(label='Env Analysis'),
    Transition(label='Modular Install'),
    Transition(label='Irrigation Setup'),
    Transition(label='Crop Selection'),
    Transition(label='Nutrient Mix'),
    Transition(label='Lighting Calibrate'),
    Transition(label='Pest Monitor'),
    Transition(label='Staff Training'),
    Transition(label='Energy Integrate'),
    Transition(label='Data Analytics'),
    Transition(label='Waste Recycle'),
    Transition(label='Market Develop'),
    Transition(label='Yield Optimize'),
    Transition(label='Climate Simulate')
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