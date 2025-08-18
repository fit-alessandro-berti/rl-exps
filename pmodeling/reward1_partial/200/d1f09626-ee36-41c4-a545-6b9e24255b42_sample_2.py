root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Load Test'),
    Transition(label='Soil Sample'),
    Transition(label='Climate Check'),
    Transition(label='Crop Select'),
    Transition(label='Irrigation Plan'),
    Transition(label='Energy Setup'),
    Transition(label='Pest Control'),
    Transition(label='Permit Obtain'),
    Transition(label='Stakeholder Meet'),
    Transition(label='Bed Construction'),
    Transition(label='Seed Planting'),
    Transition(label='Water Schedule'),
    Transition(label='Growth Monitor'),
    Transition(label='Harvest Plan'),
    Transition(label='Waste Recycle'),
    Transition(label='Yield Report')
])
root.order.add_edge(Transition(label='Site Survey'), Transition(label='Load Test'))
root.order.add_edge(Transition(label='Load Test'), Transition(label='Soil Sample'))
root.order.add_edge(Transition(label='Soil Sample'), Transition(label='Climate Check'))
root.order.add_edge(Transition(label='Climate Check'), Transition(label='Crop Select'))
root.order.add_edge(Transition(label='Crop Select'), Transition(label='Irrigation Plan'))
root.order.add_edge(Transition(label='Irrigation Plan'), Transition(label='Energy Setup'))
root.order.add_edge(Transition(label='Energy Setup'), Transition(label='Pest Control'))
root.order.add_edge(Transition(label='Pest Control'), Transition(label='Permit Obtain'))
root.order.add_edge(Transition(label='Permit Obtain'), Transition(label='Stakeholder Meet'))
root.order.add_edge(Transition(label='Stakeholder Meet'), Transition(label='Bed Construction'))
root.order.add_edge(Transition(label='Bed Construction'), Transition(label='Seed Planting'))
root.order.add_edge(Transition(label='Seed Planting'), Transition(label='Water Schedule'))
root.order.add_edge(Transition(label='Water Schedule'), Transition(label='Growth Monitor'))
root.order.add_edge(Transition(label='Growth Monitor'), Transition(label='Harvest Plan'))
root.order.add_edge(Transition(label='Harvest Plan'), Transition(label='Waste Recycle'))
root.order.add_edge(Transition(label='Waste Recycle'), Transition(label='Yield Report'))