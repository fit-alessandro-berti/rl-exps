root = StrictPartialOrder(nodes=[
    Transition(label='Artifact Intake'),
    Transition(label='Condition Check'),
    Transition(label='Provenance Research'),
    Transition(label='Scientific Testing'),
    Transition(label='Radiocarbon Dating'),
    Transition(label='Spectroscopy Scan'),
    Transition(label='Legal Clearance'),
    Transition(label='Heritage Compliance'),
    Transition(label='Digital Archiving'),
    Transition(label='Expert Review'),
    Transition(label='Committee Vote'),
    Transition(label='Acquisition Approval'),
    Transition(label='Conservation Plan'),
    Transition(label='Storage Setup'),
    Transition(label='Stakeholder Update')
])

root.order.add_edge(Transition(label='Artifact Intake'), Transition(label='Condition Check'))
root.order.add_edge(Transition(label='Condition Check'), Transition(label='Provenance Research'))
root.order.add_edge(Transition(label='Provenance Research'), Transition(label='Scientific Testing'))
root.order.add_edge(Transition(label='Scientific Testing'), Transition(label='Radiocarbon Dating'))
root.order.add_edge(Transition(label='Radiocarbon Dating'), Transition(label='Spectroscopy Scan'))
root.order.add_edge(Transition(label='Spectroscopy Scan'), Transition(label='Legal Clearance'))
root.order.add_edge(Transition(label='Legal Clearance'), Transition(label='Heritage Compliance'))
root.order.add_edge(Transition(label='Heritage Compliance'), Transition(label='Digital Archiving'))
root.order.add_edge(Transition(label='Digital Archiving'), Transition(label='Expert Review'))
root.order.add_edge(Transition(label='Expert Review'), Transition(label='Committee Vote'))
root.order.add_edge(Transition(label='Committee Vote'), Transition(label='Acquisition Approval'))
root.order.add_edge(Transition(label='Acquisition Approval'), Transition(label='Conservation Plan'))
root.order.add_edge(Transition(label='Conservation Plan'), Transition(label='Storage Setup'))
root.order.add_edge(Transition(label='Storage Setup'), Transition(label='Stakeholder Update'))