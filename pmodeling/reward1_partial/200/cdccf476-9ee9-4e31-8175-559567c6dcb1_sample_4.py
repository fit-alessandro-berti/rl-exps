root = StrictPartialOrder(nodes=[
    Transition(label='Milk Sourcing'),
    Transition(label='Curd Formation'),
    Transition(label='Microbial Test'),
    Transition(label='Whey Removal'),
    Transition(label='Pressing Cheese'),
    Transition(label='Salt Application'),
    Transition(label='Aging Control'),
    Transition(label='Quality Check'),
    Transition(label='Eco Packaging'),
    Transition(label='Inventory Log'),
    Transition(label='Temp Monitoring'),
    Transition(label='Carrier Booking'),
    Transition(label='Trace Recording'),
    Transition(label='Feedback Review'),
    Transition(label='Compliance Audit'),
    Transition(label='Batch Adjustment')
])

# Define the order of activities
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