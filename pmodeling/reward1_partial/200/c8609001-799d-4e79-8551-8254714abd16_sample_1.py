root = StrictPartialOrder(nodes=[
    Transition(label='Initial Review'),
    Transition(label='Provenance Check'),
    Transition(label='Material Test'),
    Transition(label='Expert Consult'),
    Transition(label='Database Search'),
    Transition(label='Condition Report'),
    Transition(label='Risk Assess'),
    Transition(label='Market Analysis'),
    Transition(label='Stakeholder Meet'),
    Transition(label='Legal Review'),
    Transition(label='Insurance Quote'),
    Transition(label='Price Negotiation'),
    Transition(label='Contract Draft'),
    Transition(label='Final Approval'),
    Transition(label='Asset Registration')
])

# Define edges based on the process description
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