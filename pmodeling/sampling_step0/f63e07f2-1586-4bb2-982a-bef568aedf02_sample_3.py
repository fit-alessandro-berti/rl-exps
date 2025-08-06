root = StrictPartialOrder(nodes=[
    Transition(label='Artifact Intake'),
    Transition(label='Provenance Check'),
    Transition(label='Archive Research'),
    Transition(label='Expert Interview'),
    Transition(label='Material Analysis'),
    Transition(label='Spectroscopy Test'),
    Transition(label='Carbon Dating'),
    Transition(label='Digital Imaging'),
    Transition(label='3D Modeling'),
    Transition(label='Data Review'),
    Transition(label='Consensus Meeting'),
    Transition(label='Conservation Plan'),
    Transition(label='Preservation Setup'),
    Transition(label='Documentation'),
    Transition(label='Exhibition Prep'),
])

root.order.add_edge(Transition(label='Artifact Intake'), Transition(label='Provenance Check'))
root.order.add_edge(Transition(label='Provenance Check'), Transition(label='Archive Research'))
root.order.add_edge(Transition(label='Provenance Check'), Transition(label='Expert Interview'))
root.order.add_edge(Transition(label='Archive Research'), Transition(label='Data Review'))
root.order.add_edge(Transition(label='Expert Interview'), Transition(label='Data Review'))
root.order.add_edge(Transition(label='Material Analysis'), Transition(label='Data Review'))
root.order.add_edge(Transition(label='Spectroscopy Test'), Transition(label='Data Review'))
root.order.add_edge(Transition(label='Carbon Dating'), Transition(label='Data Review'))
root.order.add_edge(Transition(label='Digital Imaging'), Transition(label='Data Review'))
root.order.add_edge(Transition(label='3D Modeling'), Transition(label='Data Review'))
root.order.add_edge(Transition(label='Data Review'), Transition(label='Consensus Meeting'))
root.order.add_edge(Transition(label='Consensus Meeting'), Transition(label='Conservation Plan'))
root.order.add_edge(Transition(label='Consensus Meeting'), Transition(label='Preservation Setup'))
root.order.add_edge(Transition(label='Conservation Plan'), Transition(label='Documentation'))
root.order.add_edge(Transition(label='Preservation Setup'), Transition(label='Documentation'))
root.order.add_edge(Transition(label='Documentation'), Transition(label='Exhibition Prep'))