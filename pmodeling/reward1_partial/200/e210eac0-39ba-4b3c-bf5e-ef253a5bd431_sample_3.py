root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Regulation Check'),
    Transition(label='Modular Design'),
    Transition(label='Material Sourcing'),
    Transition(label='Energy Integration'),
    Transition(label='Climate Setup'),
    Transition(label='Nutrient Mix'),
    Transition(label='System Assembly'),
    Transition(label='Automation Config'),
    Transition(label='Crop Seeding'),
    Transition(label='Growth Monitoring'),
    Transition(label='Waste Handling'),
    Transition(label='Community Meet'),
    Transition(label='Data Analysis'),
    Transition(label='Feedback Loop'),
    Transition(label='Yield Forecast')
])
root.order.add_edge(Transition(label='Site Survey'), Transition(label='Regulation Check'))
root.order.add_edge(Transition(label='Regulation Check'), Transition(label='Modular Design'))
root.order.add_edge(Transition(label='Modular Design'), Transition(label='Material Sourcing'))
root.order.add_edge(Transition(label='Material Sourcing'), Transition(label='Energy Integration'))
root.order.add_edge(Transition(label='Energy Integration'), Transition(label='Climate Setup'))
root.order.add_edge(Transition(label='Climate Setup'), Transition(label='Nutrient Mix'))
root.order.add_edge(Transition(label='Nutrient Mix'), Transition(label='System Assembly'))
root.order.add_edge(Transition(label='System Assembly'), Transition(label='Automation Config'))
root.order.add_edge(Transition(label='Automation Config'), Transition(label='Crop Seeding'))
root.order.add_edge(Transition(label='Crop Seeding'), Transition(label='Growth Monitoring'))
root.order.add_edge(Transition(label='Growth Monitoring'), Transition(label='Waste Handling'))
root.order.add_edge(Transition(label='Waste Handling'), Transition(label='Community Meet'))
root.order.add_edge(Transition(label='Community Meet'), Transition(label='Data Analysis'))
root.order.add_edge(Transition(label='Data Analysis'), Transition(label='Feedback Loop'))
root.order.add_edge(Transition(label='Feedback Loop'), Transition(label='Yield Forecast'))