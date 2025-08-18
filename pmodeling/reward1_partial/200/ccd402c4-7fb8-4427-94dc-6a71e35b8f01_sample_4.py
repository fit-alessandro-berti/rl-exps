root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Permit Filing'),
    Transition(label='Stakeholder Meet'),
    Transition(label='Design Layout'),
    Transition(label='IoT Install'),
    Transition(label='Sensor Calibrate'),
    Transition(label='Hydroponic Setup'),
    Transition(label='Nutrient Mix'),
    Transition(label='Seed Sowing'),
    Transition(label='Climate Control'),
    Transition(label='Data Monitor'),
    Transition(label='Yield Forecast'),
    Transition(label='Energy Plan'),
    Transition(label='Maintenance Plan'),
    Transition(label='Harvest Prep'),
    Transition(label='Supply Dispatch'),
    Transition(label='Market Launch')
])

# Define the dependencies between activities
root.order.add_edge(root.nodes[0], root.nodes[1])
root.order.add_edge(root.nodes[0], root.nodes[2])
root.order.add_edge(root.nodes[1], root.nodes[3])
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