root = StrictPartialOrder(nodes=[
    Transition(label='Provenance Check'),
    Transition(label='Specimen Sampling'),
    Transition(label='Spectroscopy Test'),
    Transition(label='Radiocarbon Date'),
    Transition(label='Material Analysis'),
    Transition(label='Forensic Review'),
    Transition(label='Expert Consult'),
    Transition(label='Legal Verify'),
    Transition(label='Ownership Audit'),
    Transition(label='Risk Assess'),
    Transition(label='Insurance Quote'),
    Transition(label='Condition Report'),
    Transition(label='Documentation'),
    Transition(label='Committee Review'),
    Transition(label='Final Approval')
])

# Define the dependencies between the nodes
root.order.add_edge(Transition(label='Provenance Check'), Transition(label='Specimen Sampling'))
root.order.add_edge(Transition(label='Specimen Sampling'), Transition(label='Spectroscopy Test'))
root.order.add_edge(Transition(label='Specimen Sampling'), Transition(label='Radiocarbon Date'))
root.order.add_edge(Transition(label='Specimen Sampling'), Transition(label='Material Analysis'))
root.order.add_edge(Transition(label='Specimen Sampling'), Transition(label='Forensic Review'))
root.order.add_edge(Transition(label='Specimen Sampling'), Transition(label='Expert Consult'))
root.order.add_edge(Transition(label='Specimen Sampling'), Transition(label='Legal Verify'))
root.order.add_edge(Transition(label='Specimen Sampling'), Transition(label='Ownership Audit'))
root.order.add_edge(Transition(label='Specimen Sampling'), Transition(label='Risk Assess'))
root.order.add_edge(Transition(label='Specimen Sampling'), Transition(label='Insurance Quote'))
root.order.add_edge(Transition(label='Specimen Sampling'), Transition(label='Condition Report'))
root.order.add_edge(Transition(label='Specimen Sampling'), Transition(label='Documentation'))
root.order.add_edge(Transition(label='Specimen Sampling'), Transition(label='Committee Review'))
root.order.add_edge(Transition(label='Specimen Sampling'), Transition(label='Final Approval'))