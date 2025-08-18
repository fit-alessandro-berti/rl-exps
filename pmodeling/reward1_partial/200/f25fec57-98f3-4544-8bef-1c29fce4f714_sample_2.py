root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Permit Filing'),
    Transition(label='Structure Design'),
    Transition(label='System Install'),
    Transition(label='Hydroponic Setup'),
    Transition(label='Climate Config'),
    Transition(label='AI Integration'),
    Transition(label='Nutrient Sourcing'),
    Transition(label='Waste Planning'),
    Transition(label='Staff Training'),
    Transition(label='Crop Seeding'),
    Transition(label='Growth Monitoring'),
    Transition(label='Quality Testing'),
    Transition(label='Harvest Scheduling'),
    Transition(label='Distribution Plan'),
    Transition(label='Data Analysis')
])
root.order.add_edge(Transition(label='Site Survey'), Transition(label='Permit Filing'))
root.order.add_edge(Transition(label='Permit Filing'), Transition(label='Structure Design'))
root.order.add_edge(Transition(label='Structure Design'), Transition(label='System Install'))
root.order.add_edge(Transition(label='System Install'), Transition(label='Hydroponic Setup'))
root.order.add_edge(Transition(label='Hydroponic Setup'), Transition(label='Climate Config'))
root.order.add_edge(Transition(label='Climate Config'), Transition(label='AI Integration'))
root.order.add_edge(Transition(label='AI Integration'), Transition(label='Nutrient Sourcing'))
root.order.add_edge(Transition(label='Nutrient Sourcing'), Transition(label='Waste Planning'))
root.order.add_edge(Transition(label='Waste Planning'), Transition(label='Staff Training'))
root.order.add_edge(Transition(label='Staff Training'), Transition(label='Crop Seeding'))
root.order.add_edge(Transition(label='Crop Seeding'), Transition(label='Growth Monitoring'))
root.order.add_edge(Transition(label='Growth Monitoring'), Transition(label='Quality Testing'))
root.order.add_edge(Transition(label='Quality Testing'), Transition(label='Harvest Scheduling'))
root.order.add_edge(Transition(label='Harvest Scheduling'), Transition(label='Distribution Plan'))
root.order.add_edge(Transition(label='Distribution Plan'), Transition(label='Data Analysis'))