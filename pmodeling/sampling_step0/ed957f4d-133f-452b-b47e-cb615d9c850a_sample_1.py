root = StrictPartialOrder(nodes=[
    Transition(label='Source Materials'),
    Transition(label='Vet Suppliers'),
    Transition(label='Design Modules'),
    Transition(label='Prototype Build'),
    Transition(label='Test Durability'),
    Transition(label='Secure Permits'),
    Transition(label='Map Habitats'),
    Transition(label='Micro Warehouse'),
    Transition(label='Inventory Sync'),
    Transition(label='Pack Sustainably'),
    Transition(label='Route Optimize'),
    Transition(label='Engage Community'),
    Transition(label='Collect Feedback'),
    Transition(label='Adjust Production'),
    Transition(label='Partner NGOs'),
    Transition(label='Launch Campaign'),
    Transition(label='Monitor Sensors'),
    Transition(label='Report Impact'),
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