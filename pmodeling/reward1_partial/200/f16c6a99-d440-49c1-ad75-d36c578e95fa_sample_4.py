root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Design Layout'),
    Transition(label='Sensor Deploy'),
    Transition(label='Crop Select'),
    Transition(label='System Install'),
    Transition(label='Energy Setup'),
    Transition(label='Water Cycle'),
    Transition(label='Pest Control'),
    Transition(label='Regulatory Check'),
    Transition(label='Staff Training'),
    Transition(label='Data Configure'),
    Transition(label='Supply Plan'),
    Transition(label='Harvest Schedule'),
    Transition(label='Quality Audit'),
    Transition(label='Market Launch'),
    Transition(label='Feedback Loop')
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