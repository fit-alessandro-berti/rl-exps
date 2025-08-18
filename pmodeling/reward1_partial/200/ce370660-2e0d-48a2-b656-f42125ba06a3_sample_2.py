root = StrictPartialOrder(nodes=[
    Transition(label='Structural Check'),
    Transition(label='Permit Apply'),
    Transition(label='Design Layout'),
    Transition(label='Soil Prep'),
    Transition(label='Bed Install'),
    Transition(label='Irrigation Setup'),
    Transition(label='Sensor Mount'),
    Transition(label='Solar Connect'),
    Transition(label='Seed Order'),
    Transition(label='Nutrient Mix'),
    Transition(label='Community Meet'),
    Transition(label='Staff Train'),
    Transition(label='Plant Crop'),
    Transition(label='Maintenance Plan'),
    Transition(label='Harvest Schedule'),
    Transition(label='Waste Manage')
])

root.order.add_edge(Transition(label='Structural Check'), Transition(label='Permit Apply'))
root.order.add_edge(Transition(label='Permit Apply'), Transition(label='Design Layout'))
root.order.add_edge(Transition(label='Design Layout'), Transition(label='Soil Prep'))
root.order.add_edge(Transition(label='Soil Prep'), Transition(label='Bed Install'))
root.order.add_edge(Transition(label='Bed Install'), Transition(label='Irrigation Setup'))
root.order.add_edge(Transition(label='Irrigation Setup'), Transition(label='Sensor Mount'))
root.order.add_edge(Transition(label='Sensor Mount'), Transition(label='Solar Connect'))
root.order.add_edge(Transition(label='Solar Connect'), Transition(label='Seed Order'))
root.order.add_edge(Transition(label='Seed Order'), Transition(label='Nutrient Mix'))
root.order.add_edge(Transition(label='Nutrient Mix'), Transition(label='Community Meet'))
root.order.add_edge(Transition(label='Community Meet'), Transition(label='Staff Train'))
root.order.add_edge(Transition(label='Staff Train'), Transition(label='Plant Crop'))
root.order.add_edge(Transition(label='Plant Crop'), Transition(label='Maintenance Plan'))
root.order.add_edge(Transition(label='Maintenance Plan'), Transition(label='Harvest Schedule'))
root.order.add_edge(Transition(label='Harvest Schedule'), Transition(label='Waste Manage'))