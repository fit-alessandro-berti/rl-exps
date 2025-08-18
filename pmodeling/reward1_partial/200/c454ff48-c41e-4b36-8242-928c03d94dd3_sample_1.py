root = StrictPartialOrder(nodes=[
    Transition(label='Site Assess'),
    Transition(label='Permit Obtain'),
    Transition(label='Soil Testing'),
    Transition(label='Crop Select'),
    Transition(label='Irrigation Setup'),
    Transition(label='Drainage Install'),
    Transition(label='Energy Integrate'),
    Transition(label='Staff Train'),
    Transition(label='Pest Control'),
    Transition(label='Logistics Plan'),
    Transition(label='Supply Coordinate'),
    Transition(label='Distribution Map'),
    Transition(label='Community Engage'),
    Transition(label='Monitoring Setup'),
    Transition(label='Yield Optimize')
])
root.order.add_edge(Transition(label='Site Assess'), Transition(label='Permit Obtain'))
root.order.add_edge(Transition(label='Permit Obtain'), Transition(label='Soil Testing'))
root.order.add_edge(Transition(label='Soil Testing'), Transition(label='Crop Select'))
root.order.add_edge(Transition(label='Crop Select'), Transition(label='Irrigation Setup'))
root.order.add_edge(Transition(label='Irrigation Setup'), Transition(label='Drainage Install'))
root.order.add_edge(Transition(label='Drainage Install'), Transition(label='Energy Integrate'))
root.order.add_edge(Transition(label='Energy Integrate'), Transition(label='Staff Train'))
root.order.add_edge(Transition(label='Staff Train'), Transition(label='Pest Control'))
root.order.add_edge(Transition(label='Pest Control'), Transition(label='Logistics Plan'))
root.order.add_edge(Transition(label='Logistics Plan'), Transition(label='Supply Coordinate'))
root.order.add_edge(Transition(label='Supply Coordinate'), Transition(label='Distribution Map'))
root.order.add_edge(Transition(label='Distribution Map'), Transition(label='Community Engage'))
root.order.add_edge(Transition(label='Community Engage'), Transition(label='Monitoring Setup'))
root.order.add_edge(Transition(label='Monitoring Setup'), Transition(label='Yield Optimize'))