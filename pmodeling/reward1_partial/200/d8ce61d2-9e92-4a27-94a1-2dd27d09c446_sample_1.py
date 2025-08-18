root = StrictPartialOrder(nodes=[
    Transition(label='Initial Audit'),
    Transition(label='Artist Review'),
    Transition(label='Material Check'),
    Transition(label='Condition Scan'),
    Transition(label='Ownership Verify'),
    Transition(label='Appraisal Update'),
    Transition(label='Restoration Plan'),
    Transition(label='Restoration Track'),
    Transition(label='Logistics Book'),
    Transition(label='Shipping Monitor'),
    Transition(label='Customs Clear'),
    Transition(label='Legal Compliance'),
    Transition(label='Ledger Update'),
    Transition(label='Exhibition Setup'),
    Transition(label='Public Showcase'),
    Transition(label='Archival Prep'),
    Transition(label='Final Report')
])

root.order.add_edge(Transition(label='Initial Audit'), Transition(label='Artist Review'))
root.order.add_edge(Transition(label='Artist Review'), Transition(label='Material Check'))
root.order.add_edge(Transition(label='Material Check'), Transition(label='Condition Scan'))
root.order.add_edge(Transition(label='Condition Scan'), Transition(label='Ownership Verify'))
root.order.add_edge(Transition(label='Ownership Verify'), Transition(label='Appraisal Update'))
root.order.add_edge(Transition(label='Appraisal Update'), Transition(label='Restoration Plan'))
root.order.add_edge(Transition(label='Restoration Plan'), Transition(label='Restoration Track'))
root.order.add_edge(Transition(label='Restoration Track'), Transition(label='Logistics Book'))
root.order.add_edge(Transition(label='Logistics Book'), Transition(label='Shipping Monitor'))
root.order.add_edge(Transition(label='Shipping Monitor'), Transition(label='Customs Clear'))
root.order.add_edge(Transition(label='Customs Clear'), Transition(label='Legal Compliance'))
root.order.add_edge(Transition(label='Legal Compliance'), Transition(label='Ledger Update'))
root.order.add_edge(Transition(label='Ledger Update'), Transition(label='Exhibition Setup'))
root.order.add_edge(Transition(label='Exhibition Setup'), Transition(label='Public Showcase'))
root.order.add_edge(Transition(label='Public Showcase'), Transition(label='Archival Prep'))
root.order.add_edge(Transition(label='Archival Prep'), Transition(label='Final Report'))