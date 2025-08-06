root = StrictPartialOrder(nodes=[
    Transition('Site Assess'),
    Transition('Env Analysis'),
    Transition('Modular Install'),
    Transition('Irrigation Setup'),
    Transition('Crop Selection'),
    Transition('Nutrient Mix'),
    Transition('Lighting Calibrate'),
    Transition('Pest Monitor'),
    Transition('Staff Training'),
    Transition('Energy Integrate'),
    Transition('Data Analytics'),
    Transition('Waste Recycle'),
    Transition('Market Develop'),
    Transition('Yield Optimize'),
    Transition('Climate Simulate')
])

root.order.add_edge(Transition('Site Assess'), Transition('Env Analysis'))
root.order.add_edge(Transition('Env Analysis'), Transition('Modular Install'))
root.order.add_edge(Transition('Modular Install'), Transition('Irrigation Setup'))
root.order.add_edge(Transition('Irrigation Setup'), Transition('Crop Selection'))
root.order.add_edge(Transition('Crop Selection'), Transition('Nutrient Mix'))
root.order.add_edge(Transition('Nutrient Mix'), Transition('Lighting Calibrate'))
root.order.add_edge(Transition('Lighting Calibrate'), Transition('Pest Monitor'))
root.order.add_edge(Transition('Pest Monitor'), Transition('Staff Training'))
root.order.add_edge(Transition('Staff Training'), Transition('Energy Integrate'))
root.order.add_edge(Transition('Energy Integrate'), Transition('Data Analytics'))
root.order.add_edge(Transition('Data Analytics'), Transition('Waste Recycle'))
root.order.add_edge(Transition('Waste Recycle'), Transition('Market Develop'))
root.order.add_edge(Transition('Market Develop'), Transition('Yield Optimize'))
root.order.add_edge(Transition('Yield Optimize'), Transition('Climate Simulate'))