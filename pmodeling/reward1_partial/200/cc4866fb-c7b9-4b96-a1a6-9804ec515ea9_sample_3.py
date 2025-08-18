root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Design Planning'),
    Transition(label='Permit Filing'),
    Transition(label='Structural Reinforce'),
    Transition(label='Hydroponic Setup'),
    Transition(label='Sensor Install'),
    Transition(label='Energy Audit'),
    Transition(label='Crop Selection'),
    Transition(label='Nutrient Mix'),
    Transition(label='Waste Process'),
    Transition(label='Climate Control'),
    Transition(label='Staff Training'),
    Transition(label='Market Study'),
    Transition(label='Community Meet'),
    Transition(label='Launch Trial'),
    Transition(label='Data Monitor')
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