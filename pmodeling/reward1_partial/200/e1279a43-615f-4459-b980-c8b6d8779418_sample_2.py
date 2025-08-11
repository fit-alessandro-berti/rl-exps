root = StrictPartialOrder(nodes=[
    Transition(label='Site Analysis'),
    Transition(label='Infrastructure Setup'),
    Transition(label='Seed Selection'),
    Transition(label='Nutrient Mix'),
    Transition(label='Planting Cycle'),
    Transition(label='Climate Adjust'),
    Transition(label='Growth Monitor'),
    Transition(label='Pest Control'),
    Transition(label='Harvesting Mode'),
    Transition(label='Quality Check'),
    Transition(label='Packaging Phase'),
    Transition(label='Cold Storage'),
    Transition(label='Order Dispatch'),
    Transition(label='Waste Recycling'),
    Transition(label='System Maintain')
])

# Define edges for the loop
root.order.add_edge(Transition(label='Planting Cycle'), Transition(label='Climate Adjust'))
root.order.add_edge(Transition(label='Climate Adjust'), Transition(label='Growth Monitor'))
root.order.add_edge(Transition(label='Growth Monitor'), Transition(label='Pest Control'))
root.order.add_edge(Transition(label='Pest Control'), Transition(label='Harvesting Mode'))
root.order.add_edge(Transition(label='Harvesting Mode'), Transition(label='Quality Check'))
root.order.add_edge(Transition(label='Quality Check'), Transition(label='Packaging Phase'))
root.order.add_edge(Transition(label='Packaging Phase'), Transition(label='Cold Storage'))
root.order.add_edge(Transition(label='Cold Storage'), Transition(label='Order Dispatch'))
root.order.add_edge(Transition(label='Order Dispatch'), Transition(label='Waste Recycling'))
root.order.add_edge(Transition(label='Waste Recycling'), Transition(label='System Maintain'))