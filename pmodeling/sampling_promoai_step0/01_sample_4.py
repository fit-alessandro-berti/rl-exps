root = StrictPartialOrder(nodes=[
    Transition(label='Receive customer inquiry'),
    Transition(label='Collect customer information'),
    Transition(label='Address customer concerns or questions'),
    Transition(label='Guide customer in selecting product/service'),
    Transition(label='Provide quote'),
    Transition(label='Place order'),
    Transition(label='Record order in system'),
    Transition(label='Send order confirmation to customer'),
    Transition(label='Skip')
])

root.order.add_edge(root.nodes[0], root.nodes[1])
root.order.add_edge(root.nodes[0], root.nodes[2])
root.order.add_edge(root.nodes[1], root.nodes[3])
root.order.add_edge(root.nodes[3], root.nodes[4])
root.order.add_edge(root.nodes[4], root.nodes[5])
root.order.add_edge(root.nodes[5], root.nodes[6])
root.order.add_edge(root.nodes[6], root.nodes[7])