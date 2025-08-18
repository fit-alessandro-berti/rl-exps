root = StrictPartialOrder(nodes=[
    Transition(label='Discover Item'),
    Transition(label='Document Find'),
    Transition(label='Initial Survey'),
    Transition(label='Image Capture'),
    Transition(label='Material Testing'),
    Transition(label='Style Compare'),
    Transition(label='Expert Consult'),
    Transition(label='Provenance Check'),
    Transition(label='Ownership Verify'),
    Transition(label='Legal Review'),
    Transition(label='Risk Assess'),
    Transition(label='Conservation Plan'),
    Transition(label='Certification'),
    Transition(label='Secure Transfer'),
    Transition(label='Dispute Resolve'),
    Transition(label='Final Archive')
])

root.order.add_edge(Transition(label='Discover Item'), Transition(label='Document Find'))
root.order.add_edge(Transition(label='Document Find'), Transition(label='Initial Survey'))
root.order.add_edge(Transition(label='Initial Survey'), Transition(label='Image Capture'))
root.order.add_edge(Transition(label='Image Capture'), Transition(label='Material Testing'))
root.order.add_edge(Transition(label='Material Testing'), Transition(label='Style Compare'))
root.order.add_edge(Transition(label='Style Compare'), Transition(label='Expert Consult'))
root.order.add_edge(Transition(label='Expert Consult'), Transition(label='Provenance Check'))
root.order.add_edge(Transition(label='Provenance Check'), Transition(label='Ownership Verify'))
root.order.add_edge(Transition(label='Ownership Verify'), Transition(label='Legal Review'))
root.order.add_edge(Transition(label='Legal Review'), Transition(label='Risk Assess'))
root.order.add_edge(Transition(label='Risk Assess'), Transition(label='Conservation Plan'))
root.order.add_edge(Transition(label='Conservation Plan'), Transition(label='Certification'))
root.order.add_edge(Transition(label='Certification'), Transition(label='Secure Transfer'))
root.order.add_edge(Transition(label='Secure Transfer'), Transition(label='Dispute Resolve'))
root.order.add_edge(Transition(label='Dispute Resolve'), Transition(label='Final Archive'))