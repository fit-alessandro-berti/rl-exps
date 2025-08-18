root = StrictPartialOrder(nodes=[
    Transition(label='Intel Gathering'),
    Transition(label='Risk Assess'),
    Transition(label='Behavior Scan'),
    Transition(label='Network Monitor'),
    Transition(label='Audit Conduct'),
    Transition(label='Flag Suspicion'),
    Transition(label='Legal Review'),
    Transition(label='Compliance Check'),
    Transition(label='Employee Train'),
    Transition(label='Threat Simulate'),
    Transition(label='Incident Plan'),
    Transition(label='Response Drill'),
    Transition(label='Data Encrypt'),
    Transition(label='Partner Liaison'),
    Transition(label='Report Generate'),
    Transition(label='Feedback Loop')
])

root.order.add_edge(Transition(label='Intel Gathering'), Transition(label='Risk Assess'))
root.order.add_edge(Transition(label='Risk Assess'), Transition(label='Behavior Scan'))
root.order.add_edge(Transition(label='Behavior Scan'), Transition(label='Network Monitor'))
root.order.add_edge(Transition(label='Network Monitor'), Transition(label='Audit Conduct'))
root.order.add_edge(Transition(label='Audit Conduct'), Transition(label='Flag Suspicion'))
root.order.add_edge(Transition(label='Flag Suspicion'), Transition(label='Legal Review'))
root.order.add_edge(Transition(label='Legal Review'), Transition(label='Compliance Check'))
root.order.add_edge(Transition(label='Compliance Check'), Transition(label='Employee Train'))
root.order.add_edge(Transition(label='Employee Train'), Transition(label='Threat Simulate'))
root.order.add_edge(Transition(label='Threat Simulate'), Transition(label='Incident Plan'))
root.order.add_edge(Transition(label='Incident Plan'), Transition(label='Response Drill'))
root.order.add_edge(Transition(label='Response Drill'), Transition(label='Data Encrypt'))
root.order.add_edge(Transition(label='Data Encrypt'), Transition(label='Partner Liaison'))
root.order.add_edge(Transition(label='Partner Liaison'), Transition(label='Report Generate'))
root.order.add_edge(Transition(label='Report Generate'), Transition(label='Feedback Loop'))