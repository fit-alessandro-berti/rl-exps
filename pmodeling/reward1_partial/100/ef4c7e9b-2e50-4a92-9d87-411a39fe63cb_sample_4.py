root = StrictPartialOrder(nodes=[
    Transition(label='Seed Selection'),
    Transition(label='Nutrient Mix'),
    Transition(label='Environment Setup'),
    Transition(label='Pest Scan'),
    Transition(label='Light Control'),
    Transition(label='Growth Monitor'),
    Transition(label='Water Cycle'),
    Transition(label='Air Quality'),
    Transition(label='Robotic Harvest'),
    Transition(label='Quality Check'),
    Transition(label='Data Logging'),
    Transition(label='Packaging'),
    Transition(label='Waste Sort'),
    Transition(label='Energy Audit'),
    Transition(label='Retail Sync')
])

# Define the dependencies
root.order.add_edge(Transition(label='Seed Selection'), Transition(label='Nutrient Mix'))
root.order.add_edge(Transition(label='Nutrient Mix'), Transition(label='Environment Setup'))
root.order.add_edge(Transition(label='Environment Setup'), Transition(label='Pest Scan'))
root.order.add_edge(Transition(label='Pest Scan'), Transition(label='Light Control'))
root.order.add_edge(Transition(label='Light Control'), Transition(label='Growth Monitor'))
root.order.add_edge(Transition(label='Growth Monitor'), Transition(label='Water Cycle'))
root.order.add_edge(Transition(label='Water Cycle'), Transition(label='Air Quality'))
root.order.add_edge(Transition(label='Air Quality'), Transition(label='Robotic Harvest'))
root.order.add_edge(Transition(label='Robotic Harvest'), Transition(label='Quality Check'))
root.order.add_edge(Transition(label='Quality Check'), Transition(label='Data Logging'))
root.order.add_edge(Transition(label='Data Logging'), Transition(label='Packaging'))
root.order.add_edge(Transition(label='Packaging'), Transition(label='Waste Sort'))
root.order.add_edge(Transition(label='Waste Sort'), Transition(label='Energy Audit'))
root.order.add_edge(Transition(label='Energy Audit'), Transition(label='Retail Sync'))