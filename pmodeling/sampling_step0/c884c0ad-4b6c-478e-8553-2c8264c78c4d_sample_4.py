root = StrictPartialOrder(nodes=[
    Transition(label='Seed Sourcing'),
    Transition(label='Germination Check'),
    Transition(label='Nutrient Mix'),
    Transition(label='Automated Planting'),
    Transition(label='Climate Control'),
    Transition(label='Crop Scanning'),
    Transition(label='Pest Monitoring'),
    Transition(label='Growth Analysis'),
    Transition(label='Robotic Harvest'),
    Transition(label='Quality Sort'),
    Transition(label='Eco Packaging'),
    Transition(label='Blockchain Track'),
    Transition(label='Route Planning'),
    Transition(label='Feedback Collect'),
    Transition(label='Waste Recycling'),
    Transition(label='Data Analytics'),
    Transition(label='Demand Forecast'),
    Transition(label='Maintenance Alert')
])
root.order.add_edge(Transition('Seed Sourcing'), Transition('Germination Check'))
root.order.add_edge(Transition('Germination Check'), Transition('Nutrient Mix'))
root.order.add_edge(Transition('Nutrient Mix'), Transition('Automated Planting'))
root.order.add_edge(Transition('Automated Planting'), Transition('Climate Control'))
root.order.add_edge(Transition('Climate Control'), Transition('Crop Scanning'))
root.order.add_edge(Transition('Crop Scanning'), Transition('Pest Monitoring'))
root.order.add_edge(Transition('Pest Monitoring'), Transition('Growth Analysis'))
root.order.add_edge(Transition('Growth Analysis'), Transition('Robotic Harvest'))
root.order.add_edge(Transition('Robotic Harvest'), Transition('Quality Sort'))
root.order.add_edge(Transition('Quality Sort'), Transition('Eco Packaging'))
root.order.add_edge(Transition('Eco Packaging'), Transition('Blockchain Track'))
root.order.add_edge(Transition('Blockchain Track'), Transition('Route Planning'))
root.order.add_edge(Transition('Route Planning'), Transition('Feedback Collect'))
root.order.add_edge(Transition('Feedback Collect'), Transition('Waste Recycling'))
root.order.add_edge(Transition('Waste Recycling'), Transition('Data Analytics'))
root.order.add_edge(Transition('Data Analytics'), Transition('Demand Forecast'))
root.order.add_edge(Transition('Demand Forecast'), Transition('Maintenance Alert'))