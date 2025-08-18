root = StrictPartialOrder(nodes=[
    Transition(label='Trend Sensing'),
    Transition(label='Idea Fusion'),
    Transition(label='Prototype Build'),
    Transition(label='Expert Review'),
    Transition(label='Field Testing'),
    Transition(label='IP Analysis'),
    Transition(label='Compliance Check'),
    Transition(label='Partner Setup'),
    Transition(label='User Profiling'),
    Transition(label='Launch Prep'),
    Transition(label='Feedback Loop'),
    Transition(label='Scale Planning'),
    Transition(label='Risk Assess'),
    Transition(label='Demand Scan'),
    Transition(label='Agile Adjust')
])

root.order.add_edge(Transition(label='Trend Sensing'), Transition(label='Idea Fusion'))
root.order.add_edge(Transition(label='Idea Fusion'), Transition(label='Prototype Build'))
root.order.add_edge(Transition(label='Prototype Build'), Transition(label='Expert Review'))
root.order.add_edge(Transition(label='Expert Review'), Transition(label='Field Testing'))
root.order.add_edge(Transition(label='Field Testing'), Transition(label='IP Analysis'))
root.order.add_edge(Transition(label='IP Analysis'), Transition(label='Compliance Check'))
root.order.add_edge(Transition(label='Compliance Check'), Transition(label='Partner Setup'))
root.order.add_edge(Transition(label='Partner Setup'), Transition(label='User Profiling'))
root.order.add_edge(Transition(label='User Profiling'), Transition(label='Launch Prep'))
root.order.add_edge(Transition(label='Launch Prep'), Transition(label='Feedback Loop'))
root.order.add_edge(Transition(label='Feedback Loop'), Transition(label='Scale Planning'))
root.order.add_edge(Transition(label='Scale Planning'), Transition(label='Risk Assess'))
root.order.add_edge(Transition(label='Risk Assess'), Transition(label='Demand Scan'))
root.order.add_edge(Transition(label='Demand Scan'), Transition(label='Agile Adjust'))