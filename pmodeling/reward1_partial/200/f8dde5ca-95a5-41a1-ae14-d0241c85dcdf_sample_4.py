root = StrictPartialOrder(nodes=[
    Transition(label='Provenance Check'),
    Transition(label='Material Scan'),
    Transition(label='Radiocarbon Test'),
    Transition(label='Style Compare'),
    Transition(label='Database Query'),
    Transition(label='Blockchain Prep'),
    Transition(label='Legal Review'),
    Transition(label='Ownership Audit'),
    Transition(label='Conservation Plan'),
    Transition(label='Expert Panel'),
    Transition(label='Report Draft'),
    Transition(label='Client Review'),
    Transition(label='Authority Submit'),
    Transition(label='Exhibit Setup'),
    Transition(label='Final Approval')
])

root.order.add_edge(Transition(label='Provenance Check'), Transition(label='Material Scan'))
root.order.add_edge(Transition(label='Material Scan'), Transition(label='Radiocarbon Test'))
root.order.add_edge(Transition(label='Radiocarbon Test'), Transition(label='Style Compare'))
root.order.add_edge(Transition(label='Style Compare'), Transition(label='Database Query'))
root.order.add_edge(Transition(label='Database Query'), Transition(label='Blockchain Prep'))
root.order.add_edge(Transition(label='Blockchain Prep'), Transition(label='Legal Review'))
root.order.add_edge(Transition(label='Legal Review'), Transition(label='Ownership Audit'))
root.order.add_edge(Transition(label='Ownership Audit'), Transition(label='Conservation Plan'))
root.order.add_edge(Transition(label='Conservation Plan'), Transition(label='Expert Panel'))
root.order.add_edge(Transition(label='Expert Panel'), Transition(label='Report Draft'))
root.order.add_edge(Transition(label='Report Draft'), Transition(label='Client Review'))
root.order.add_edge(Transition(label='Client Review'), Transition(label='Authority Submit'))
root.order.add_edge(Transition(label='Authority Submit'), Transition(label='Exhibit Setup'))
root.order.add_edge(Transition(label='Exhibit Setup'), Transition(label='Final Approval'))