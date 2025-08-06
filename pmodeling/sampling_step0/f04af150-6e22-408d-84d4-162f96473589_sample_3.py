root = StrictPartialOrder(nodes=[
    Transition(label='Material Sourcing'),
    Transition(label='Supplier Vetting'),
    Transition(label='Design Review'),
    Transition(label='Prototype Build'),
    Transition(label='Quality Audit'),
    Transition(label='Batch Scheduling'),
    Transition(label='Handcrafting'),
    Transition(label='Packaging Design'),
    Transition(label='Custom Labeling'),
    Transition(label='Sustainability Check'),
    Transition(label='Inventory Sync'),
    Transition(label='Market Analysis'),
    Transition(label='Order Aggregation'),
    Transition(label='Distribution Plan'),
    Transition(label='Customer Feedback'),
    OperatorPOWL(operator=Operator.XOR, children=[
        OperatorPOWL(operator=Operator.LOOP, children=[
            Transition(label='Material Sourcing'),
            Transition(label='Supplier Vetting'),
            Transition(label='Design Review'),
            Transition(label='Prototype Build'),
            Transition(label='Quality Audit'),
            Transition(label='Batch Scheduling'),
            Transition(label='Handcrafting'),
            Transition(label='Packaging Design'),
            Transition(label='Custom Labeling'),
            Transition(label='Sustainability Check'),
            Transition(label='Inventory Sync'),
            Transition(label='Market Analysis'),
            Transition(label='Order Aggregation'),
            Transition(label='Distribution Plan'),
            Transition(label='Customer Feedback')
        ])
    ])
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