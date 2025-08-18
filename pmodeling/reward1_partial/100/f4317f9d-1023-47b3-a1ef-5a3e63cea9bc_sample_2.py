root = StrictPartialOrder(nodes=[
    Transition(label='Provenance Check'),
    Transition(label='Material Scan'),
    Transition(label='Style Compare'),
    Transition(label='AI Imaging'),
    Transition(label='Chemical Test'),
    Transition(label='Aging Verify'),
    Transition(label='Record Match'),
    Transition(label='Database Query'),
    Transition(label='Panel Review'),
    Transition(label='Forgery Risk'),
    Transition(label='Market Value'),
    Transition(label='Report Draft'),
    Transition(label='Certification'),
    Transition(label='Approval Stage'),
    Transition(label='Secure Packing'),
    Transition(label='Transport Prep')
])

root.order.add_edge(Transition(label='Provenance Check'), Transition(label='Material Scan'))
root.order.add_edge(Transition(label='Material Scan'), Transition(label='Style Compare'))
root.order.add_edge(Transition(label='Style Compare'), Transition(label='AI Imaging'))
root.order.add_edge(Transition(label='AI Imaging'), Transition(label='Chemical Test'))
root.order.add_edge(Transition(label='Chemical Test'), Transition(label='Aging Verify'))
root.order.add_edge(Transition(label='Aging Verify'), Transition(label='Record Match'))
root.order.add_edge(Transition(label='Record Match'), Transition(label='Database Query'))
root.order.add_edge(Transition(label='Database Query'), Transition(label='Panel Review'))
root.order.add_edge(Transition(label='Panel Review'), Transition(label='Forgery Risk'))
root.order.add_edge(Transition(label='Forgery Risk'), Transition(label='Market Value'))
root.order.add_edge(Transition(label='Market Value'), Transition(label='Report Draft'))
root.order.add_edge(Transition(label='Report Draft'), Transition(label='Certification'))
root.order.add_edge(Transition(label='Certification'), Transition(label='Approval Stage'))
root.order.add_edge(Transition(label='Approval Stage'), Transition(label='Secure Packing'))
root.order.add_edge(Transition(label='Secure Packing'), Transition(label='Transport Prep'))