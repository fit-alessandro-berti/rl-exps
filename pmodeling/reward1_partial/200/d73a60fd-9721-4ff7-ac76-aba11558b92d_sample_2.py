root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Structural Audit'),
    Transition(label='System Design'),
    Transition(label='Permit Filing'),
    Transition(label='Foundation Prep'),
    Transition(label='Frame Build'),
    Transition(label='Irrigation Setup'),
    Transition(label='Lighting Install'),
    Transition(label='Climate Control'),
    Transition(label='Nutrient Mix'),
    Transition(label='Crop Planting'),
    Transition(label='Pest Scouting'),
    Transition(label='Data Monitoring'),
    Transition(label='Waste Sorting'),
    Transition(label='Energy Audit'),
    Transition(label='Community Meet'),
    Transition(label='Yield Analysis')
])

root.order.add_edge(Transition(label='Site Survey'), Transition(label='Structural Audit'))
root.order.add_edge(Transition(label='Structural Audit'), Transition(label='System Design'))
root.order.add_edge(Transition(label='System Design'), Transition(label='Permit Filing'))
root.order.add_edge(Transition(label='Permit Filing'), Transition(label='Foundation Prep'))
root.order.add_edge(Transition(label='Foundation Prep'), Transition(label='Frame Build'))
root.order.add_edge(Transition(label='Frame Build'), Transition(label='Irrigation Setup'))
root.order.add_edge(Transition(label='Irrigation Setup'), Transition(label='Lighting Install'))
root.order.add_edge(Transition(label='Lighting Install'), Transition(label='Climate Control'))
root.order.add_edge(Transition(label='Climate Control'), Transition(label='Nutrient Mix'))
root.order.add_edge(Transition(label='Nutrient Mix'), Transition(label='Crop Planting'))
root.order.add_edge(Transition(label='Crop Planting'), Transition(label='Pest Scouting'))
root.order.add_edge(Transition(label='Pest Scouting'), Transition(label='Data Monitoring'))
root.order.add_edge(Transition(label='Data Monitoring'), Transition(label='Waste Sorting'))
root.order.add_edge(Transition(label='Waste Sorting'), Transition(label='Energy Audit'))
root.order.add_edge(Transition(label='Energy Audit'), Transition(label='Community Meet'))
root.order.add_edge(Transition(label='Community Meet'), Transition(label='Yield Analysis'))