root = StrictPartialOrder(nodes=[
    Transition('Site Survey'),
    Transition('Design Layout'),
    Transition('Material Sourcing'),
    Transition('Unit Assembly'),
    Transition('System Wiring'),
    Transition('Sensor Install'),
    Transition('Water Testing'),
    Transition('Nutrient Mix'),
    Transition('Seed Selection'),
    Transition('Planting Setup'),
    Transition('Climate Control'),
    Transition('Pest Management'),
    Transition('Data Calibration'),
    Transition('Yield Analysis'),
    Transition('Community Meet'),
    Transition('Compliance Check'),
    Transition('Expansion Plan')
])

root.order.add_edge(Transition('Site Survey'), Transition('Design Layout'))
root.order.add_edge(Transition('Design Layout'), Transition('Material Sourcing'))
root.order.add_edge(Transition('Material Sourcing'), Transition('Unit Assembly'))
root.order.add_edge(Transition('Unit Assembly'), Transition('System Wiring'))
root.order.add_edge(Transition('System Wiring'), Transition('Sensor Install'))
root.order.add_edge(Transition('Sensor Install'), Transition('Water Testing'))
root.order.add_edge(Transition('Water Testing'), Transition('Nutrient Mix'))
root.order.add_edge(Transition('Nutrient Mix'), Transition('Seed Selection'))
root.order.add_edge(Transition('Seed Selection'), Transition('Planting Setup'))
root.order.add_edge(Transition('Planting Setup'), Transition('Climate Control'))
root.order.add_edge(Transition('Climate Control'), Transition('Pest Management'))
root.order.add_edge(Transition('Pest Management'), Transition('Data Calibration'))
root.order.add_edge(Transition('Data Calibration'), Transition('Yield Analysis'))
root.order.add_edge(Transition('Yield Analysis'), Transition('Community Meet'))
root.order.add_edge(Transition('Community Meet'), Transition('Compliance Check'))
root.order.add_edge(Transition('Compliance Check'), Transition('Expansion Plan'))