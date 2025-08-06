root = StrictPartialOrder(nodes=[
    Transition(label='Artifact Intake'),
    Transition(label='Provenance Check'),
    Transition(label='Material Testing'),
    Transition(label='Historical Review'),
    Transition(label='Expert Interview'),
    Transition(label='Condition Audit'),
    Transition(label='Digital Catalog'),
    Transition(label='Forgery Detection'),
    Transition(label='Legal Compliance'),
    Transition(label='Restoration Plan'),
    Transition(label='Valuation Report'),
    Transition(label='Market Analysis'),
    Transition(label='Final Approval'),
    Transition(label='Sale Preparation'),
    Transition(label='Client Notification')
])

root.order.add_edge(Transition(label='Artifact Intake'), Transition(label='Provenance Check'))
root.order.add_edge(Transition(label='Provenance Check'), Transition(label='Material Testing'))
root.order.add_edge(Transition(label='Material Testing'), Transition(label='Historical Review'))
root.order.add_edge(Transition(label='Historical Review'), Transition(label='Expert Interview'))
root.order.add_edge(Transition(label='Expert Interview'), Transition(label='Condition Audit'))
root.order.add_edge(Transition(label='Condition Audit'), Transition(label='Digital Catalog'))
root.order.add_edge(Transition(label='Digital Catalog'), Transition(label='Forgery Detection'))
root.order.add_edge(Transition(label='Forgery Detection'), Transition(label='Legal Compliance'))
root.order.add_edge(Transition(label='Legal Compliance'), Transition(label='Restoration Plan'))
root.order.add_edge(Transition(label='Restoration Plan'), Transition(label='Valuation Report'))
root.order.add_edge(Transition(label='Valuation Report'), Transition(label='Market Analysis'))
root.order.add_edge(Transition(label='Market Analysis'), Transition(label='Final Approval'))
root.order.add_edge(Transition(label='Final Approval'), Transition(label='Sale Preparation'))
root.order.add_edge(Transition(label='Sale Preparation'), Transition(label='Client Notification'))