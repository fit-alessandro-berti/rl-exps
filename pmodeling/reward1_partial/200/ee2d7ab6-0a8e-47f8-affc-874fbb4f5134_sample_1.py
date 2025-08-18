root = StrictPartialOrder(nodes=[
    Transition(label='Client Consult'),
    Transition(label='Spec Gathering'),
    Transition(label='Supplier Sourcing'),
    Transition(label='Design Review'),
    Transition(label='Simulation Test'),
    Transition(label='Proto Assembly'),
    Transition(label='Quality Check'),
    Transition(label='Firmware Flash'),
    Transition(label='Sensor Install'),
    Transition(label='Final Testing'),
    Transition(label='Brand Packaging'),
    Transition(label='Shipping Prep'),
    Transition(label='Delivery Schedule'),
    Transition(label='Client Training'),
    Transition(label='Diagnostics Setup')
])

root.order.add_edge(Transition('Client Consult'), Transition('Spec Gathering'))
root.order.add_edge(Transition('Spec Gathering'), Transition('Supplier Sourcing'))
root.order.add_edge(Transition('Supplier Sourcing'), Transition('Design Review'))
root.order.add_edge(Transition('Design Review'), Transition('Simulation Test'))
root.order.add_edge(Transition('Simulation Test'), Transition('Proto Assembly'))
root.order.add_edge(Transition('Proto Assembly'), Transition('Quality Check'))
root.order.add_edge(Transition('Quality Check'), Transition('Firmware Flash'))
root.order.add_edge(Transition('Firmware Flash'), Transition('Sensor Install'))
root.order.add_edge(Transition('Sensor Install'), Transition('Final Testing'))
root.order.add_edge(Transition('Final Testing'), Transition('Brand Packaging'))
root.order.add_edge(Transition('Brand Packaging'), Transition('Shipping Prep'))
root.order.add_edge(Transition('Shipping Prep'), Transition('Delivery Schedule'))
root.order.add_edge(Transition('Delivery Schedule'), Transition('Client Training'))
root.order.add_edge(Transition('Client Training'), Transition('Diagnostics Setup'))