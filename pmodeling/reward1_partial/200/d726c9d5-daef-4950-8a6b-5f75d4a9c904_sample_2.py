root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Structure Check'),
    Transition(label='Soil Sample'),
    Transition(label='Water Test'),
    Transition(label='Crop Selection'),
    Transition(label='Material Order'),
    Transition(label='Planter Setup'),
    Transition(label='Irrigation Install'),
    Transition(label='Sensor Deploy'),
    Transition(label='Solar Setup'),
    Transition(label='Data Integration'),
    Transition(label='Community Meet'),
    Transition(label='Training Session'),
    Transition(label='Yield Monitor'),
    Transition(label='Adjust Plan')
])

root.order.add_edge(Transition(label='Site Survey'), Transition(label='Structure Check'))
root.order.add_edge(Transition(label='Structure Check'), Transition(label='Soil Sample'))
root.order.add_edge(Transition(label='Soil Sample'), Transition(label='Water Test'))
root.order.add_edge(Transition(label='Water Test'), Transition(label='Crop Selection'))
root.order.add_edge(Transition(label='Crop Selection'), Transition(label='Material Order'))
root.order.add_edge(Transition(label='Material Order'), Transition(label='Planter Setup'))
root.order.add_edge(Transition(label='Planter Setup'), Transition(label='Irrigation Install'))
root.order.add_edge(Transition(label='Irrigation Install'), Transition(label='Sensor Deploy'))
root.order.add_edge(Transition(label='Sensor Deploy'), Transition(label='Solar Setup'))
root.order.add_edge(Transition(label='Solar Setup'), Transition(label='Data Integration'))
root.order.add_edge(Transition(label='Data Integration'), Transition(label='Community Meet'))
root.order.add_edge(Transition(label='Community Meet'), Transition(label='Training Session'))
root.order.add_edge(Transition(label='Training Session'), Transition(label='Yield Monitor'))
root.order.add_edge(Transition(label='Yield Monitor'), Transition(label='Adjust Plan'))