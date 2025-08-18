root = StrictPartialOrder(nodes=[
    Transition(label='Site Select'),
    Transition(label='Env Assess'),
    Transition(label='Design Modules'),
    Transition(label='Hydroponics Setup'),
    Transition(label='Software Dev'),
    Transition(label='Seed Choose'),
    Transition(label='LED Install'),
    Transition(label='Train Staff'),
    Transition(label='Compliance Check'),
    Transition(label='Engage Community'),
    Transition(label='Plant Crops'),
    Transition(label='Monitor Growth'),
    Transition(label='Optimize Yields'),
    Transition(label='Waste Manage'),
    Transition(label='Energy Audit'),
    Transition(label='Water Recycle')
])

# Define the partial order dependencies
root.order.add_edge(Transition(label='Site Select'), Transition(label='Env Assess'))
root.order.add_edge(Transition(label='Env Assess'), Transition(label='Design Modules'))
root.order.add_edge(Transition(label='Design Modules'), Transition(label='Hydroponics Setup'))
root.order.add_edge(Transition(label='Hydroponics Setup'), Transition(label='Software Dev'))
root.order.add_edge(Transition(label='Software Dev'), Transition(label='Seed Choose'))
root.order.add_edge(Transition(label='Seed Choose'), Transition(label='LED Install'))
root.order.add_edge(Transition(label='LED Install'), Transition(label='Train Staff'))
root.order.add_edge(Transition(label='Train Staff'), Transition(label='Compliance Check'))
root.order.add_edge(Transition(label='Compliance Check'), Transition(label='Engage Community'))
root.order.add_edge(Transition(label='Engage Community'), Transition(label='Plant Crops'))
root.order.add_edge(Transition(label='Plant Crops'), Transition(label='Monitor Growth'))
root.order.add_edge(Transition(label='Monitor Growth'), Transition(label='Optimize Yields'))
root.order.add_edge(Transition(label='Optimize Yields'), Transition(label='Waste Manage'))
root.order.add_edge(Transition(label='Waste Manage'), Transition(label='Energy Audit'))
root.order.add_edge(Transition(label='Energy Audit'), Transition(label='Water Recycle'))