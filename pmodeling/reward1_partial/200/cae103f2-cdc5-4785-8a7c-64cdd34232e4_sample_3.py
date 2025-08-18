root = StrictPartialOrder(nodes=[
    Transition(label='Site Acquisition'),
    Transition(label='Impact Assess'),
    Transition(label='Modular Setup'),
    Transition(label='Crop Planting'),
    Transition(label='Nutrient Control'),
    Transition(label='Pest Control'),
    Transition(label='Growth Monitor'),
    Transition(label='Community Engage'),
    Transition(label='Yield Forecast'),
    Transition(label='Supply Coordinate'),
    Transition(label='Compliance Check'),
    Transition(label='Waste Recycle'),
    Transition(label='Energy Optimize'),
    Transition(label='Market Strategy'),
    Transition(label='Performance Review')
])

# Define the dependencies (edges) between the activities
root.order.add_edge(Transition('Site Acquisition'), Transition('Impact Assess'))
root.order.add_edge(Transition('Impact Assess'), Transition('Modular Setup'))
root.order.add_edge(Transition('Modular Setup'), Transition('Crop Planting'))
root.order.add_edge(Transition('Crop Planting'), Transition('Nutrient Control'))
root.order.add_edge(Transition('Nutrient Control'), Transition('Pest Control'))
root.order.add_edge(Transition('Pest Control'), Transition('Growth Monitor'))
root.order.add_edge(Transition('Growth Monitor'), Transition('Community Engage'))
root.order.add_edge(Transition('Community Engage'), Transition('Yield Forecast'))
root.order.add_edge(Transition('Yield Forecast'), Transition('Supply Coordinate'))
root.order.add_edge(Transition('Supply Coordinate'), Transition('Compliance Check'))
root.order.add_edge(Transition('Compliance Check'), Transition('Waste Recycle'))
root.order.add_edge(Transition('Waste Recycle'), Transition('Energy Optimize'))
root.order.add_edge(Transition('Energy Optimize'), Transition('Market Strategy'))
root.order.add_edge(Transition('Market Strategy'), Transition('Performance Review'))