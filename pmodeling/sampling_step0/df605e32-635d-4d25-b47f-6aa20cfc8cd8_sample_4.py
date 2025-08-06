root = StrictPartialOrder(nodes=[
    Transition(label='Artifact Scan'),
    Transition(label='Ownership Verify'),
    Transition(label='Risk Assess'),
    Transition(label='Legal Review'),
    Transition(label='Stakeholder Notify'),
    Transition(label='Recovery Plan'),
    Transition(label='Third-Party Contact'),
    Transition(label='Negotiation Setup'),
    Transition(label='Secure Transport'),
    Transition(label='Condition Inspect'),
    Transition(label='Restoration Begin'),
    Transition(label='Documentation Log'),
    Transition(label='Heritage Archive'),
    Transition(label='Final Audit'),
    Transition(label='Process Close')
])

root.order.add_edge(Transition(label='Artifact Scan'), Transition(label='Ownership Verify'))
root.order.add_edge(Transition(label='Ownership Verify'), Transition(label='Risk Assess'))
root.order.add_edge(Transition(label='Risk Assess'), Transition(label='Legal Review'))
root.order.add_edge(Transition(label='Legal Review'), Transition(label='Stakeholder Notify'))
root.order.add_edge(Transition(label='Stakeholder Notify'), Transition(label='Recovery Plan'))
root.order.add_edge(Transition(label='Recovery Plan'), Transition(label='Third-Party Contact'))
root.order.add_edge(Transition(label='Third-Party Contact'), Transition(label='Negotiation Setup'))
root.order.add_edge(Transition(label='Negotiation Setup'), Transition(label='Secure Transport'))
root.order.add_edge(Transition(label='Secure Transport'), Transition(label='Condition Inspect'))
root.order.add_edge(Transition(label='Condition Inspect'), Transition(label='Restoration Begin'))
root.order.add_edge(Transition(label='Restoration Begin'), Transition(label='Documentation Log'))
root.order.add_edge(Transition(label='Documentation Log'), Transition(label='Heritage Archive'))
root.order.add_edge(Transition(label='Heritage Archive'), Transition(label='Final Audit'))
root.order.add_edge(Transition(label='Final Audit'), Transition(label='Process Close'))