root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Design Layout'),
    Transition(label='Select Crops'),
    Transition(label='Install Modules'),
    Transition(label='Setup Sensors'),
    Transition(label='Calibrate Climate'),
    Transition(label='Configure Lighting'),
    Transition(label='Integrate IoT'),
    Transition(label='Train Staff'),
    Transition(label='Run Trials'),
    Transition(label='Analyze Data'),
    Transition(label='Optimize Yield'),
    Transition(label='Check Compliance'),
    Transition(label='Plan Marketing'),
    Transition(label='Launch Facility')
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