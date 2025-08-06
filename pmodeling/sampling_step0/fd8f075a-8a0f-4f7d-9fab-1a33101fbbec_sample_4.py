root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Permit Filing'),
    Transition(label='Structure Prep'),
    Transition(label='System Install'),
    Transition(label='Nutrient Mix'),
    Transition(label='Sensor Setup'),
    Transition(label='AI Calibration'),
    Transition(label='Seed Sourcing'),
    Transition(label='Staff Training'),
    Transition(label='Energy Connect'),
    Transition(label='Water Cycle'),
    Transition(label='Growth Monitor'),
    Transition(label='Waste Audit'),
    Transition(label='Community Meet'),
    Transition(label='Data Review'),
    Transition(label='Yield Forecast')
])

# Define edges based on the process flow
root.order.add_edge(root.nodes[0], root.nodes[1])  # Site Survey -> Permit Filing
root.order.add_edge(root.nodes[1], root.nodes[2])  # Permit Filing -> Structure Prep
root.order.add_edge(root.nodes[2], root.nodes[3])  # Structure Prep -> System Install
root.order.add_edge(root.nodes[3], root.nodes[4])  # System Install -> Nutrient Mix
root.order.add_edge(root.nodes[4], root.nodes[5])  # Nutrient Mix -> Sensor Setup
root.order.add_edge(root.nodes[5], root.nodes[6])  # Sensor Setup -> AI Calibration
root.order.add_edge(root.nodes[6], root.nodes[7])  # AI Calibration -> Seed Sourcing
root.order.add_edge(root.nodes[7], root.nodes[8])  # Seed Sourcing -> Staff Training
root.order.add_edge(root.nodes[8], root.nodes[9])  # Staff Training -> Energy Connect
root.order.add_edge(root.nodes[9], root.nodes[10])  # Energy Connect -> Water Cycle
root.order.add_edge(root.nodes[10], root.nodes[11])  # Water Cycle -> Growth Monitor
root.order.add_edge(root.nodes[11], root.nodes[12])  # Growth Monitor -> Waste Audit
root.order.add_edge(root.nodes[12], root.nodes[13])  # Waste Audit -> Community Meet
root.order.add_edge(root.nodes[13], root.nodes[14])  # Community Meet -> Data Review
root.order.add_edge(root.nodes[14], root.nodes[15])  # Data Review -> Yield Forecast