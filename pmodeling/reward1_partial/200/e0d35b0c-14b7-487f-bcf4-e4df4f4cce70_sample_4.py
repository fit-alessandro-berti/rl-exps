root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Structural Check'),
    Transition(label='Resource Sourcing'),
    Transition(label='System Install'),
    Transition(label='Lighting Setup'),
    Transition(label='Irrigation Setup'),
    Transition(label='Stakeholder Meet'),
    Transition(label='Volunteer Train'),
    Transition(label='Regulation Review'),
    Transition(label='Crop Selection'),
    Transition(label='Planting Phase'),
    Transition(label='Climate Control'),
    Transition(label='Growth Monitor'),
    Transition(label='Data Logging'),
    Transition(label='Harvest Event'),
    Transition(label='Waste Manage'),
    Transition(label='Feedback Collect')
])

# Define the relationships between the activities
root.order.add_edge(root.nodes[0], root.nodes[1])  # Site Survey -> Structural Check
root.order.add_edge(root.nodes[1], root.nodes[2])  # Structural Check -> Resource Sourcing
root.order.add_edge(root.nodes[2], root.nodes[3])  # Resource Sourcing -> System Install
root.order.add_edge(root.nodes[3], root.nodes[4])  # System Install -> Lighting Setup
root.order.add_edge(root.nodes[3], root.nodes[5])  # System Install -> Irrigation Setup
root.order.add_edge(root.nodes[4], root.nodes[6])  # Lighting Setup -> Stakeholder Meet
root.order.add_edge(root.nodes[5], root.nodes[6])  # Irrigation Setup -> Stakeholder Meet
root.order.add_edge(root.nodes[6], root.nodes[7])  # Stakeholder Meet -> Volunteer Train
root.order.add_edge(root.nodes[6], root.nodes[8])  # Stakeholder Meet -> Regulation Review
root.order.add_edge(root.nodes[7], root.nodes[9])  # Volunteer Train -> Crop Selection
root.order.add_edge(root.nodes[8], root.nodes[9])  # Regulation Review -> Crop Selection
root.order.add_edge(root.nodes[9], root.nodes[10])  # Crop Selection -> Planting Phase
root.order.add_edge(root.nodes[10], root.nodes[11])  # Planting Phase -> Climate Control
root.order.add_edge(root.nodes[10], root.nodes[12])  # Planting Phase -> Growth Monitor
root.order.add_edge(root.nodes[11], root.nodes[13])  # Climate Control -> Data Logging
root.order.add_edge(root.nodes[12], root.nodes[13])  # Growth Monitor -> Data Logging
root.order.add_edge(root.nodes[13], root.nodes[14])  # Data Logging -> Harvest Event
root.order.add_edge(root.nodes[13], root.nodes[15])  # Data Logging -> Waste Manage
root.order.add_edge(root.nodes[14], root.nodes[16])  # Harvest Event -> Feedback Collect
root.order.add_edge(root.nodes[15], root.nodes[16])  # Waste Manage -> Feedback Collect