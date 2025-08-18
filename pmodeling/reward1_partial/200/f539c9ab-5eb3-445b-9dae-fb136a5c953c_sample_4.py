root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Structural Audit'),
    Transition(label='Modular Design'),
    Transition(label='Hydroponic Setup'),
    Transition(label='Climate Config'),
    Transition(label='Nutrient Mix'),
    Transition(label='Pest Detect'),
    Transition(label='Lighting Setup'),
    Transition(label='Energy Audit'),
    Transition(label='Automation Install'),
    Transition(label='Staff Training'),
    Transition(label='Market Analysis'),
    Transition(label='Regulation Check'),
    Transition(label='Yield Monitor'),
    Transition(label='Waste Manage'),
    Transition(label='Data Analytics')
])

# Define the order of activities
root.order.add_edge(Transition(label='Site Survey'), Transition(label='Structural Audit'))
root.order.add_edge(Transition(label='Structural Audit'), Transition(label='Modular Design'))
root.order.add_edge(Transition(label='Modular Design'), Transition(label='Hydroponic Setup'))
root.order.add_edge(Transition(label='Hydroponic Setup'), Transition(label='Climate Config'))
root.order.add_edge(Transition(label='Climate Config'), Transition(label='Nutrient Mix'))
root.order.add_edge(Transition(label='Nutrient Mix'), Transition(label='Pest Detect'))
root.order.add_edge(Transition(label='Pest Detect'), Transition(label='Lighting Setup'))
root.order.add_edge(Transition(label='Lighting Setup'), Transition(label='Energy Audit'))
root.order.add_edge(Transition(label='Energy Audit'), Transition(label='Automation Install'))
root.order.add_edge(Transition(label='Automation Install'), Transition(label='Staff Training'))
root.order.add_edge(Transition(label='Staff Training'), Transition(label='Market Analysis'))
root.order.add_edge(Transition(label='Market Analysis'), Transition(label='Regulation Check'))
root.order.add_edge(Transition(label='Regulation Check'), Transition(label='Yield Monitor'))
root.order.add_edge(Transition(label='Yield Monitor'), Transition(label='Waste Manage'))
root.order.add_edge(Transition(label='Waste Manage'), Transition(label='Data Analytics'))