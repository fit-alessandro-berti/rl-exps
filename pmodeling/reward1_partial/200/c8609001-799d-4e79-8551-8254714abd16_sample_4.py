root = StrictPartialOrder(nodes=[
    Transition(label='Initial Review'),
    Transition(label='Provenance Check'),
    Transition(label='Material Test'),
    Transition(label='Expert Consult'),
    Transition(label='Database Search'),
    Transition(label='Condition Report'),
    Transition(label='Risk Assess'),
    Transition(label='Market Analysis'),
    Transition(label='Stakeholder Meet'),
    Transition(label='Legal Review'),
    Transition(label='Insurance Quote'),
    Transition(label='Price Negotiation'),
    Transition(label='Contract Draft'),
    Transition(label='Final Approval'),
    Transition(label='Asset Registration')
])

root.order.add_edge(Transition(label='Initial Review'), Transition(label='Provenance Check'))
root.order.add_edge(Transition(label='Initial Review'), Transition(label='Material Test'))
root.order.add_edge(Transition(label='Provenance Check'), Transition(label='Expert Consult'))
root.order.add_edge(Transition(label='Provenance Check'), Transition(label='Database Search'))
root.order.add_edge(Transition(label='Material Test'), Transition(label='Expert Consult'))
root.order.add_edge(Transition(label='Material Test'), Transition(label='Database Search'))
root.order.add_edge(Transition(label='Expert Consult'), Transition(label='Condition Report'))
root.order.add_edge(Transition(label='Database Search'), Transition(label='Condition Report'))
root.order.add_edge(Transition(label='Condition Report'), Transition(label='Risk Assess'))
root.order.add_edge(Transition(label='Risk Assess'), Transition(label='Market Analysis'))
root.order.add_edge(Transition(label='Market Analysis'), Transition(label='Stakeholder Meet'))
root.order.add_edge(Transition(label='Stakeholder Meet'), Transition(label='Legal Review'))
root.order.add_edge(Transition(label='Legal Review'), Transition(label='Insurance Quote'))
root.order.add_edge(Transition(label='Insurance Quote'), Transition(label='Price Negotiation'))
root.order.add_edge(Transition(label='Price Negotiation'), Transition(label='Contract Draft'))
root.order.add_edge(Transition(label='Contract Draft'), Transition(label='Final Approval'))
root.order.add_edge(Transition(label='Final Approval'), Transition(label='Asset Registration'))