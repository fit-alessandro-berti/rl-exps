root = StrictPartialOrder(nodes=[
    Transition(label='Milk Sourcing'),
    Transition(label='Farm Selection'),
    Transition(label='Quality Testing'),
    Transition(label='Milk Pasteurize'),
    Transition(label='Starter Culture'),
    Transition(label='Coagulation'),
    Transition(label='Curd Cutting'),
    Transition(label='Whey Draining'),
    Transition(label='Mold Inoculate'),
    Transition(label='Aging Control'),
    Transition(label='Flavor Tasting'),
    Transition(label='Packaging Design'),
    Transition(label='Label Approval'),
    Transition(label='Inventory Audit'),
    Transition(label='Order Fulfill'),
    Transition(label='Retail Shipping')
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