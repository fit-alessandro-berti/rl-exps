root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Permit Filing'),
    Transition(label='Structure Prep'),
    Transition(label='System Install'),
    Transition(label='Nutrient Mix'),
    Transition(label='Sensor Setup'),
    Transition(label='AI Calibration'),
    Transition(label='Seed Sourcing'),
    Transition(label='Staff Training'),
    Transition(label='Energy Connect'),
    Transition(label='Water Cycle'),
    Transition(label='Growth Monitor'),
    Transition(label='Waste Audit'),
    Transition(label='Community Meet'),
    Transition(label='Data Review'),
    Transition(label='Yield Forecast')
])

root.order.add_edge(Transition(label='Site Survey'), Transition(label='Permit Filing'))
root.order.add_edge(Transition(label='Permit Filing'), Transition(label='Structure Prep'))
root.order.add_edge(Transition(label='Structure Prep'), Transition(label='System Install'))
root.order.add_edge(Transition(label='System Install'), Transition(label='Nutrient Mix'))
root.order.add_edge(Transition(label='Nutrient Mix'), Transition(label='Sensor Setup'))
root.order.add_edge(Transition(label='Sensor Setup'), Transition(label='AI Calibration'))
root.order.add_edge(Transition(label='AI Calibration'), Transition(label='Seed Sourcing'))
root.order.add_edge(Transition(label='Seed Sourcing'), Transition(label='Staff Training'))
root.order.add_edge(Transition(label='Staff Training'), Transition(label='Energy Connect'))
root.order.add_edge(Transition(label='Energy Connect'), Transition(label='Water Cycle'))
root.order.add_edge(Transition(label='Water Cycle'), Transition(label='Growth Monitor'))
root.order.add_edge(Transition(label='Growth Monitor'), Transition(label='Waste Audit'))
root.order.add_edge(Transition(label='Waste Audit'), Transition(label='Community Meet'))
root.order.add_edge(Transition(label='Community Meet'), Transition(label='Data Review'))
root.order.add_edge(Transition(label='Data Review'), Transition(label='Yield Forecast'))