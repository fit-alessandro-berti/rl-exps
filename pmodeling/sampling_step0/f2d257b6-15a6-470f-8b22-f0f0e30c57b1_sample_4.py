root = StrictPartialOrder(nodes=[
    Transition(label='Artifact Intake'),
    Transition(label='Condition Check'),
    Transition(label='Material Sampling'),
    Transition(label='Radiocarbon Test'),
    Transition(label='Provenance Review'),
    Transition(label='Imaging Capture'),
    Transition(label='Chemical Analysis'),
    Transition(label='Historical Match'),
    Transition(label='Expert Consult'),
    Transition(label='Forgery Scan'),
    Transition(label='Market Survey'),
    Transition(label='Value Estimate'),
    Transition(label='Certification'),
    Transition(label='Digital Archive'),
    Transition(label='Final Storage'),
])

root.order.add_edge(Transition(label='Artifact Intake'), Transition(label='Condition Check'))
root.order.add_edge(Transition(label='Condition Check'), Transition(label='Material Sampling'))
root.order.add_edge(Transition(label='Material Sampling'), Transition(label='Radiocarbon Test'))
root.order.add_edge(Transition(label='Radiocarbon Test'), Transition(label='Provenance Review'))
root.order.add_edge(Transition(label='Provenance Review'), Transition(label='Imaging Capture'))
root.order.add_edge(Transition(label='Imaging Capture'), Transition(label='Chemical Analysis'))
root.order.add_edge(Transition(label='Chemical Analysis'), Transition(label='Historical Match'))
root.order.add_edge(Transition(label='Historical Match'), Transition(label='Expert Consult'))
root.order.add_edge(Transition(label='Expert Consult'), Transition(label='Forgery Scan'))
root.order.add_edge(Transition(label='Forgery Scan'), Transition(label='Market Survey'))
root.order.add_edge(Transition(label='Market Survey'), Transition(label='Value Estimate'))
root.order.add_edge(Transition(label='Value Estimate'), Transition(label='Certification'))
root.order.add_edge(Transition(label='Certification'), Transition(label='Digital Archive'))
root.order.add_edge(Transition(label='Digital Archive'), Transition(label='Final Storage'))