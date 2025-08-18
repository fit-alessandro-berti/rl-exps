root = StrictPartialOrder(nodes=[
    Transition(label='Assess Structure'),
    Transition(label='Analyze Environment'),
    Transition(label='Design Modules'),
    Transition(label='Procure Materials'),
    Transition(label='Install Irrigation'),
    Transition(label='Set Sensors'),
    Transition(label='Select Seeds'),
    Transition(label='Schedule Planting'),
    Transition(label='Monitor Growth'),
    Transition(label='Collect Data'),
    Transition(label='Manage Pests'),
    Transition(label='Harvest Crops'),
    Transition(label='Coordinate Sales'),
    Transition(label='Compost Waste'),
    Transition(label='Review Feedback')
])

root.order.add_edge(root.nodes[0], root.nodes[1])
root.order.add_edge(root.nodes[0], root.nodes[2])
root.order.add_edge(root.nodes[1], root.nodes[3])
root.order.add_edge(root.nodes[2], root.nodes[3])
root.order.add_edge(root.nodes[3], root.nodes[4])
root.order.add_edge(root.nodes[3], root.nodes[5])
root.order.add_edge(root.nodes[4], root.nodes[6])
root.order.add_edge(root.nodes[5], root.nodes[6])
root.order.add_edge(root.nodes[6], root.nodes[7])
root.order.add_edge(root.nodes[6], root.nodes[8])
root.order.add_edge(root.nodes[8], root.nodes[9])
root.order.add_edge(root.nodes[8], root.nodes[10])
root.order.add_edge(root.nodes[9], root.nodes[11])
root.order.add_edge(root.nodes[10], root.nodes[11])
root.order.add_edge(root.nodes[11], root.nodes[12])
root.order.add_edge(root.nodes[11], root.nodes[13])
root.order.add_edge(root.nodes[12], root.nodes[14])
root.order.add_edge(root.nodes[13], root.nodes[14])
root.order.add_edge(root.nodes[14], root.nodes[15])