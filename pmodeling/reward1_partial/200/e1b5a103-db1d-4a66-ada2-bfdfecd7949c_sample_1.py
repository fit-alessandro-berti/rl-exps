root = StrictPartialOrder(nodes=[
    Transition(label='Site Analysis'),
    Transition(label='Structure Check'),
    Transition(label='Climate Setup'),
    Transition(label='Hydroponics Install'),
    Transition(label='Nutrient Mix'),
    Transition(label='Seed Select'),
    Transition(label='Light Schedule'),
    Transition(label='Irrigation Plan'),
    Transition(label='Health Monitor'),
    Transition(label='Pest Control'),
    Transition(label='Robotic Harvest'),
    Transition(label='Clean Packaging'),
    Transition(label='Distribution Plan'),
    Transition(label='Data Collection'),
    Transition(label='Cycle Feedback')
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