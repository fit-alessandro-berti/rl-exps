root = StrictPartialOrder(nodes=[
    Transition(label='Sensor Setup'),
    Transition(label='Data Capture'),
    Transition(label='Nutrient Mix'),
    Transition(label='Crop Rotate'),
    Transition(label='Waste Collect'),
    Transition(label='Compost Process'),
    Transition(label='Drone Dispatch'),
    Transition(label='Pest Control'),
    Transition(label='Pollination Run'),
    Transition(label='Volunteer Assign'),
    Transition(label='Feedback Gather'),
    Transition(label='Model Update'),
    Transition(label='Yield Forecast'),
    Transition(label='Water Adjust'),
    Transition(label='Report Generate'),
    Transition(label='Resource Audit'),
    Transition(label='Schedule Sync')
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
root.order.add_edge(root.nodes[15], root.nodes[16])
root.order.add_edge(root.nodes[16], root.nodes[17])
root.order.add_edge(root.nodes[17], root.nodes[18])