root = StrictPartialOrder(nodes=[
    Transition(label='Site Assess'),
    Transition(label='Structure Check'),
    Transition(label='Soil Test'),
    Transition(label='Climate Eval'),
    Transition(label='Permit Obtain'),
    Transition(label='Design Layout'),
    Transition(label='Seed Sourcing'),
    Transition(label='Irrigation Set'),
    Transition(label='Nutrient Mix'),
    Transition(label='Pest Control'),
    Transition(label='Sensor Install'),
    Transition(label='Staff Train'),
    Transition(label='Crop Planting'),
    Transition(label='Yield Monitor'),
    Transition(label='Market Setup'),
    Transition(label='Maintenance'),
    Transition(label='Waste Manage')
])

# Define dependencies for the activities
root.order.add_edge(Transition(label='Site Assess'), Transition(label='Structure Check'))
root.order.add_edge(Transition(label='Site Assess'), Transition(label='Soil Test'))
root.order.add_edge(Transition(label='Site Assess'), Transition(label='Climate Eval'))
root.order.add_edge(Transition(label='Site Assess'), Transition(label='Permit Obtain'))

root.order.add_edge(Transition(label='Structure Check'), Transition(label='Design Layout'))

root.order.add_edge(Transition(label='Soil Test'), Transition(label='Design Layout'))
root.order.add_edge(Transition(label='Climate Eval'), Transition(label='Design Layout'))

root.order.add_edge(Transition(label='Permit Obtain'), Transition(label='Design Layout'))

root.order.add_edge(Transition(label='Design Layout'), Transition(label='Seed Sourcing'))
root.order.add_edge(Transition(label='Design Layout'), Transition(label='Irrigation Set'))
root.order.add_edge(Transition(label='Design Layout'), Transition(label='Nutrient Mix'))
root.order.add_edge(Transition(label='Design Layout'), Transition(label='Pest Control'))
root.order.add_edge(Transition(label='Design Layout'), Transition(label='Sensor Install'))

root.order.add_edge(Transition(label='Seed Sourcing'), Transition(label='Staff Train'))
root.order.add_edge(Transition(label='Irrigation Set'), Transition(label='Staff Train'))
root.order.add_edge(Transition(label='Nutrient Mix'), Transition(label='Staff Train'))
root.order.add_edge(Transition(label='Pest Control'), Transition(label='Staff Train'))
root.order.add_edge(Transition(label='Sensor Install'), Transition(label='Staff Train'))

root.order.add_edge(Transition(label='Staff Train'), Transition(label='Crop Planting'))

root.order.add_edge(Transition(label='Crop Planting'), Transition(label='Yield Monitor'))

root.order.add_edge(Transition(label='Yield Monitor'), Transition(label='Market Setup'))

root.order.add_edge(Transition(label='Market Setup'), Transition(label='Maintenance'))

root.order.add_edge(Transition(label='Maintenance'), Transition(label='Waste Manage'))