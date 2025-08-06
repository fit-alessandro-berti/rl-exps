root = StrictPartialOrder(nodes=[
    Transition(label='Sensor Setup'),
    Transition(label='Data Collection'),
    Transition(label='Weather Check'),
    Transition(label='Soil Testing'),
    Transition(label='Crop Selection'),
    Transition(label='Resource Assign'),
    Transition(label='Irrigation Adjust'),
    Transition(label='Pest Scan'),
    Transition(label='Nutrient Mix'),
    Transition(label='Growth Monitor'),
    Transition(label='Community Poll'),
    Transition(label='Schedule Update'),
    Transition(label='Harvest Plan'),
    Transition(label='Waste Sort'),
    Transition(label='Yield Report')
])

# Define dependencies between activities
root.order.add_edge(Transition('Sensor Setup'), Transition('Data Collection'))
root.order.add_edge(Transition('Data Collection'), Transition('Weather Check'))
root.order.add_edge(Transition('Weather Check'), Transition('Soil Testing'))
root.order.add_edge(Transition('Soil Testing'), Transition('Crop Selection'))
root.order.add_edge(Transition('Crop Selection'), Transition('Resource Assign'))
root.order.add_edge(Transition('Resource Assign'), Transition('Irrigation Adjust'))
root.order.add_edge(Transition('Irrigation Adjust'), Transition('Pest Scan'))
root.order.add_edge(Transition('Pest Scan'), Transition('Nutrient Mix'))
root.order.add_edge(Transition('Nutrient Mix'), Transition('Growth Monitor'))
root.order.add_edge(Transition('Growth Monitor'), Transition('Community Poll'))
root.order.add_edge(Transition('Community Poll'), Transition('Schedule Update'))
root.order.add_edge(Transition('Schedule Update'), Transition('Harvest Plan'))
root.order.add_edge(Transition('Harvest Plan'), Transition('Waste Sort'))
root.order.add_edge(Transition('Waste Sort'), Transition('Yield Report'))