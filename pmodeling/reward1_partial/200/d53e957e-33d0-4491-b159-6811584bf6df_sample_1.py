root = StrictPartialOrder(nodes=[
    Transition(label='Data Capture'),
    Transition(label='Trend Scan'),
    Transition(label='Idea Workshop'),
    Transition(label='Concept Draft'),
    Transition(label='Expert Review'),
    Transition(label='Prototype Build'),
    Transition(label='Regulation Check'),
    Transition(label='IP Alignment'),
    Transition(label='Supply Sync'),
    Transition(label='Market Mapping'),
    Transition(label='Pilot Launch'),
    Transition(label='Feedback Loop'),
    Transition(label='Design Iterate'),
    Transition(label='Impact Measure'),
    Transition(label='Strategy Adapt')
])

root.order.add_edge(Transition(label='Data Capture'), Transition(label='Trend Scan'))
root.order.add_edge(Transition(label='Trend Scan'), Transition(label='Idea Workshop'))
root.order.add_edge(Transition(label='Idea Workshop'), Transition(label='Concept Draft'))
root.order.add_edge(Transition(label='Concept Draft'), Transition(label='Expert Review'))
root.order.add_edge(Transition(label='Expert Review'), Transition(label='Prototype Build'))
root.order.add_edge(Transition(label='Prototype Build'), Transition(label='Regulation Check'))
root.order.add_edge(Transition(label='Regulation Check'), Transition(label='IP Alignment'))
root.order.add_edge(Transition(label='IP Alignment'), Transition(label='Supply Sync'))
root.order.add_edge(Transition(label='Supply Sync'), Transition(label='Market Mapping'))
root.order.add_edge(Transition(label='Market Mapping'), Transition(label='Pilot Launch'))
root.order.add_edge(Transition(label='Pilot Launch'), Transition(label='Feedback Loop'))
root.order.add_edge(Transition(label='Feedback Loop'), Transition(label='Design Iterate'))
root.order.add_edge(Transition(label='Design Iterate'), Transition(label='Impact Measure'))
root.order.add_edge(Transition(label='Impact Measure'), Transition(label='Strategy Adapt'))