root = StrictPartialOrder(nodes=[
    Transition(label='Site Analysis'),
    Transition(label='Impact Review'),
    Transition(label='Modular Design'),
    Transition(label='System Integration'),
    Transition(label='Climate Setup'),
    Transition(label='Nutrient Mix'),
    Transition(label='Light Config'),
    Transition(label='Staff Training'),
    Transition(label='Pest Monitor'),
    Transition(label='Drone Deploy'),
    Transition(label='Health Scan'),
    Transition(label='Data Logging'),
    Transition(label='Supply Sync'),
    Transition(label='Maintenance Plan'),
    Transition(label='Waste Manage')
])

# Define the partial order relationships
root.order.add_edge(Transition(label='Site Analysis'), Transition(label='Impact Review'))
root.order.add_edge(Transition(label='Impact Review'), Transition(label='Modular Design'))
root.order.add_edge(Transition(label='Modular Design'), Transition(label='System Integration'))
root.order.add_edge(Transition(label='System Integration'), Transition(label='Climate Setup'))
root.order.add_edge(Transition(label='Climate Setup'), Transition(label='Nutrient Mix'))
root.order.add_edge(Transition(label='Nutrient Mix'), Transition(label='Light Config'))
root.order.add_edge(Transition(label='Light Config'), Transition(label='Staff Training'))
root.order.add_edge(Transition(label='Staff Training'), Transition(label='Pest Monitor'))
root.order.add_edge(Transition(label='Pest Monitor'), Transition(label='Drone Deploy'))
root.order.add_edge(Transition(label='Drone Deploy'), Transition(label='Health Scan'))
root.order.add_edge(Transition(label='Health Scan'), Transition(label='Data Logging'))
root.order.add_edge(Transition(label='Data Logging'), Transition(label='Supply Sync'))
root.order.add_edge(Transition(label='Supply Sync'), Transition(label='Maintenance Plan'))
root.order.add_edge(Transition(label='Maintenance Plan'), Transition(label='Waste Manage'))