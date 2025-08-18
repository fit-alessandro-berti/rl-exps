root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Structural Check'),
    Transition(label='Env Control'),
    Transition(label='Hydro Setup'),
    Transition(label='Crop Select'),
    Transition(label='IoT Install'),
    Transition(label='Sensor Calibrate'),
    Transition(label='Water Cycle'),
    Transition(label='Nutrient Mix'),
    Transition(label='Lighting Adjust'),
    Transition(label='Staff Train'),
    Transition(label='Waste Manage'),
    Transition(label='Energy Audit'),
    Transition(label='Harvest Plan'),
    Transition(label='Delivery Setup'),
    Transition(label='Market Align')
])

# Define the dependencies between activities
root.order.add_edge(Transition(label='Site Survey'), Transition(label='Structural Check'))
root.order.add_edge(Transition(label='Site Survey'), Transition(label='Env Control'))
root.order.add_edge(Transition(label='Structural Check'), Transition(label='Hydro Setup'))
root.order.add_edge(Transition(label='Env Control'), Transition(label='Hydro Setup'))
root.order.add_edge(Transition(label='Hydro Setup'), Transition(label='Crop Select'))
root.order.add_edge(Transition(label='Crop Select'), Transition(label='IoT Install'))
root.order.add_edge(Transition(label='IoT Install'), Transition(label='Sensor Calibrate'))
root.order.add_edge(Transition(label='Sensor Calibrate'), Transition(label='Water Cycle'))
root.order.add_edge(Transition(label='Water Cycle'), Transition(label='Nutrient Mix'))
root.order.add_edge(Transition(label='Nutrient Mix'), Transition(label='Lighting Adjust'))
root.order.add_edge(Transition(label='Lighting Adjust'), Transition(label='Staff Train'))
root.order.add_edge(Transition(label='Staff Train'), Transition(label='Waste Manage'))
root.order.add_edge(Transition(label='Waste Manage'), Transition(label='Energy Audit'))
root.order.add_edge(Transition(label='Energy Audit'), Transition(label='Harvest Plan'))
root.order.add_edge(Transition(label='Harvest Plan'), Transition(label='Delivery Setup'))
root.order.add_edge(Transition(label='Delivery Setup'), Transition(label='Market Align'))