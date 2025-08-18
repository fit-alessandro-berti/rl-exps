root = StrictPartialOrder(nodes=[
    Transition(label='Artist Check'),
    Transition(label='Provenance Scan'),
    Transition(label='Document Review'),
    Transition(label='Material Test'),
    Transition(label='Pigment Analysis'),
    Transition(label='Pattern Detect'),
    Transition(label='Fraud Screening'),
    Transition(label='Legal Compliance'),
    Transition(label='Customs Liaison'),
    Transition(label='Transport Plan'),
    Transition(label='Condition Report'),
    Transition(label='Insurance Setup'),
    Transition(label='Exhibition Prep'),
    Transition(label='Final Certify'),
    Transition(label='Stakeholder Notify')
])

# Define the dependencies
root.order.add_edge(Transition(label='Artist Check'), Transition(label='Provenance Scan'))
root.order.add_edge(Transition(label='Provenance Scan'), Transition(label='Document Review'))
root.order.add_edge(Transition(label='Document Review'), Transition(label='Material Test'))
root.order.add_edge(Transition(label='Material Test'), Transition(label='Pigment Analysis'))
root.order.add_edge(Transition(label='Pigment Analysis'), Transition(label='Pattern Detect'))
root.order.add_edge(Transition(label='Pattern Detect'), Transition(label='Fraud Screening'))
root.order.add_edge(Transition(label='Fraud Screening'), Transition(label='Legal Compliance'))
root.order.add_edge(Transition(label='Legal Compliance'), Transition(label='Customs Liaison'))
root.order.add_edge(Transition(label='Customs Liaison'), Transition(label='Transport Plan'))
root.order.add_edge(Transition(label='Transport Plan'), Transition(label='Condition Report'))
root.order.add_edge(Transition(label='Condition Report'), Transition(label='Insurance Setup'))
root.order.add_edge(Transition(label='Insurance Setup'), Transition(label='Exhibition Prep'))
root.order.add_edge(Transition(label='Exhibition Prep'), Transition(label='Final Certify'))
root.order.add_edge(Transition(label='Final Certify'), Transition(label='Stakeholder Notify'))