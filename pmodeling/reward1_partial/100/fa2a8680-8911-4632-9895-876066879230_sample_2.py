root = StrictPartialOrder(nodes=[
    Transition(label='Client Meet'),
    Transition(label='Requirement Gather'),
    Transition(label='Module Design'),
    Transition(label='Supplier Vetting'),
    Transition(label='Component Order'),
    Transition(label='Prototype Build'),
    Transition(label='Field Testing'),
    Transition(label='Test Analysis'),
    Transition(label='Software Setup'),
    Transition(label='Data Integration'),
    Transition(label='Pilot Train'),
    Transition(label='Compliance Check'),
    Transition(label='Fleet Deploy'),
    Transition(label='Remote Monitor'),
    Transition(label='Maintenance Plan'),
    Transition(label='Performance Tune')
])

# Define the edges
root.order.add_edge(root.nodes[0], root.nodes[1])  # Client Meet -> Requirement Gather
root.order.add_edge(root.nodes[1], root.nodes[2])  # Requirement Gather -> Module Design
root.order.add_edge(root.nodes[2], root.nodes[3])  # Module Design -> Supplier Vetting
root.order.add_edge(root.nodes[3], root.nodes[4])  # Supplier Vetting -> Component Order
root.order.add_edge(root.nodes[4], root.nodes[5])  # Component Order -> Prototype Build
root.order.add_edge(root.nodes[5], root.nodes[6])  # Prototype Build -> Field Testing
root.order.add_edge(root.nodes[6], root.nodes[7])  # Field Testing -> Test Analysis
root.order.add_edge(root.nodes[7], root.nodes[8])  # Test Analysis -> Software Setup
root.order.add_edge(root.nodes[8], root.nodes[9])  # Software Setup -> Data Integration
root.order.add_edge(root.nodes[9], root.nodes[10])  # Data Integration -> Pilot Train
root.order.add_edge(root.nodes[10], root.nodes[11])  # Pilot Train -> Compliance Check
root.order.add_edge(root.nodes[11], root.nodes[12])  # Compliance Check -> Fleet Deploy
root.order.add_edge(root.nodes[12], root.nodes[13])  # Fleet Deploy -> Remote Monitor
root.order.add_edge(root.nodes[13], root.nodes[14])  # Remote Monitor -> Maintenance Plan
root.order.add_edge(root.nodes[14], root.nodes[15])  # Maintenance Plan -> Performance Tune

# Add a loop to maintain the process
loop = OperatorPOWL(operator=Operator.LOOP, children=[root.nodes[15]])
root.order.add_edge(root.nodes[15], loop)
root.order.add_edge(loop, root.nodes[15])  # Loop back to Performance Tune

# Add a choice to select between maintenance or performance tuning
choice = OperatorPOWL(operator=Operator.XOR, children=[root.nodes[14], root.nodes[15]])
root.order.add_edge(root.nodes[14], choice)
root.order.add_edge(root.nodes[15], choice)<|fim_middle|>