root = StrictPartialOrder(nodes=[
    Transition(label='Trend Scan'),
    Transition(label='Idea Sprint'),
    Transition(label='Feasibility Check'),
    Transition(label='Risk Review'),
    Transition(label='Tech Prototype'),
    Transition(label='Market Simulate'),
    Transition(label='Stakeholder Align'),
    Transition(label='Budget Adjust'),
    Transition(label='Talent Source'),
    Transition(label='Pilot Launch'),
    Transition(label='Data Refine'),
    Transition(label='Scale Analysis'),
    Transition(label='Integration Plan'),
    Transition(label='Change Manage'),
    Transition(label='Knowledge Transfer')
])

root.order.add_edge(Transition(label='Trend Scan'), Transition(label='Idea Sprint'))
root.order.add_edge(Transition(label='Idea Sprint'), Transition(label='Feasibility Check'))
root.order.add_edge(Transition(label='Feasibility Check'), Transition(label='Risk Review'))
root.order.add_edge(Transition(label='Risk Review'), Transition(label='Tech Prototype'))
root.order.add_edge(Transition(label='Tech Prototype'), Transition(label='Market Simulate'))
root.order.add_edge(Transition(label='Market Simulate'), Transition(label='Stakeholder Align'))
root.order.add_edge(Transition(label='Stakeholder Align'), Transition(label='Budget Adjust'))
root.order.add_edge(Transition(label='Budget Adjust'), Transition(label='Talent Source'))
root.order.add_edge(Transition(label='Talent Source'), Transition(label='Pilot Launch'))
root.order.add_edge(Transition(label='Pilot Launch'), Transition(label='Data Refine'))
root.order.add_edge(Transition(label='Data Refine'), Transition(label='Scale Analysis'))
root.order.add_edge(Transition(label='Scale Analysis'), Transition(label='Integration Plan'))
root.order.add_edge(Transition(label='Integration Plan'), Transition(label='Change Manage'))
root.order.add_edge(Transition(label='Change Manage'), Transition(label='Knowledge Transfer'))