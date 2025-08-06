root = StrictPartialOrder(nodes=[
    Transition(label='Client Meet'),
    Transition(label='Vision Capture'),
    Transition(label='Concept Draft'),
    Transition(label='Feedback Loop'),
    Transition(label='Material Sourcing'),
    Transition(label='Vendor Selection'),
    Transition(label='Artisan Assign'),
    Transition(label='Prototype Build'),
    Transition(label='Quality Review'),
    Transition(label='Technical Check'),
    Transition(label='Final Approval'),
    Transition(label='Packaging Prep'),
    Transition(label='Logistics Plan'),
    Transition(label='Secure Transport'),
    Transition(label='Installation Set'),
    Transition(label='Client Support'),
    Transition(label='Archival Record')
])

root.order.add_edge(Transition(label='Client Meet'), Transition(label='Vision Capture'))
root.order.add_edge(Transition(label='Vision Capture'), Transition(label='Concept Draft'))
root.order.add_edge(Transition(label='Concept Draft'), Transition(label='Feedback Loop'))
root.order.add_edge(Transition(label='Feedback Loop'), Transition(label='Concept Draft'))
root.order.add_edge(Transition(label='Feedback Loop'), Transition(label='Material Sourcing'))
root.order.add_edge(Transition(label='Material Sourcing'), Transition(label='Vendor Selection'))
root.order.add_edge(Transition(label='Vendor Selection'), Transition(label='Artisan Assign'))
root.order.add_edge(Transition(label='Artisan Assign'), Transition(label='Prototype Build'))
root.order.add_edge(Transition(label='Prototype Build'), Transition(label='Quality Review'))
root.order.add_edge(Transition(label='Quality Review'), Transition(label='Technical Check'))
root.order.add_edge(Transition(label='Technical Check'), Transition(label='Final Approval'))
root.order.add_edge(Transition(label='Final Approval'), Transition(label='Packaging Prep'))
root.order.add_edge(Transition(label='Packaging Prep'), Transition(label='Logistics Plan'))
root.order.add_edge(Transition(label='Logistics Plan'), Transition(label='Secure Transport'))
root.order.add_edge(Transition(label='Secure Transport'), Transition(label='Installation Set'))
root.order.add_edge(Transition(label='Installation Set'), Transition(label='Client Support'))
root.order.add_edge(Transition(label='Client Support'), Transition(label='Archival Record'))