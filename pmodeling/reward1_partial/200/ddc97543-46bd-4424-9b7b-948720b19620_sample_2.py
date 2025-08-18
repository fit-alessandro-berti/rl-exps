root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Structure Prep'),
    Transition(label='System Install'),
    Transition(label='Env Control'),
    Transition(label='Nutrient Mix'),
    Transition(label='Crop Select'),
    Transition(label='AI Setup'),
    Transition(label='Worker Train'),
    Transition(label='Pest Control'),
    Transition(label='Irrigation Plan'),
    Transition(label='Data Monitor'),
    Transition(label='Yield Forecast'),
    Transition(label='Energy Audit'),
    Transition(label='Market Setup'),
    Transition(label='Logistics Plan'),
    Transition(label='Waste Manage')
])

root.order.add_edge(Transition(label='Site Survey'), Transition(label='Structure Prep'))
root.order.add_edge(Transition(label='Structure Prep'), Transition(label='System Install'))
root.order.add_edge(Transition(label='System Install'), Transition(label='Env Control'))
root.order.add_edge(Transition(label='Env Control'), Transition(label='Nutrient Mix'))
root.order.add_edge(Transition(label='Nutrient Mix'), Transition(label='Crop Select'))
root.order.add_edge(Transition(label='Crop Select'), Transition(label='AI Setup'))
root.order.add_edge(Transition(label='AI Setup'), Transition(label='Worker Train'))
root.order.add_edge(Transition(label='Worker Train'), Transition(label='Pest Control'))
root.order.add_edge(Transition(label='Pest Control'), Transition(label='Irrigation Plan'))
root.order.add_edge(Transition(label='Irrigation Plan'), Transition(label='Data Monitor'))
root.order.add_edge(Transition(label='Data Monitor'), Transition(label='Yield Forecast'))
root.order.add_edge(Transition(label='Yield Forecast'), Transition(label='Energy Audit'))
root.order.add_edge(Transition(label='Energy Audit'), Transition(label='Market Setup'))
root.order.add_edge(Transition(label='Market Setup'), Transition(label='Logistics Plan'))
root.order.add_edge(Transition(label='Logistics Plan'), Transition(label='Waste Manage'))