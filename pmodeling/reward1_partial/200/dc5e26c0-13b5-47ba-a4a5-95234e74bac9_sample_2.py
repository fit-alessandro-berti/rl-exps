root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Design Layout'),
    Transition(label='Climate Setup'),
    Transition(label='Sensor Install'),
    Transition(label='Nutrient Mix'),
    Transition(label='Automation Code'),
    Transition(label='Crop Planning'),
    Transition(label='Pest Control'),
    Transition(label='Energy Audit'),
    Transition(label='Waste Sort'),
    Transition(label='Planting Tier'),
    Transition(label='Harvest Prep'),
    Transition(label='Logistics Plan'),
    Transition(label='Community Meet'),
    Transition(label='Data Review'),
    Transition(label='System Upgrade')
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