root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Design Modules'),
    Transition(label='Install Sensors'),
    Transition(label='Calibrate Climate'),
    Transition(label='Select Seeds'),
    Transition(label='Optimize Nutrients'),
    Transition(label='Deploy Robots'),
    Transition(label='Monitor Growth'),
    Transition(label='Detect Pests'),
    Transition(label='Analyze Data'),
    Transition(label='Harvest Crops'),
    Transition(label='Customize Pack'),
    Transition(label='Recycle Waste'),
    Transition(label='Audit Energy'),
    Transition(label='Align Demand')
])

# Define edges
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