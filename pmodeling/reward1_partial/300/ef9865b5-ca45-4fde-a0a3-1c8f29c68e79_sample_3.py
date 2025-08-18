root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Permit Review'),
    Transition(label='Design Layout'),
    Transition(label='Material Sourcing'),
    Transition(label='Irrigation Setup'),
    Transition(label='Sensor Install'),
    Transition(label='Structural Test'),
    Transition(label='Recruit Farmers'),
    Transition(label='Trial Planting'),
    Transition(label='Pest Control'),
    Transition(label='Soilless Prep'),
    Transition(label='System Calibrate'),
    Transition(label='Data Monitor'),
    Transition(label='Harvest Plan'),
    Transition(label='Community Outreach')
])
root.order.add_edge(Transition(label='Site Survey'), Transition(label='Permit Review'))
root.order.add_edge(Transition(label='Permit Review'), Transition(label='Design Layout'))
root.order.add_edge(Transition(label='Design Layout'), Transition(label='Material Sourcing'))
root.order.add_edge(Transition(label='Material Sourcing'), Transition(label='Irrigation Setup'))
root.order.add_edge(Transition(label='Irrigation Setup'), Transition(label='Sensor Install'))
root.order.add_edge(Transition(label='Sensor Install'), Transition(label='Structural Test'))
root.order.add_edge(Transition(label='Structural Test'), Transition(label='Recruit Farmers'))
root.order.add_edge(Transition(label='Recruit Farmers'), Transition(label='Trial Planting'))
root.order.add_edge(Transition(label='Trial Planting'), Transition(label='Pest Control'))
root.order.add_edge(Transition(label='Pest Control'), Transition(label='Soilless Prep'))
root.order.add_edge(Transition(label='Soilless Prep'), Transition(label='System Calibrate'))
root.order.add_edge(Transition(label='System Calibrate'), Transition(label='Data Monitor'))
root.order.add_edge(Transition(label='Data Monitor'), Transition(label='Harvest Plan'))
root.order.add_edge(Transition(label='Harvest Plan'), Transition(label='Community Outreach'))