root = StrictPartialOrder(nodes=[
    Transition(label='Seed Selection'),
    Transition(label='Nutrient Mix'),
    Transition(label='Planting Setup'),
    Transition(label='Climate Control'),
    Transition(label='Water Cycling'),
    Transition(label='Growth Monitoring'),
    Transition(label='Pest Detection'),
    Transition(label='Light Adjustment'),
    Transition(label='Data Analysis'),
    Transition(label='Harvest Planning'),
    Transition(label='Crop Harvest'),
    Transition(label='Yield Sorting'),
    Transition(label='Packaging Prep'),
    Transition(label='Distribution Plan'),
    Transition(label='Regulation Check'),
    Transition(label='Waste Recycling'),
    Transition(label='System Maintenance'),
])

root.order.add_edge(Transition(label='Seed Selection'), Transition(label='Nutrient Mix'))
root.order.add_edge(Transition(label='Seed Selection'), Transition(label='Planting Setup'))
root.order.add_edge(Transition(label='Nutrient Mix'), Transition(label='Climate Control'))
root.order.add_edge(Transition(label='Nutrient Mix'), Transition(label='Water Cycling'))
root.order.add_edge(Transition(label='Planting Setup'), Transition(label='Climate Control'))
root.order.add_edge(Transition(label='Planting Setup'), Transition(label='Water Cycling'))
root.order.add_edge(Transition(label='Climate Control'), Transition(label='Growth Monitoring'))
root.order.add_edge(Transition(label='Climate Control'), Transition(label='Pest Detection'))
root.order.add_edge(Transition(label='Climate Control'), Transition(label='Light Adjustment'))
root.order.add_edge(Transition(label='Growth Monitoring'), Transition(label='Data Analysis'))
root.order.add_edge(Transition(label='Data Analysis'), Transition(label='Harvest Planning'))
root.order.add_edge(Transition(label='Data Analysis'), Transition(label='Crop Harvest'))
root.order.add_edge(Transition(label='Data Analysis'), Transition(label='Yield Sorting'))
root.order.add_edge(Transition(label='Crop Harvest'), Transition(label='Packaging Prep'))
root.order.add_edge(Transition(label='Crop Harvest'), Transition(label='Distribution Plan'))
root.order.add_edge(Transition(label='Distribution Plan'), Transition(label='Regulation Check'))
root.order.add_edge(Transition(label='Distribution Plan'), Transition(label='Waste Recycling'))
root.order.add_edge(Transition(label='Regulation Check'), Transition(label='System Maintenance'))
root.order.add_edge(Transition(label='Waste Recycling'), Transition(label='System Maintenance'))