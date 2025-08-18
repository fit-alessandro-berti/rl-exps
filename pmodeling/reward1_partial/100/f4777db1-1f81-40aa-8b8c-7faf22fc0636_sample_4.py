root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Impact Study'),
    Transition(label='Structure Check'),
    Transition(label='Soil Testing'),
    Transition(label='System Design'),
    Transition(label='Seed Selection'),
    Transition(label='Irrigation Setup'),
    Transition(label='Lighting Install'),
    Transition(label='Pest Control'),
    Transition(label='Community Meet'),
    Transition(label='Regulation Review'),
    Transition(label='Waste Plan'),
    Transition(label='Crop Monitor'),
    Transition(label='Harvest Prep'),
    Transition(label='Market Launch')
])

root.order.add_edge(Transition(label='Site Survey'), Transition(label='Impact Study'))
root.order.add_edge(Transition(label='Impact Study'), Transition(label='Structure Check'))
root.order.add_edge(Transition(label='Structure Check'), Transition(label='Soil Testing'))
root.order.add_edge(Transition(label='Soil Testing'), Transition(label='System Design'))
root.order.add_edge(Transition(label='System Design'), Transition(label='Seed Selection'))
root.order.add_edge(Transition(label='Seed Selection'), Transition(label='Irrigation Setup'))
root.order.add_edge(Transition(label='Irrigation Setup'), Transition(label='Lighting Install'))
root.order.add_edge(Transition(label='Lighting Install'), Transition(label='Pest Control'))
root.order.add_edge(Transition(label='Pest Control'), Transition(label='Community Meet'))
root.order.add_edge(Transition(label='Community Meet'), Transition(label='Regulation Review'))
root.order.add_edge(Transition(label='Regulation Review'), Transition(label='Waste Plan'))
root.order.add_edge(Transition(label='Waste Plan'), Transition(label='Crop Monitor'))
root.order.add_edge(Transition(label='Crop Monitor'), Transition(label='Harvest Prep'))
root.order.add_edge(Transition(label='Harvest Prep'), Transition(label='Market Launch'))