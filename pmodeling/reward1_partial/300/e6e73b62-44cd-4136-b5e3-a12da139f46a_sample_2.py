root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Design Layout'),
    Transition(label='Procure Modules'),
    Transition(label='Install Framework'),
    Transition(label='Setup Sensors'),
    Transition(label='Calibrate Nutrients'),
    Transition(label='Configure IoT'),
    Transition(label='Plant Seeding'),
    Transition(label='Monitor Growth'),
    Transition(label='Manage Lighting'),
    Transition(label='Pest Control'),
    Transition(label='Recycle Waste'),
    Transition(label='Analyze Data'),
    Transition(label='Adjust Environment'),
    Transition(label='Harvest Crops'),
    Transition(label='Distribute Produce')
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