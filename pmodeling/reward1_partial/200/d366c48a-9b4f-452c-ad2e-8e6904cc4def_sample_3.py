root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Climate Scan'),
    Transition(label='Module Setup'),
    Transition(label='Crop Choice'),
    Transition(label='Nutrient Feed'),
    Transition(label='Pest Control'),
    Transition(label='Energy Audit'),
    Transition(label='Waste Cycle'),
    Transition(label='Growth Track'),
    Transition(label='Demand Plan'),
    Transition(label='Community Link'),
    Transition(label='Regulation Check'),
    Transition(label='Supply Sync'),
    Transition(label='System Upgrade'),
    Transition(label='Data Backup')
])

root.order.add_edge(root.nodes[0], root.nodes[1])
root.order.add_edge(root.nodes[0], root.nodes[2])
root.order.add_edge(root.nodes[1], root.nodes[3])
root.order.add_edge(root.nodes[2], root.nodes[3])
root.order.add_edge(root.nodes[3], root.nodes[4])
root.order.add_edge(root.nodes[3], root.nodes[5])
root.order.add_edge(root.nodes[4], root.nodes[6])
root.order.add_edge(root.nodes[4], root.nodes[7])
root.order.add_edge(root.nodes[5], root.nodes[8])
root.order.add_edge(root.nodes[6], root.nodes[9])
root.order.add_edge(root.nodes[7], root.nodes[9])
root.order.add_edge(root.nodes[8], root.nodes[9])
root.order.add_edge(root.nodes[9], root.nodes[10])
root.order.add_edge(root.nodes[9], root.nodes[11])
root.order.add_edge(root.nodes[10], root.nodes[12])
root.order.add_edge(root.nodes[11], root.nodes[12])
root.order.add_edge(root.nodes[12], root.nodes[13])
root.order.add_edge(root.nodes[13], root.nodes[14])
root.order.add_edge(root.nodes[14], root.nodes[15])