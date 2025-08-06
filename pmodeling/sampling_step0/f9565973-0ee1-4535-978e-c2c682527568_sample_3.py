root = StrictPartialOrder(nodes=[
    Transition(label='Artifact Intake'),
    Transition(label='Initial Survey'),
    Transition(label='Material Test'),
    Transition(label='Historical Check'),
    Transition(label='Registry Search'),
    Transition(label='Owner Interview'),
    Transition(label='Condition Report'),
    Transition(label='Forgery Scan'),
    Transition(label='Digital Tagging'),
    Transition(label='Ledger Entry'),
    Transition(label='Expert Review'),
    Transition(label='Legal Verify'),
    Transition(label='Provenance Draft'),
    Transition(label='Client Approval'),
    Transition(label='Final Certificate'),
    Transition(label='Archive Storage')
])

root.order.add_edge(Transition(label='Artifact Intake'), Transition(label='Initial Survey'))
root.order.add_edge(Transition(label='Initial Survey'), Transition(label='Material Test'))
root.order.add_edge(Transition(label='Material Test'), Transition(label='Historical Check'))
root.order.add_edge(Transition(label='Historical Check'), Transition(label='Registry Search'))
root.order.add_edge(Transition(label='Registry Search'), Transition(label='Owner Interview'))
root.order.add_edge(Transition(label='Owner Interview'), Transition(label='Condition Report'))
root.order.add_edge(Transition(label='Condition Report'), Transition(label='Forgery Scan'))
root.order.add_edge(Transition(label='Forgery Scan'), Transition(label='Digital Tagging'))
root.order.add_edge(Transition(label='Digital Tagging'), Transition(label='Ledger Entry'))
root.order.add_edge(Transition(label='Ledger Entry'), Transition(label='Expert Review'))
root.order.add_edge(Transition(label='Expert Review'), Transition(label='Legal Verify'))
root.order.add_edge(Transition(label='Legal Verify'), Transition(label='Provenance Draft'))
root.order.add_edge(Transition(label='Provenance Draft'), Transition(label='Client Approval'))
root.order.add_edge(Transition(label='Client Approval'), Transition(label='Final Certificate'))
root.order.add_edge(Transition(label='Final Certificate'), Transition(label='Archive Storage'))