root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Fleet Design'),
    Transition(label='Permit Request'),
    Transition(label='Regulation Review'),
    Transition(label='Stakeholder Meet'),
    Transition(label='Route Mapping'),
    Transition(label='Traffic Sync'),
    Transition(label='Drone Assembly'),
    Transition(label='Software Setup'),
    Transition(label='Test Flight'),
    Transition(label='Data Integration'),
    Transition(label='Compliance Audit'),
    Transition(label='Emergency Plan'),
    Transition(label='Launch Prep'),
    Transition(label='Feedback Loop'),
    Transition(label='Performance Tune'),
    Transition(label='Scale Strategy')
])

root.order.add_edge(Transition(label='Site Survey'), Transition(label='Fleet Design'))
root.order.add_edge(Transition(label='Fleet Design'), Transition(label='Permit Request'))
root.order.add_edge(Transition(label='Permit Request'), Transition(label='Regulation Review'))
root.order.add_edge(Transition(label='Regulation Review'), Transition(label='Stakeholder Meet'))
root.order.add_edge(Transition(label='Stakeholder Meet'), Transition(label='Route Mapping'))
root.order.add_edge(Transition(label='Route Mapping'), Transition(label='Traffic Sync'))
root.order.add_edge(Transition(label='Traffic Sync'), Transition(label='Drone Assembly'))
root.order.add_edge(Transition(label='Drone Assembly'), Transition(label='Software Setup'))
root.order.add_edge(Transition(label='Software Setup'), Transition(label='Test Flight'))
root.order.add_edge(Transition(label='Test Flight'), Transition(label='Data Integration'))
root.order.add_edge(Transition(label='Data Integration'), Transition(label='Compliance Audit'))
root.order.add_edge(Transition(label='Compliance Audit'), Transition(label='Emergency Plan'))
root.order.add_edge(Transition(label='Emergency Plan'), Transition(label='Launch Prep'))
root.order.add_edge(Transition(label='Launch Prep'), Transition(label='Feedback Loop'))
root.order.add_edge(Transition(label='Feedback Loop'), Transition(label='Performance Tune'))
root.order.add_edge(Transition(label='Performance Tune'), Transition(label='Scale Strategy'))