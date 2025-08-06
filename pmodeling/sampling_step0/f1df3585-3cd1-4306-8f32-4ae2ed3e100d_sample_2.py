root = StrictPartialOrder(nodes=[
    Transition(label='Site Assess'),
    Transition(label='Plan Layout'),
    Transition(label='Install Racks'),
    Transition(label='Mix Nutrients'),
    Transition(label='Calibrate Sensors'),
    Transition(label='Setup Lighting'),
    Transition(label='Configure Climate'),
    Transition(label='Select Seeds'),
    Transition(label='Monitor Germinate'),
    Transition(label='Apply Bio-controls'),
    Transition(label='Maintain Systems'),
    Transition(label='Analyze Data'),
    Transition(label='Harvest Crops'),
    Transition(label='Quality Check'),
    Transition(label='Package Produce'),
    Transition(label='Distribute Goods')
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