root = StrictPartialOrder(nodes=[
    Transition(label='Site Assess'),
    Transition(label='Load Testing'),
    Transition(label='Climate Study'),
    Transition(label='Medium Prep'),
    Transition(label='Bed Install'),
    Transition(label='Irrigation Setup'),
    Transition(label='Crop Select'),
    Transition(label='Pest Control'),
    Transition(label='Community Meet'),
    Transition(label='Monitor Deploy'),
    Transition(label='Waste Cycle'),
    Transition(label='Yield Forecast'),
    Transition(label='Market Link'),
    Transition(label='Workshop Plan'),
    Transition(label='Tech Integrate')
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