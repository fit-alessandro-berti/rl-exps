root = StrictPartialOrder(nodes=[
    Transition(label='Site Analysis'),
    Transition(label='Climate Setup'),
    Transition(label='Nutrient Mix'),
    Transition(label='Seed Germinate'),
    Transition(label='Auto Planting'),
    Transition(label='Irrigation Setup'),
    Transition(label='IoT Monitoring'),
    Transition(label='Pest Detection'),
    Transition(label='Drone Pollinate'),
    Transition(label='Pesticide Spray'),
    Transition(label='Robotic Harvest'),
    Transition(label='Quality Check'),
    Transition(label='Package Product'),
    Transition(label='Waste Recycle'),
    Transition(label='Energy Optimize'),
    Transition(label='Data Logging')
])

# Define the dependencies between activities
root.order.add_edge(Transition(label='Site Analysis'), Transition(label='Climate Setup'))
root.order.add_edge(Transition(label='Climate Setup'), Transition(label='Nutrient Mix'))
root.order.add_edge(Transition(label='Nutrient Mix'), Transition(label='Seed Germinate'))
root.order.add_edge(Transition(label='Seed Germinate'), Transition(label='Auto Planting'))
root.order.add_edge(Transition(label='Auto Planting'), Transition(label='Irrigation Setup'))
root.order.add_edge(Transition(label='Irrigation Setup'), Transition(label='IoT Monitoring'))
root.order.add_edge(Transition(label='IoT Monitoring'), Transition(label='Pest Detection'))
root.order.add_edge(Transition(label='Pest Detection'), Transition(label='Drone Pollinate'))
root.order.add_edge(Transition(label='Drone Pollinate'), Transition(label='Pesticide Spray'))
root.order.add_edge(Transition(label='Pesticide Spray'), Transition(label='Robotic Harvest'))
root.order.add_edge(Transition(label='Robotic Harvest'), Transition(label='Quality Check'))
root.order.add_edge(Transition(label='Quality Check'), Transition(label='Package Product'))
root.order.add_edge(Transition(label='Package Product'), Transition(label='Waste Recycle'))
root.order.add_edge(Transition(label='Waste Recycle'), Transition(label='Energy Optimize'))
root.order.add_edge(Transition(label='Energy Optimize'), Transition(label='Data Logging'))