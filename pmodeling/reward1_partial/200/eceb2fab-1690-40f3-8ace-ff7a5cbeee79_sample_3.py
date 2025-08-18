root = StrictPartialOrder(nodes=[
    Transition(label='Provenance Check'),
    Transition(label='Condition Scan'),
    Transition(label='Material Test'),
    Transition(label='Disassembly'),
    Transition(label='Surface Clean'),
    Transition(label='Structural Repair'),
    Transition(label='Reconstruction'),
    Transition(label='Finish Match'),
    Transition(label='Stabilize Parts'),
    Transition(label='Documentation'),
    Transition(label='Quality Audit'),
    Transition(label='Valuation'),
    Transition(label='Market Analysis'),
    Transition(label='Target Outreach'),
    Transition(label='Delivery Prep'),
    Transition(label='Client Feedback')
])

root.order.add_edge(Transition(label='Provenance Check'), Transition(label='Condition Scan'))
root.order.add_edge(Transition(label='Condition Scan'), Transition(label='Material Test'))
root.order.add_edge(Transition(label='Material Test'), Transition(label='Disassembly'))
root.order.add_edge(Transition(label='Disassembly'), Transition(label='Surface Clean'))
root.order.add_edge(Transition(label='Surface Clean'), Transition(label='Structural Repair'))
root.order.add_edge(Transition(label='Structural Repair'), Transition(label='Reconstruction'))
root.order.add_edge(Transition(label='Reconstruction'), Transition(label='Finish Match'))
root.order.add_edge(Transition(label='Finish Match'), Transition(label='Stabilize Parts'))
root.order.add_edge(Transition(label='Stabilize Parts'), Transition(label='Documentation'))
root.order.add_edge(Transition(label='Documentation'), Transition(label='Quality Audit'))
root.order.add_edge(Transition(label='Quality Audit'), Transition(label='Valuation'))
root.order.add_edge(Transition(label='Valuation'), Transition(label='Market Analysis'))
root.order.add_edge(Transition(label='Market Analysis'), Transition(label='Target Outreach'))
root.order.add_edge(Transition(label='Target Outreach'), Transition(label='Delivery Prep'))
root.order.add_edge(Transition(label='Delivery Prep'), Transition(label='Client Feedback'))