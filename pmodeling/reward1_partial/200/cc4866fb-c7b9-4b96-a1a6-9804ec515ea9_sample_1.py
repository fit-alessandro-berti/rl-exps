root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Design Planning'),
    Transition(label='Permit Filing'),
    Transition(label='Structural Reinforce'),
    Transition(label='Hydroponic Setup'),
    Transition(label='Sensor Install'),
    Transition(label='Energy Audit'),
    Transition(label='Crop Selection'),
    Transition(label='Nutrient Mix'),
    Transition(label='Waste Process'),
    Transition(label='Climate Control'),
    Transition(label='Staff Training'),
    Transition(label='Market Study'),
    Transition(label='Community Meet'),
    Transition(label='Launch Trial'),
    Transition(label='Data Monitor')
])

root.order.add_edge(Transition(label='Site Survey'), Transition(label='Design Planning'))
root.order.add_edge(Transition(label='Design Planning'), Transition(label='Permit Filing'))
root.order.add_edge(Transition(label='Permit Filing'), Transition(label='Structural Reinforce'))
root.order.add_edge(Transition(label='Structural Reinforce'), Transition(label='Hydroponic Setup'))
root.order.add_edge(Transition(label='Hydroponic Setup'), Transition(label='Sensor Install'))
root.order.add_edge(Transition(label='Sensor Install'), Transition(label='Energy Audit'))
root.order.add_edge(Transition(label='Energy Audit'), Transition(label='Crop Selection'))
root.order.add_edge(Transition(label='Crop Selection'), Transition(label='Nutrient Mix'))
root.order.add_edge(Transition(label='Nutrient Mix'), Transition(label='Waste Process'))
root.order.add_edge(Transition(label='Waste Process'), Transition(label='Climate Control'))
root.order.add_edge(Transition(label='Climate Control'), Transition(label='Staff Training'))
root.order.add_edge(Transition(label='Staff Training'), Transition(label='Market Study'))
root.order.add_edge(Transition(label='Market Study'), Transition(label='Community Meet'))
root.order.add_edge(Transition(label='Community Meet'), Transition(label='Launch Trial'))
root.order.add_edge(Transition(label='Launch Trial'), Transition(label='Data Monitor'))