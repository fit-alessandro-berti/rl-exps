root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Load Testing'),
    Transition(label='Crop Selection'),
    Transition(label='Soil Prep'),
    Transition(label='Irrigation Setup'),
    Transition(label='Permits Acquire'),
    Transition(label='Supplier Outreach'),
    Transition(label='Planting Seedlings'),
    Transition(label='Pest Monitoring'),
    Transition(label='Nutrient Testing'),
    Transition(label='Waste Sorting'),
    Transition(label='Staff Training'),
    Transition(label='Community Meet'),
    Transition(label='Harvest Planning'),
    Transition(label='Market Launch'),
    Transition(label='Yield Tracking')
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