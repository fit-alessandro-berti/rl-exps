root = StrictPartialOrder(nodes=[
    Transition(label='Artifact Intake'),
    Transition(label='Condition Check'),
    Transition(label='Multi-spectral Scan'),
    Transition(label='Material Test'),
    Transition(label='Database Match'),
    Transition(label='Provenance Check'),
    Transition(label='Expert Review'),
    Transition(label='Historical Query'),
    Transition(label='Lab Collaboration'),
    Transition(label='Imaging Analysis'),
    Transition(label='Forgery Detection'),
    Transition(label='Legal Drafting'),
    Transition(label='Certification Issue'),
    Transition(label='Client Briefing'),
    Transition(label='Archival Update')
])

root.order.add_edge(Transition(label='Artifact Intake'), Transition(label='Condition Check'))
root.order.add_edge(Transition(label='Artifact Intake'), Transition(label='Multi-spectral Scan'))
root.order.add_edge(Transition(label='Artifact Intake'), Transition(label='Material Test'))
root.order.add_edge(Transition(label='Condition Check'), Transition(label='Database Match'))
root.order.add_edge(Transition(label='Condition Check'), Transition(label='Provenance Check'))
root.order.add_edge(Transition(label='Condition Check'), Transition(label='Expert Review'))
root.order.add_edge(Transition(label='Expert Review'), Transition(label='Historical Query'))
root.order.add_edge(Transition(label='Expert Review'), Transition(label='Lab Collaboration'))
root.order.add_edge(Transition(label='Expert Review'), Transition(label='Imaging Analysis'))
root.order.add_edge(Transition(label='Imaging Analysis'), Transition(label='Forgery Detection'))
root.order.add_edge(Transition(label='Forgery Detection'), Transition(label='Legal Drafting'))
root.order.add_edge(Transition(label='Legal Drafting'), Transition(label='Certification Issue'))
root.order.add_edge(Transition(label='Certification Issue'), Transition(label='Client Briefing'))
root.order.add_edge(Transition(label='Certification Issue'), Transition(label='Archival Update'))