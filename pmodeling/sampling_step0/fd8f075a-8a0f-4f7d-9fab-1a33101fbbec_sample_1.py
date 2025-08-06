root = StrictPartialOrder(nodes=[
    Transition('Site Survey'),
    Transition('Permit Filing'),
    Transition('Structure Prep'),
    Transition('System Install'),
    Transition('Nutrient Mix'),
    Transition('Sensor Setup'),
    Transition('AI Calibration'),
    Transition('Seed Sourcing'),
    Transition('Staff Training'),
    Transition('Energy Connect'),
    Transition('Water Cycle'),
    Transition('Growth Monitor'),
    Transition('Waste Audit'),
    Transition('Community Meet'),
    Transition('Data Review'),
    Transition('Yield Forecast'),
])
root.order.add_edge(Transition('Site Survey'), Transition('Permit Filing'))
root.order.add_edge(Transition('Permit Filing'), Transition('Structure Prep'))
root.order.add_edge(Transition('Structure Prep'), Transition('System Install'))
root.order.add_edge(Transition('System Install'), Transition('Nutrient Mix'))
root.order.add_edge(Transition('Nutrient Mix'), Transition('Sensor Setup'))
root.order.add_edge(Transition('Sensor Setup'), Transition('AI Calibration'))
root.order.add_edge(Transition('AI Calibration'), Transition('Seed Sourcing'))
root.order.add_edge(Transition('Seed Sourcing'), Transition('Staff Training'))
root.order.add_edge(Transition('Staff Training'), Transition('Energy Connect'))
root.order.add_edge(Transition('Energy Connect'), Transition('Water Cycle'))
root.order.add_edge(Transition('Water Cycle'), Transition('Growth Monitor'))
root.order.add_edge(Transition('Growth Monitor'), Transition('Waste Audit'))
root.order.add_edge(Transition('Waste Audit'), Transition('Community Meet'))
root.order.add_edge(Transition('Community Meet'), Transition('Data Review'))
root.order.add_edge(Transition('Data Review'), Transition('Yield Forecast'))