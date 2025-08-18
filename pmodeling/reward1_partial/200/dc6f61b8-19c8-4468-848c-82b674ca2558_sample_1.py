root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Energy Partner'),
    Transition(label='Permit Filing'),
    Transition(label='Hydro Unit'),
    Transition(label='AI Setup'),
    Transition(label='Nutrient Plan'),
    Transition(label='System Install'),
    Transition(label='Crop Testing'),
    Transition(label='Data Analysis'),
    Transition(label='Community Meet'),
    Transition(label='Yield Adjust'),
    Transition(label='Carbon Audit'),
    Transition(label='Logistics Plan'),
    Transition(label='Quality Check'),
    Transition(label='Scale Review')
])

root.order.add_edge(Transition(label='Site Survey'), Transition(label='Energy Partner'))
root.order.add_edge(Transition(label='Site Survey'), Transition(label='Permit Filing'))
root.order.add_edge(Transition(label='Energy Partner'), Transition(label='Hydro Unit'))
root.order.add_edge(Transition(label='Permit Filing'), Transition(label='Hydro Unit'))
root.order.add_edge(Transition(label='Hydro Unit'), Transition(label='AI Setup'))
root.order.add_edge(Transition(label='AI Setup'), Transition(label='Nutrient Plan'))
root.order.add_edge(Transition(label='Nutrient Plan'), Transition(label='System Install'))
root.order.add_edge(Transition(label='System Install'), Transition(label='Crop Testing'))
root.order.add_edge(Transition(label='Crop Testing'), Transition(label='Data Analysis'))
root.order.add_edge(Transition(label='Data Analysis'), Transition(label='Community Meet'))
root.order.add_edge(Transition(label='Community Meet'), Transition(label='Yield Adjust'))
root.order.add_edge(Transition(label='Yield Adjust'), Transition(label='Carbon Audit'))
root.order.add_edge(Transition(label='Carbon Audit'), Transition(label='Logistics Plan'))
root.order.add_edge(Transition(label='Logistics Plan'), Transition(label='Quality Check'))
root.order.add_edge(Transition(label='Quality Check'), Transition(label='Scale Review'))