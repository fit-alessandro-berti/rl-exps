root = StrictPartialOrder(nodes=[
    Transition(label='Client Brief'),
    Transition(label='Spec Analysis'),
    Transition(label='Material Sourcing'),
    Transition(label='Component Vetting'),
    Transition(label='Frame Assembly'),
    Transition(label='Sensor Install'),
    Transition(label='Propulsion Setup'),
    Transition(label='Calibration'),
    Transition(label='Software Load'),
    Transition(label='Flight Test'),
    Transition(label='AI Training'),
    Transition(label='QA Review'),
    Transition(label='Mission Pack'),
    Transition(label='Client Training'),
    Transition(label='Deployment Support')
])

root.order.add_edge(root.nodes[0], root.nodes[1])
root.order.add_edge(root.nodes[1], root.nodes[2])
root.order.add_edge(root.nodes[2], root.nodes[3])
root.order.add_edge(root.nodes[3], root.nodes[4])
root.order.add_edge(root.nodes[4], root.nodes[5])
root.order.add_edge(root.nodes[4], root.nodes[6])
root.order.add_edge(root.nodes[5], root.nodes[7])
root.order.add_edge(root.nodes[6], root.nodes[7])
root.order.add_edge(root.nodes[7], root.nodes[8])
root.order.add_edge(root.nodes[8], root.nodes[9])
root.order.add_edge(root.nodes[9], root.nodes[10])
root.order.add_edge(root.nodes[10], root.nodes[11])
root.order.add_edge(root.nodes[11], root.nodes[12])
root.order.add_edge(root.nodes[12], root.nodes[13])