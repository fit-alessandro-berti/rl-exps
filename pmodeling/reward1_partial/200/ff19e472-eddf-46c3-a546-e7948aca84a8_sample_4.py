root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Design Layout'),
    Transition(label='Install Modules'),
    Transition(label='Calibrate Climate'),
    Transition(label='Prepare Nutrients'),
    Transition(label='Select Seeds'),
    Transition(label='Start Germination'),
    Transition(label='Deploy Sensors'),
    Transition(label='Monitor Growth'),
    Transition(label='Manage Pests'),
    Transition(label='Schedule Harvest'),
    Transition(label='Process Waste'),
    Transition(label='Optimize Energy'),
    Transition(label='Conduct Training'),
    Transition(label='Update Records'),
    Transition(label='Review Performance')
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