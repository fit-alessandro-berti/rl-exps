root = StrictPartialOrder(nodes=[
    Transition(label='Artifact Intake'),
    Transition(label='Preliminary Check'),
    Transition(label='Historical Review'),
    Transition(label='Chemical Test'),
    Transition(label='Provenance Audit'),
    Transition(label='Expert Panel'),
    Transition(label='Token Minting'),
    Transition(label='Legal Review'),
    Transition(label='Compliance Check'),
    Transition(label='Insurance Valuation'),
    Transition(label='Risk Assessment'),
    Transition(label='Packaging Prep'),
    Transition(label='Climate Control'),
    Transition(label='Transport Setup'),
    Transition(label='Final Approval')
])

root.order.add_edge(Transition(label='Artifact Intake'), Transition(label='Preliminary Check'))
root.order.add_edge(Transition(label='Preliminary Check'), Transition(label='Historical Review'))
root.order.add_edge(Transition(label='Preliminary Check'), Transition(label='Chemical Test'))
root.order.add_edge(Transition(label='Preliminary Check'), Transition(label='Provenance Audit'))
root.order.add_edge(Transition(label='Historical Review'), Transition(label='Expert Panel'))
root.order.add_edge(Transition(label='Chemical Test'), Transition(label='Expert Panel'))
root.order.add_edge(Transition(label='Provenance Audit'), Transition(label='Expert Panel'))
root.order.add_edge(Transition(label='Expert Panel'), Transition(label='Token Minting'))
root.order.add_edge(Transition(label='Token Minting'), Transition(label='Legal Review'))
root.order.add_edge(Transition(label='Legal Review'), Transition(label='Compliance Check'))
root.order.add_edge(Transition(label='Compliance Check'), Transition(label='Insurance Valuation'))
root.order.add_edge(Transition(label='Insurance Valuation'), Transition(label='Risk Assessment'))
root.order.add_edge(Transition(label='Risk Assessment'), Transition(label='Packaging Prep'))
root.order.add_edge(Transition(label='Packaging Prep'), Transition(label='Climate Control'))
root.order.add_edge(Transition(label='Climate Control'), Transition(label='Transport Setup'))
root.order.add_edge(Transition(label='Transport Setup'), Transition(label='Final Approval'))