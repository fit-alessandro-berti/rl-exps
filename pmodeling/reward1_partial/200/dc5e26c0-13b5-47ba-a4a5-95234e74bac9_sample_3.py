root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Design Layout'),
    Transition(label='Climate Setup'),
    Transition(label='Sensor Install'),
    Transition(label='Nutrient Mix'),
    Transition(label='Automation Code'),
    Transition(label='Crop Planning'),
    Transition(label='Pest Control'),
    Transition(label='Energy Audit'),
    Transition(label='Waste Sort'),
    Transition(label='Planting Tier'),
    Transition(label='Harvest Prep'),
    Transition(label='Logistics Plan'),
    Transition(label='Community Meet'),
    Transition(label='Data Review'),
    Transition(label='System Upgrade')
])

# Define dependencies
root.order.add_edge(Transition(label='Site Survey'), Transition(label='Design Layout'))
root.order.add_edge(Transition(label='Design Layout'), Transition(label='Climate Setup'))
root.order.add_edge(Transition(label='Climate Setup'), Transition(label='Sensor Install'))
root.order.add_edge(Transition(label='Sensor Install'), Transition(label='Nutrient Mix'))
root.order.add_edge(Transition(label='Nutrient Mix'), Transition(label='Automation Code'))
root.order.add_edge(Transition(label='Automation Code'), Transition(label='Crop Planning'))
root.order.add_edge(Transition(label='Crop Planning'), Transition(label='Pest Control'))
root.order.add_edge(Transition(label='Pest Control'), Transition(label='Energy Audit'))
root.order.add_edge(Transition(label='Energy Audit'), Transition(label='Waste Sort'))
root.order.add_edge(Transition(label='Waste Sort'), Transition(label='Planting Tier'))
root.order.add_edge(Transition(label='Planting Tier'), Transition(label='Harvest Prep'))
root.order.add_edge(Transition(label='Harvest Prep'), Transition(label='Logistics Plan'))
root.order.add_edge(Transition(label='Logistics Plan'), Transition(label='Community Meet'))
root.order.add_edge(Transition(label='Community Meet'), Transition(label='Data Review'))
root.order.add_edge(Transition(label='Data Review'), Transition(label='System Upgrade'))