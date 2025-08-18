root = StrictPartialOrder(nodes=[
    Transition(label='Initial Assess'),
    Transition(label='Artifact Scan'),
    Transition(label='Condition Map'),
    Transition(label='Material Test'),
    Transition(label='Cleaning Phase'),
    Transition(label='Stability Check'),
    Transition(label='Minor Repair'),
    Transition(label='Structural Reinforce'),
    Transition(label='Surface Restore'),
    Transition(label='Coating Apply'),
    Transition(label='Ethics Review'),
    Transition(label='Provenance Verify'),
    Transition(label='Client Update'),
    Transition(label='Final Report'),
    Transition(label='Archive Store')
])

# Define dependencies based on the process flow
root.order.add_edge(Transition(label='Initial Assess'), Transition(label='Artifact Scan'))
root.order.add_edge(Transition(label='Artifact Scan'), Transition(label='Condition Map'))
root.order.add_edge(Transition(label='Condition Map'), Transition(label='Material Test'))
root.order.add_edge(Transition(label='Material Test'), Transition(label='Cleaning Phase'))
root.order.add_edge(Transition(label='Cleaning Phase'), Transition(label='Stability Check'))
root.order.add_edge(Transition(label='Stability Check'), Transition(label='Minor Repair'))
root.order.add_edge(Transition(label='Minor Repair'), Transition(label='Structural Reinforce'))
root.order.add_edge(Transition(label='Structural Reinforce'), Transition(label='Surface Restore'))
root.order.add_edge(Transition(label='Surface Restore'), Transition(label='Coating Apply'))
root.order.add_edge(Transition(label='Coating Apply'), Transition(label='Ethics Review'))
root.order.add_edge(Transition(label='Ethics Review'), Transition(label='Provenance Verify'))
root.order.add_edge(Transition(label='Provenance Verify'), Transition(label='Client Update'))
root.order.add_edge(Transition(label='Client Update'), Transition(label='Final Report'))
root.order.add_edge(Transition(label='Final Report'), Transition(label='Archive Store'))