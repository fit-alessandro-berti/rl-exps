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

root.order.add_edge(root.nodes[0], root.nodes[1])
root.order.add_edge(root.nodes[1], root.nodes[2])
root.order.add_edge(root.nodes[2], root.nodes[3])
root.order.add_edge(root.nodes[3], root.nodes[4])
root.order.add_edge(root.nodes[4], root.nodes[5])
root.order.add_edge(root.nodes[5], root.nodes[6])
root.order.add_edge(root.nodes[6], root.nodes[7])
root.order.add_edge(root.nodes[7], root.nodes[8])
root.order.add_edge(root.nodes[8], root.nodes[9])
root.order.add_edge(root.nodes[9], root.nodes[10])
root.order.add_edge(root.nodes[10], root.nodes[11])
root.order.add_edge(root.nodes[11], root.nodes[12])
root.order.add_edge(root.nodes[12], root.nodes[13])
root.order.add_edge(root.nodes[13], root.nodes[14])