root = StrictPartialOrder(nodes=[
    Transition(label='Site Analysis'),
    Transition(label='Structural Check'),
    Transition(label='Rack Install'),
    Transition(label='System Setup'),
    Transition(label='Hydroponics Config'),
    Transition(label='Aeroponics Tune'),
    Transition(label='Lighting Setup'),
    Transition(label='Enviro Control'),
    Transition(label='Sensor Deploy'),
    Transition(label='Waste Recycle'),
    Transition(label='Water Reuse'),
    Transition(label='Staff Training'),
    Transition(label='Test Grow'),
    Transition(label='Data Analytics'),
    Transition(label='Yield Optimize')
])

root.order.add_edge(Transition(label='Site Analysis'), Transition(label='Structural Check'))
root.order.add_edge(Transition(label='Structural Check'), Transition(label='Rack Install'))
root.order.add_edge(Transition(label='Rack Install'), Transition(label='System Setup'))
root.order.add_edge(Transition(label='System Setup'), Transition(label='Hydroponics Config'))
root.order.add_edge(Transition(label='Hydroponics Config'), Transition(label='Aeroponics Tune'))
root.order.add_edge(Transition(label='Aeroponics Tune'), Transition(label='Lighting Setup'))
root.order.add_edge(Transition(label='Lighting Setup'), Transition(label='Enviro Control'))
root.order.add_edge(Transition(label='Enviro Control'), Transition(label='Sensor Deploy'))
root.order.add_edge(Transition(label='Sensor Deploy'), Transition(label='Waste Recycle'))
root.order.add_edge(Transition(label='Waste Recycle'), Transition(label='Water Reuse'))
root.order.add_edge(Transition(label='Water Reuse'), Transition(label='Staff Training'))
root.order.add_edge(Transition(label='Staff Training'), Transition(label='Test Grow'))
root.order.add_edge(Transition(label='Test Grow'), Transition(label='Data Analytics'))
root.order.add_edge(Transition(label='Data Analytics'), Transition(label='Yield Optimize'))