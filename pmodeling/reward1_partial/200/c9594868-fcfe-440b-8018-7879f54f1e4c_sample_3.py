root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Load Test'),
    Transition(label='Permit Review'),
    Transition(label='Design Layout'),
    Transition(label='Material Sourcing'),
    Transition(label='Soil Prep'),
    Transition(label='Hydroponic Setup'),
    Transition(label='Community Meet'),
    Transition(label='Crop Select'),
    Transition(label='Sensor Install'),
    Transition(label='Water Testing'),
    Transition(label='Pest Control'),
    Transition(label='Growth Monitor'),
    Transition(label='Harvest Plan'),
    Transition(label='Market Launch'),
    Transition(label='Feedback Collect')
])

root.order.add_edge(Transition(label='Site Survey'), Transition(label='Load Test'))
root.order.add_edge(Transition(label='Load Test'), Transition(label='Permit Review'))
root.order.add_edge(Transition(label='Permit Review'), Transition(label='Design Layout'))
root.order.add_edge(Transition(label='Design Layout'), Transition(label='Material Sourcing'))
root.order.add_edge(Transition(label='Material Sourcing'), Transition(label='Soil Prep'))
root.order.add_edge(Transition(label='Soil Prep'), Transition(label='Hydroponic Setup'))
root.order.add_edge(Transition(label='Hydroponic Setup'), Transition(label='Community Meet'))
root.order.add_edge(Transition(label='Community Meet'), Transition(label='Crop Select'))
root.order.add_edge(Transition(label='Crop Select'), Transition(label='Sensor Install'))
root.order.add_edge(Transition(label='Sensor Install'), Transition(label='Water Testing'))
root.order.add_edge(Transition(label='Water Testing'), Transition(label='Pest Control'))
root.order.add_edge(Transition(label='Pest Control'), Transition(label='Growth Monitor'))
root.order.add_edge(Transition(label='Growth Monitor'), Transition(label='Harvest Plan'))
root.order.add_edge(Transition(label='Harvest Plan'), Transition(label='Market Launch'))
root.order.add_edge(Transition(label='Market Launch'), Transition(label='Feedback Collect'))