root = StrictPartialOrder(nodes=[
    Transition('Artist Check'),
    Transition('Provenance Scan'),
    Transition('Document Review'),
    Transition('Material Test'),
    Transition('Pigment Analysis'),
    Transition('Pattern Detect'),
    Transition('Fraud Screening'),
    Transition('Legal Compliance'),
    Transition('Customs Liaison'),
    Transition('Transport Plan'),
    Transition('Condition Report'),
    Transition('Insurance Setup'),
    Transition('Exhibition Prep'),
    Transition('Final Certify'),
    Transition('Stakeholder Notify')
])

root.order.add_edge(Transition('Artist Check'), Transition('Provenance Scan'))
root.order.add_edge(Transition('Provenance Scan'), Transition('Document Review'))
root.order.add_edge(Transition('Document Review'), Transition('Material Test'))
root.order.add_edge(Transition('Material Test'), Transition('Pigment Analysis'))
root.order.add_edge(Transition('Pigment Analysis'), Transition('Pattern Detect'))
root.order.add_edge(Transition('Pattern Detect'), Transition('Fraud Screening'))
root.order.add_edge(Transition('Fraud Screening'), Transition('Legal Compliance'))
root.order.add_edge(Transition('Legal Compliance'), Transition('Customs Liaison'))
root.order.add_edge(Transition('Customs Liaison'), Transition('Transport Plan'))
root.order.add_edge(Transition('Transport Plan'), Transition('Condition Report'))
root.order.add_edge(Transition('Condition Report'), Transition('Insurance Setup'))
root.order.add_edge(Transition('Insurance Setup'), Transition('Exhibition Prep'))
root.order.add_edge(Transition('Exhibition Prep'), Transition('Final Certify'))
root.order.add_edge(Transition('Final Certify'), Transition('Stakeholder Notify'))