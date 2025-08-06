root = StrictPartialOrder(nodes=[
    Transition('Site Survey'),
    Transition('Structure Check'),
    Transition('Soil Sample'),
    Transition('Water Test'),
    Transition('Crop Selection'),
    Transition('Material Order'),
    Transition('Planter Setup'),
    Transition('Irrigation Install'),
    Transition('Sensor Deploy'),
    Transition('Solar Setup'),
    Transition('Data Integration'),
    Transition('Community Meet'),
    Transition('Training Session'),
    Transition('Yield Monitor'),
    Transition('Adjust Plan')
])

root.order.add_edge(Transition('Site Survey'), Transition('Structure Check'))
root.order.add_edge(Transition('Structure Check'), Transition('Soil Sample'))
root.order.add_edge(Transition('Soil Sample'), Transition('Water Test'))
root.order.add_edge(Transition('Water Test'), Transition('Crop Selection'))
root.order.add_edge(Transition('Crop Selection'), Transition('Material Order'))
root.order.add_edge(Transition('Material Order'), Transition('Planter Setup'))
root.order.add_edge(Transition('Planter Setup'), Transition('Irrigation Install'))
root.order.add_edge(Transition('Irrigation Install'), Transition('Sensor Deploy'))
root.order.add_edge(Transition('Sensor Deploy'), Transition('Solar Setup'))
root.order.add_edge(Transition('Solar Setup'), Transition('Data Integration'))
root.order.add_edge(Transition('Data Integration'), Transition('Community Meet'))
root.order.add_edge(Transition('Community Meet'), Transition('Training Session'))
root.order.add_edge(Transition('Training Session'), Transition('Yield Monitor'))
root.order.add_edge(Transition('Yield Monitor'), Transition('Adjust Plan'))