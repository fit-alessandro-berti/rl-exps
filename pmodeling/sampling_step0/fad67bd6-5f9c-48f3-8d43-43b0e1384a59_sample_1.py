root = StrictPartialOrder(nodes=[
    Transition(label='Regulatory Check'),
    Transition(label='Path Design'),
    Transition(label='Weather Sync'),
    Transition(label='Traffic Align'),
    Transition(label='Package Secure'),
    Transition(label='Customer Alert'),
    Transition(label='Drone Assemble'),
    Transition(label='Flight Test'),
    Transition(label='Data Monitor'),
    Transition(label='Safety Audit'),
    Transition(label='Emergency Plan'),
    Transition(label='Maintenance Plan'),
    Transition(label='Battery Cycle'),
    Transition(label='Route Update'),
    Transition(label='Performance Review'),
    Transition(label='Impact Study'),
    Transition(label='Compliance Review')
])

root.order.add_edge(Transition(label='Regulatory Check'), Transition(label='Path Design'))
root.order.add_edge(Transition(label='Path Design'), Transition(label='Weather Sync'))
root.order.add_edge(Transition(label='Weather Sync'), Transition(label='Traffic Align'))
root.order.add_edge(Transition(label='Traffic Align'), Transition(label='Package Secure'))
root.order.add_edge(Transition(label='Package Secure'), Transition(label='Customer Alert'))
root.order.add_edge(Transition(label='Customer Alert'), Transition(label='Drone Assemble'))
root.order.add_edge(Transition(label='Drone Assemble'), Transition(label='Flight Test'))
root.order.add_edge(Transition(label='Flight Test'), Transition(label='Data Monitor'))
root.order.add_edge(Transition(label='Data Monitor'), Transition(label='Safety Audit'))
root.order.add_edge(Transition(label='Safety Audit'), Transition(label='Emergency Plan'))
root.order.add_edge(Transition(label='Emergency Plan'), Transition(label='Maintenance Plan'))
root.order.add_edge(Transition(label='Maintenance Plan'), Transition(label='Battery Cycle'))
root.order.add_edge(Transition(label='Battery Cycle'), Transition(label='Route Update'))
root.order.add_edge(Transition(label='Route Update'), Transition(label='Performance Review'))
root.order.add_edge(Transition(label='Performance Review'), Transition(label='Impact Study'))
root.order.add_edge(Transition(label='Impact Study'), Transition(label='Compliance Review'))