root = StrictPartialOrder(nodes=[
    Transition(label='Seed Select'),
    Transition(label='Nutrient Mix'),
    Transition(label='Climate Setup'),
    Transition(label='Light Adjust'),
    Transition(label='CO2 Control'),
    Transition(label='Humidity Tune'),
    Transition(label='Growth Monitor'),
    Transition(label='Pest Detect'),
    Transition(label='Harvest Plan'),
    Transition(label='Produce Sort'),
    Transition(label='Pack Biodeg'),
    Transition(label='Drone Dispatch'),
    Transition(label='Waste Recycle'),
    Transition(label='Compost Create'),
    Transition(label='Cycle Review')
])

root.order.add_edge(Transition(label='Seed Select'), Transition(label='Nutrient Mix'))
root.order.add_edge(Transition(label='Nutrient Mix'), Transition(label='Climate Setup'))
root.order.add_edge(Transition(label='Climate Setup'), Transition(label='Light Adjust'))
root.order.add_edge(Transition(label='Light Adjust'), Transition(label='CO2 Control'))
root.order.add_edge(Transition(label='CO2 Control'), Transition(label='Humidity Tune'))
root.order.add_edge(Transition(label='Humidity Tune'), Transition(label='Growth Monitor'))
root.order.add_edge(Transition(label='Growth Monitor'), Transition(label='Pest Detect'))
root.order.add_edge(Transition(label='Pest Detect'), Transition(label='Harvest Plan'))
root.order.add_edge(Transition(label='Harvest Plan'), Transition(label='Produce Sort'))
root.order.add_edge(Transition(label='Produce Sort'), Transition(label='Pack Biodeg'))
root.order.add_edge(Transition(label='Pack Biodeg'), Transition(label='Drone Dispatch'))
root.order.add_edge(Transition(label='Drone Dispatch'), Transition(label='Waste Recycle'))
root.order.add_edge(Transition(label='Waste Recycle'), Transition(label='Compost Create'))
root.order.add_edge(Transition(label='Compost Create'), Transition(label='Cycle Review'))