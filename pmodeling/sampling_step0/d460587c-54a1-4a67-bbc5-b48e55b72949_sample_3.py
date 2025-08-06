root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Permit Filing'),
    Transition(label='Load Testing'),
    Transition(label='Soil Sampling'),
    Transition(label='Water Testing'),
    Transition(label='System Design'),
    Transition(label='Solar Setup'),
    Transition(label='Crop Planning'),
    Transition(label='Stakeholder Meet'),
    Transition(label='Material Order'),
    Transition(label='System Install'),
    Transition(label='Environmental Audit'),
    Transition(label='Growth Monitoring'),
    Transition(label='Pest Control'),
    Transition(label='Market Launch'),
])

root.order.add_edge(Transition(label='Site Survey'), Transition(label='Permit Filing'))
root.order.add_edge(Transition(label='Permit Filing'), Transition(label='Load Testing'))
root.order.add_edge(Transition(label='Load Testing'), Transition(label='Soil Sampling'))
root.order.add_edge(Transition(label='Soil Sampling'), Transition(label='Water Testing'))
root.order.add_edge(Transition(label='Water Testing'), Transition(label='System Design'))
root.order.add_edge(Transition(label='System Design'), Transition(label='Solar Setup'))
root.order.add_edge(Transition(label='Solar Setup'), Transition(label='Crop Planning'))
root.order.add_edge(Transition(label='Crop Planning'), Transition(label='Stakeholder Meet'))
root.order.add_edge(Transition(label='Stakeholder Meet'), Transition(label='Material Order'))
root.order.add_edge(Transition(label='Material Order'), Transition(label='System Install'))
root.order.add_edge(Transition(label='System Install'), Transition(label='Environmental Audit'))
root.order.add_edge(Transition(label='Environmental Audit'), Transition(label='Growth Monitoring'))
root.order.add_edge(Transition(label='Growth Monitoring'), Transition(label='Pest Control'))
root.order.add_edge(Transition(label='Pest Control'), Transition(label='Market Launch'))