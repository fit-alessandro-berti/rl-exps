root = StrictPartialOrder(nodes=[
    Transition(label='Provenance Check'),
    Transition(label='Material Scan'),
    Transition(label='Context Review'),
    Transition(label='Expert Consult'),
    Transition(label='Image Capture'),
    Transition(label='Condition Test'),
    Transition(label='Forgery Risk'),
    Transition(label='Registry Crosscheck'),
    Transition(label='Legal Verify'),
    Transition(label='Ethics Review'),
    Transition(label='Report Draft'),
    Transition(label='Certificate Issue'),
    Transition(label='Digital Archive'),
    Transition(label='Transfer Setup'),
    Transition(label='Final Approval')
])

root.order.add_edge(Transition(label='Provenance Check'), Transition(label='Material Scan'))
root.order.add_edge(Transition(label='Material Scan'), Transition(label='Context Review'))
root.order.add_edge(Transition(label='Context Review'), Transition(label='Expert Consult'))
root.order.add_edge(Transition(label='Expert Consult'), Transition(label='Image Capture'))
root.order.add_edge(Transition(label='Image Capture'), Transition(label='Condition Test'))
root.order.add_edge(Transition(label='Condition Test'), Transition(label='Forgery Risk'))
root.order.add_edge(Transition(label='Forgery Risk'), Transition(label='Registry Crosscheck'))
root.order.add_edge(Transition(label='Registry Crosscheck'), Transition(label='Legal Verify'))
root.order.add_edge(Transition(label='Legal Verify'), Transition(label='Ethics Review'))
root.order.add_edge(Transition(label='Ethics Review'), Transition(label='Report Draft'))
root.order.add_edge(Transition(label='Report Draft'), Transition(label='Certificate Issue'))
root.order.add_edge(Transition(label='Certificate Issue'), Transition(label='Digital Archive'))
root.order.add_edge(Transition(label='Digital Archive'), Transition(label='Transfer Setup'))
root.order.add_edge(Transition(label='Transfer Setup'), Transition(label='Final Approval'))