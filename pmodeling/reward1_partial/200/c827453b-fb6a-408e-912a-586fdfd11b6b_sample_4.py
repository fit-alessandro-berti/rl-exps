root = StrictPartialOrder(nodes=[
    Transition(label='Sensor Setup'),
    Transition(label='Data Capture'),
    Transition(label='Nutrient Mix'),
    Transition(label='Crop Rotate'),
    Transition(label='Waste Collect'),
    Transition(label='Compost Process'),
    Transition(label='Drone Dispatch'),
    Transition(label='Pest Control'),
    Transition(label='Pollination Run'),
    Transition(label='Volunteer Assign'),
    Transition(label='Feedback Gather'),
    Transition(label='Model Update'),
    Transition(label='Yield Forecast'),
    Transition(label='Water Adjust'),
    Transition(label='Report Generate'),
    Transition(label='Resource Audit'),
    Transition(label='Schedule Sync')
])

# Define the order between transitions
root.order.add_edge(Transition(label='Sensor Setup'), Transition(label='Data Capture'))
root.order.add_edge(Transition(label='Data Capture'), Transition(label='Nutrient Mix'))
root.order.add_edge(Transition(label='Nutrient Mix'), Transition(label='Crop Rotate'))
root.order.add_edge(Transition(label='Crop Rotate'), Transition(label='Waste Collect'))
root.order.add_edge(Transition(label='Waste Collect'), Transition(label='Compost Process'))
root.order.add_edge(Transition(label='Compost Process'), Transition(label='Drone Dispatch'))
root.order.add_edge(Transition(label='Drone Dispatch'), Transition(label='Pest Control'))
root.order.add_edge(Transition(label='Pest Control'), Transition(label='Pollination Run'))
root.order.add_edge(Transition(label='Pollination Run'), Transition(label='Volunteer Assign'))
root.order.add_edge(Transition(label='Volunteer Assign'), Transition(label='Feedback Gather'))
root.order.add_edge(Transition(label='Feedback Gather'), Transition(label='Model Update'))
root.order.add_edge(Transition(label='Model Update'), Transition(label='Yield Forecast'))
root.order.add_edge(Transition(label='Yield Forecast'), Transition(label='Water Adjust'))
root.order.add_edge(Transition(label='Water Adjust'), Transition(label='Report Generate'))
root.order.add_edge(Transition(label='Report Generate'), Transition(label='Resource Audit'))
root.order.add_edge(Transition(label='Resource Audit'), Transition(label='Schedule Sync'))