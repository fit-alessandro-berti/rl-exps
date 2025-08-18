root = StrictPartialOrder(nodes=[
    Transition(label='Site Analysis'),
    Transition(label='Permit Securing'),
    Transition(label='Unit Designing'),
    Transition(label='LED Sourcing'),
    Transition(label='Hydroponic Setup'),
    Transition(label='Staff Hiring'),
    Transition(label='Pilot Cultivation'),
    Transition(label='Data Integration'),
    Transition(label='Waste Recycling'),
    Transition(label='Local Distribution'),
    Transition(label='Subscription Setup'),
    Transition(label='IoT Deployment'),
    Transition(label='Sustainability Audit'),
    Transition(label='Market Testing'),
    Transition(label='Process Refinement')
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