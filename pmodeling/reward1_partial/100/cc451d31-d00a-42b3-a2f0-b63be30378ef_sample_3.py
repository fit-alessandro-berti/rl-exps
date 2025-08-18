root = StrictPartialOrder(nodes=[
    Transition(label='Idea Solicitation'),
    Transition(label='AI Filtering'),
    Transition(label='Community Voting'),
    Transition(label='Expert Review'),
    Transition(label='Prototype Build'),
    Transition(label='User Testing'),
    Transition(label='Iterate Feedback'),
    Transition(label='Risk Assess'),
    Transition(label='Compliance Check'),
    Transition(label='Pilot Launch'),
    Transition(label='Performance Track'),
    Transition(label='Impact Analyze'),
    Transition(label='Insight Gather'),
    Transition(label='Cycle Adjust'),
    Transition(label='Final Report')
])

root.order.add_edge(Transition(label='Idea Solicitation'), Transition(label='AI Filtering'))
root.order.add_edge(Transition(label='AI Filtering'), Transition(label='Community Voting'))
root.order.add_edge(Transition(label='AI Filtering'), Transition(label='Expert Review'))
root.order.add_edge(Transition(label='Community Voting'), Transition(label='Prototype Build'))
root.order.add_edge(Transition(label='Expert Review'), Transition(label='Prototype Build'))
root.order.add_edge(Transition(label='Prototype Build'), Transition(label='User Testing'))
root.order.add_edge(Transition(label='User Testing'), Transition(label='Iterate Feedback'))
root.order.add_edge(Transition(label='Iterate Feedback'), Transition(label='Risk Assess'))
root.order.add_edge(Transition(label='Risk Assess'), Transition(label='Compliance Check'))
root.order.add_edge(Transition(label='Compliance Check'), Transition(label='Pilot Launch'))
root.order.add_edge(Transition(label='Pilot Launch'), Transition(label='Performance Track'))
root.order.add_edge(Transition(label='Performance Track'), Transition(label='Impact Analyze'))
root.order.add_edge(Transition(label='Impact Analyze'), Transition(label='Insight Gather'))
root.order.add_edge(Transition(label='Insight Gather'), Transition(label='Cycle Adjust'))
root.order.add_edge(Transition(label='Cycle Adjust'), Transition(label='Final Report'))