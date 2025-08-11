root = StrictPartialOrder(nodes=[
    Transition(label='Initial Review'),
    Transition(label='Provenance Check'),
    Transition(label='Material Testing'),
    Transition(label='Expert Survey'),
    Transition(label='Digital Scan'),
    Transition(label='Condition Report'),
    Transition(label='Legal Review'),
    Transition(label='Risk Analysis'),
    Transition(label='Seller Negotiation'),
    Transition(label='Documentation'),
    Transition(label='Archival Entry'),
    Transition(label='Committee Review'),
    Transition(label='Final Approval'),
    Transition(label='Acquisition Setup'),
    Transition(label='Exhibit Planning')
])
root.order.add_edge(Transition(label='Initial Review'), Transition(label='Provenance Check'))
root.order.add_edge(Transition(label='Provenance Check'), Transition(label='Material Testing'))
root.order.add_edge(Transition(label='Material Testing'), Transition(label='Expert Survey'))
root.order.add_edge(Transition(label='Expert Survey'), Transition(label='Digital Scan'))
root.order.add_edge(Transition(label='Digital Scan'), Transition(label='Condition Report'))
root.order.add_edge(Transition(label='Condition Report'), Transition(label='Legal Review'))
root.order.add_edge(Transition(label='Legal Review'), Transition(label='Risk Analysis'))
root.order.add_edge(Transition(label='Risk Analysis'), Transition(label='Seller Negotiation'))
root.order.add_edge(Transition(label='Seller Negotiation'), Transition(label='Documentation'))
root.order.add_edge(Transition(label='Documentation'), Transition(label='Archival Entry'))
root.order.add_edge(Transition(label='Archival Entry'), Transition(label='Committee Review'))
root.order.add_edge(Transition(label='Committee Review'), Transition(label='Final Approval'))
root.order.add_edge(Transition(label='Final Approval'), Transition(label='Acquisition Setup'))
root.order.add_edge(Transition(label='Acquisition Setup'), Transition(label='Exhibit Planning'))