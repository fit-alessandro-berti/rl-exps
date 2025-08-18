root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Structure Check'),
    Transition(label='Hydroponic Install'),
    Transition(label='Lighting Setup'),
    Transition(label='Climate Control'),
    Transition(label='Seed Selection'),
    Transition(label='Nutrient Mix'),
    Transition(label='Water Recycling'),
    Transition(label='Sensor Deploy'),
    Transition(label='Pest Control'),
    Transition(label='Growth Monitor'),
    Transition(label='Harvest Plan'),
    Transition(label='Packaging Prep'),
    Transition(label='Delivery Route'),
    Transition(label='Data Analysis'),
    Transition(label='Yield Forecast')
])

root.order.add_edge(Transition(label='Site Survey'), Transition(label='Structure Check'))
root.order.add_edge(Transition(label='Structure Check'), Transition(label='Hydroponic Install'))
root.order.add_edge(Transition(label='Hydroponic Install'), Transition(label='Lighting Setup'))
root.order.add_edge(Transition(label='Lighting Setup'), Transition(label='Climate Control'))
root.order.add_edge(Transition(label='Climate Control'), Transition(label='Seed Selection'))
root.order.add_edge(Transition(label='Seed Selection'), Transition(label='Nutrient Mix'))
root.order.add_edge(Transition(label='Nutrient Mix'), Transition(label='Water Recycling'))
root.order.add_edge(Transition(label='Water Recycling'), Transition(label='Sensor Deploy'))
root.order.add_edge(Transition(label='Sensor Deploy'), Transition(label='Pest Control'))
root.order.add_edge(Transition(label='Pest Control'), Transition(label='Growth Monitor'))
root.order.add_edge(Transition(label='Growth Monitor'), Transition(label='Harvest Plan'))
root.order.add_edge(Transition(label='Harvest Plan'), Transition(label='Packaging Prep'))
root.order.add_edge(Transition(label='Packaging Prep'), Transition(label='Delivery Route'))
root.order.add_edge(Transition(label='Delivery Route'), Transition(label='Data Analysis'))
root.order.add_edge(Transition(label='Data Analysis'), Transition(label='Yield Forecast'))