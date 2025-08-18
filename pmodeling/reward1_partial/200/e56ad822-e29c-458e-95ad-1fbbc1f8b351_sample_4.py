root = StrictPartialOrder(nodes=[
    Transition(label='Submit Artifact'),
    Transition(label='Initial Review'),
    Transition(label='Provenance Check'),
    Transition(label='Material Scan'),
    Transition(label='Context Analysis'),
    Transition(label='Expert Panel'),
    Transition(label='Digital Fingerprint'),
    Transition(label='AI Pattern'),
    Transition(label='Legal Audit'),
    Transition(label='Ethics Review'),
    Transition(label='Fraud Detection'),
    Transition(label='Blockchain Log'),
    Transition(label='Certification'),
    Transition(label='Owner Notify'),
    Transition(label='Archive Data'),
    Transition(label='Secure Storage')
])

root.order.add_edge(Transition(label='Submit Artifact'), Transition(label='Initial Review'))
root.order.add_edge(Transition(label='Initial Review'), Transition(label='Provenance Check'))
root.order.add_edge(Transition(label='Provenance Check'), Transition(label='Material Scan'))
root.order.add_edge(Transition(label='Material Scan'), Transition(label='Context Analysis'))
root.order.add_edge(Transition(label='Context Analysis'), Transition(label='Expert Panel'))
root.order.add_edge(Transition(label='Expert Panel'), Transition(label='Digital Fingerprint'))
root.order.add_edge(Transition(label='Digital Fingerprint'), Transition(label='AI Pattern'))
root.order.add_edge(Transition(label='AI Pattern'), Transition(label='Legal Audit'))
root.order.add_edge(Transition(label='Legal Audit'), Transition(label='Ethics Review'))
root.order.add_edge(Transition(label='Ethics Review'), Transition(label='Fraud Detection'))
root.order.add_edge(Transition(label='Fraud Detection'), Transition(label='Blockchain Log'))
root.order.add_edge(Transition(label='Blockchain Log'), Transition(label='Certification'))
root.order.add_edge(Transition(label='Certification'), Transition(label='Owner Notify'))
root.order.add_edge(Transition(label='Owner Notify'), Transition(label='Archive Data'))
root.order.add_edge(Transition(label='Archive Data'), Transition(label='Secure Storage'))