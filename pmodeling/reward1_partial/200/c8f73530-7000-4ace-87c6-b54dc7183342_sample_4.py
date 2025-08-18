root = StrictPartialOrder(nodes=[
    Transition(label='Milk Sourcing'),
    Transition(label='Quality Testing'),
    Transition(label='Milk Pasteurize'),
    Transition(label='Culture Inoculate'),
    Transition(label='Coagulation'),
    Transition(label='Curd Cutting'),
    Transition(label='Whey Drain'),
    Transition(label='Pressing'),
    Transition(label='Salting'),
    Transition(label='Aging Control'),
    Transition(label='Sensory Audit'),
    Transition(label='Packaging Design'),
    Transition(label='Label Approval'),
    Transition(label='Order Customization'),
    Transition(label='Logistics Plan'),
    Transition(label='Market Delivery'),
    Transition(label='Customer Feedback'),
    Transition(label='Regulatory Check')
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
root.order.add_edge(root.nodes[16], root.nodes[17])
root.order.add_edge(root.nodes[17], root.nodes[18])
root.order.add_edge(root.nodes[18], root.nodes[19])