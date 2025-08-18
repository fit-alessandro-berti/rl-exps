root = StrictPartialOrder(nodes=[
    Transition(label='Trend Scan'),
    Transition(label='Opportunity Map'),
    Transition(label='Expert Gather'),
    Transition(label='Idea Sprint'),
    Transition(label='Proto Build'),
    Transition(label='User Feedback'),
    Transition(label='Risk Review'),
    Transition(label='IP Audit'),
    Transition(label='Pilot Launch'),
    Transition(label='Stakeholder Meet'),
    Transition(label='Resource Shift'),
    Transition(label='Scale Up'),
    Transition(label='Impact Assess'),
    Transition(label='Knowledge Share'),
    Transition(label='Monitor Trends')
])
root.order.add_edge(Transition(label='Trend Scan'), Transition(label='Opportunity Map'))
root.order.add_edge(Transition(label='Trend Scan'), Transition(label='Expert Gather'))
root.order.add_edge(Transition(label='Opportunity Map'), Transition(label='Idea Sprint'))
root.order.add_edge(Transition(label='Expert Gather'), Transition(label='Idea Sprint'))
root.order.add_edge(Transition(label='Idea Sprint'), Transition(label='Proto Build'))
root.order.add_edge(Transition(label='Proto Build'), Transition(label='User Feedback'))
root.order.add_edge(Transition(label='User Feedback'), Transition(label='Risk Review'))
root.order.add_edge(Transition(label='Risk Review'), Transition(label='IP Audit'))
root.order.add_edge(Transition(label='IP Audit'), Transition(label='Pilot Launch'))
root.order.add_edge(Transition(label='Pilot Launch'), Transition(label='Stakeholder Meet'))
root.order.add_edge(Transition(label='Stakeholder Meet'), Transition(label='Resource Shift'))
root.order.add_edge(Transition(label='Resource Shift'), Transition(label='Scale Up'))
root.order.add_edge(Transition(label='Scale Up'), Transition(label='Impact Assess'))
root.order.add_edge(Transition(label='Impact Assess'), Transition(label='Knowledge Share'))
root.order.add_edge(Transition(label='Knowledge Share'), Transition(label='Monitor Trends'))