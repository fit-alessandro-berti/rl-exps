root = StrictPartialOrder(nodes=[
    Transition(label='User Signup'),
    Transition(label='Preference Set'),
    Transition(label='Meal Select'),
    Transition(label='Schedule Delivery'),
    Transition(label='Supplier Match'),
    Transition(label='Inventory Check'),
    Transition(label='Ingredient Order'),
    Transition(label='Quality Inspect'),
    Transition(label='Meal Pack'),
    Transition(label='Route Plan'),
    Transition(label='Dispatch Kit'),
    Transition(label='Delivery Track'),
    Transition(label='Feedback Collect'),
    Transition(label='Data Analyze'),
    Transition(label='Plan Optimize')
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