root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Modular Design'),
    Transition(label='System Build'),
    Transition(label='Env Control'),
    Transition(label='Seed Selection'),
    Transition(label='Nutrient Mix'),
    Transition(label='Planting Setup'),
    Transition(label='Growth Monitor'),
    Transition(label='Pest Control'),
    Transition(label='Water Cycle'),
    Transition(label='Data Capture'),
    Transition(label='Yield Forecast'),
    Transition(label='Waste Reuse'),
    Transition(label='Stakeholder Meet'),
    Transition(label='Compliance Check'),
    Transition(label='Supply Sync')
])

root.order.add_edge(Transition(label='Site Survey'), Transition(label='Modular Design'))
root.order.add_edge(Transition(label='Modular Design'), Transition(label='System Build'))
root.order.add_edge(Transition(label='System Build'), Transition(label='Env Control'))
root.order.add_edge(Transition(label='Env Control'), Transition(label='Seed Selection'))
root.order.add_edge(Transition(label='Seed Selection'), Transition(label='Nutrient Mix'))
root.order.add_edge(Transition(label='Nutrient Mix'), Transition(label='Planting Setup'))
root.order.add_edge(Transition(label='Planting Setup'), Transition(label='Growth Monitor'))
root.order.add_edge(Transition(label='Growth Monitor'), Transition(label='Pest Control'))
root.order.add_edge(Transition(label='Pest Control'), Transition(label='Water Cycle'))
root.order.add_edge(Transition(label='Water Cycle'), Transition(label='Data Capture'))
root.order.add_edge(Transition(label='Data Capture'), Transition(label='Yield Forecast'))
root.order.add_edge(Transition(label='Yield Forecast'), Transition(label='Waste Reuse'))
root.order.add_edge(Transition(label='Waste Reuse'), Transition(label='Stakeholder Meet'))
root.order.add_edge(Transition(label='Stakeholder Meet'), Transition(label='Compliance Check'))
root.order.add_edge(Transition(label='Compliance Check'), Transition(label='Supply Sync'))