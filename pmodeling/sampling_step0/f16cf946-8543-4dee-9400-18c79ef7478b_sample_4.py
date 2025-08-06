root = StrictPartialOrder(nodes=[
    Transition('Site Survey'),
    Transition('Climate Study'),
    Transition('System Design'),
    Transition('Seed Selection'),
    Transition('Unit Install'),
    Transition('Sensor Setup'),
    Transition('Nutrient Mix'),
    Transition('Energy Audit'),
    Transition('Pest Control'),
    Transition('Crop Plan'),
    Transition('Quality Check'),
    Transition('Yield Forecast'),
    Transition('Supply Sync'),
    Transition('Staff Train'),
    Transition('Data Review')
])
root.order.add_edge(Transition('Site Survey'), Transition('Climate Study'))
root.order.add_edge(Transition('Climate Study'), Transition('System Design'))
root.order.add_edge(Transition('System Design'), Transition('Seed Selection'))
root.order.add_edge(Transition('Seed Selection'), Transition('Unit Install'))
root.order.add_edge(Transition('Unit Install'), Transition('Sensor Setup'))
root.order.add_edge(Transition('Sensor Setup'), Transition('Nutrient Mix'))
root.order.add_edge(Transition('Nutrient Mix'), Transition('Energy Audit'))
root.order.add_edge(Transition('Energy Audit'), Transition('Pest Control'))
root.order.add_edge(Transition('Pest Control'), Transition('Crop Plan'))
root.order.add_edge(Transition('Crop Plan'), Transition('Quality Check'))
root.order.add_edge(Transition('Quality Check'), Transition('Yield Forecast'))
root.order.add_edge(Transition('Yield Forecast'), Transition('Supply Sync'))
root.order.add_edge(Transition('Supply Sync'), Transition('Staff Train'))
root.order.add_edge(Transition('Staff Train'), Transition('Data Review'))