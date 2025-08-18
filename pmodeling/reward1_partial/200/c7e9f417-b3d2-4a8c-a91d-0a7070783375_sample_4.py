root = StrictPartialOrder(nodes=[
    Transition(label='Brand Audit'),
    Transition(label='Equity Review'),
    Transition(label='Market Analysis'),
    Transition(label='Legal Clearance'),
    Transition(label='Trademark Check'),
    Transition(label='Portfolio Merge'),
    Transition(label='Customer Sync'),
    Transition(label='Cultural Align'),
    Transition(label='Internal Brief'),
    Transition(label='Campaign Design'),
    Transition(label='Resource Plan'),
    Transition(label='Stakeholder Meet'),
    Transition(label='Launch Prep'),
    Transition(label='Feedback Loop'),
    Transition(label='Performance Track')
])

root.order.add_edge(Transition(label='Brand Audit'), Transition(label='Equity Review'))
root.order.add_edge(Transition(label='Equity Review'), Transition(label='Market Analysis'))
root.order.add_edge(Transition(label='Market Analysis'), Transition(label='Legal Clearance'))
root.order.add_edge(Transition(label='Legal Clearance'), Transition(label='Trademark Check'))
root.order.add_edge(Transition(label='Trademark Check'), Transition(label='Portfolio Merge'))
root.order.add_edge(Transition(label='Portfolio Merge'), Transition(label='Customer Sync'))
root.order.add_edge(Transition(label='Customer Sync'), Transition(label='Cultural Align'))
root.order.add_edge(Transition(label='Cultural Align'), Transition(label='Internal Brief'))
root.order.add_edge(Transition(label='Internal Brief'), Transition(label='Campaign Design'))
root.order.add_edge(Transition(label='Campaign Design'), Transition(label='Resource Plan'))
root.order.add_edge(Transition(label='Resource Plan'), Transition(label='Stakeholder Meet'))
root.order.add_edge(Transition(label='Stakeholder Meet'), Transition(label='Launch Prep'))
root.order.add_edge(Transition(label='Launch Prep'), Transition(label='Feedback Loop'))
root.order.add_edge(Transition(label='Feedback Loop'), Transition(label='Performance Track'))