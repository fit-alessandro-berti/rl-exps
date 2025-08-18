root = StrictPartialOrder(nodes=[
    Transition(label='Seed Selection'),
    Transition(label='Germination Start'),
    Transition(label='Nutrient Mix'),
    Transition(label='Climate Adjust'),
    Transition(label='Light Scheduling'),
    Transition(label='Pest Inspection'),
    Transition(label='Bio Control'),
    Transition(label='Growth Monitor'),
    Transition(label='Water Recirc'),
    Transition(label='Harvest Plan'),
    Transition(label='Yield Forecast'),
    Transition(label='Quality Check'),
    Transition(label='Packaging Prep'),
    Transition(label='Cold Storage'),
    Transition(label='Delivery Route'),
    Transition(label='Energy Audit'),
    Transition(label='Sustain Report')
])

root.order.add_edge(Transition('Seed Selection'), Transition('Germination Start'))
root.order.add_edge(Transition('Germination Start'), Transition('Nutrient Mix'))
root.order.add_edge(Transition('Nutrient Mix'), Transition('Climate Adjust'))
root.order.add_edge(Transition('Climate Adjust'), Transition('Light Scheduling'))
root.order.add_edge(Transition('Light Scheduling'), Transition('Pest Inspection'))
root.order.add_edge(Transition('Pest Inspection'), Transition('Bio Control'))
root.order.add_edge(Transition('Bio Control'), Transition('Growth Monitor'))
root.order.add_edge(Transition('Growth Monitor'), Transition('Water Recirc'))
root.order.add_edge(Transition('Water Recirc'), Transition('Harvest Plan'))
root.order.add_edge(Transition('Harvest Plan'), Transition('Yield Forecast'))
root.order.add_edge(Transition('Yield Forecast'), Transition('Quality Check'))
root.order.add_edge(Transition('Quality Check'), Transition('Packaging Prep'))
root.order.add_edge(Transition('Packaging Prep'), Transition('Cold Storage'))
root.order.add_edge(Transition('Cold Storage'), Transition('Delivery Route'))
root.order.add_edge(Transition('Delivery Route'), Transition('Energy Audit'))
root.order.add_edge(Transition('Energy Audit'), Transition('Sustain Report'))