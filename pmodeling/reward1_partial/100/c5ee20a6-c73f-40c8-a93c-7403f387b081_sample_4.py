root = StrictPartialOrder(nodes=[
    Transition(label='Initial Assess'),
    Transition(label='Condition Scan'),
    Transition(label='Material Test'),
    Transition(label='Historical Check'),
    Transition(label='Provenance Verify'),
    Transition(label='Parts Sourcing'),
    Transition(label='Gentle Clean'),
    Transition(label='Stabilize Item'),
    Transition(label='Structural Repair'),
    Transition(label='Surface Finish'),
    Transition(label='Expert Consult'),
    Transition(label='Archival Review'),
    Transition(label='Ethics Audit'),
    Transition(label='Quality Inspect'),
    Transition(label='Photo Document'),
    Transition(label='Packaging Prep'),
    Transition(label='Report Generate'),
    Transition(label='Certify Provenance'),
])

root.order.add_edge(Transition(label='Initial Assess'), Transition(label='Condition Scan'))
root.order.add_edge(Transition(label='Initial Assess'), Transition(label='Material Test'))
root.order.add_edge(Transition(label='Initial Assess'), Transition(label='Historical Check'))
root.order.add_edge(Transition(label='Initial Assess'), Transition(label='Provenance Verify'))
root.order.add_edge(Transition(label='Initial Assess'), Transition(label='Parts Sourcing'))
root.order.add_edge(Transition(label='Initial Assess'), Transition(label='Gentle Clean'))
root.order.add_edge(Transition(label='Initial Assess'), Transition(label='Stabilize Item'))
root.order.add_edge(Transition(label='Initial Assess'), Transition(label='Structural Repair'))
root.order.add_edge(Transition(label='Initial Assess'), Transition(label='Surface Finish'))
root.order.add_edge(Transition(label='Initial Assess'), Transition(label='Expert Consult'))
root.order.add_edge(Transition(label='Initial Assess'), Transition(label='Archival Review'))
root.order.add_edge(Transition(label='Initial Assess'), Transition(label='Ethics Audit'))
root.order.add_edge(Transition(label='Initial Assess'), Transition(label='Quality Inspect'))
root.order.add_edge(Transition(label='Initial Assess'), Transition(label='Photo Document'))
root.order.add_edge(Transition(label='Initial Assess'), Transition(label='Packaging Prep'))
root.order.add_edge(Transition(label='Initial Assess'), Transition(label='Report Generate'))
root.order.add_edge(Transition(label='Initial Assess'), Transition(label='Certify Provenance'))