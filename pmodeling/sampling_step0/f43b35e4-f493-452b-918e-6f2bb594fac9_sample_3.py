root = StrictPartialOrder(nodes=[
    Transition(label='Client Brief'),
    Transition(label='Design Draft'),
    Transition(label='Part Sourcing'),
    Transition(label='Component Fabric'),
    Transition(label='Circuit Assembly'),
    Transition(label='Software Upload'),
    Transition(label='Initial Testing'),
    Transition(label='Flight Calibrate'),
    Transition(label='Payload Mount'),
    Transition(label='Stress Testing'),
    Transition(label='Feedback Loop'),
    Transition(label='Quality Check'),
    Transition(label='Certification'),
    Transition(label='Packaging'),
    Transition(label='Delivery Plan'),
    Transition(label='Post Support')
])

root.order.add_edge(Transition(label='Client Brief'), Transition(label='Design Draft'))
root.order.add_edge(Transition(label='Design Draft'), Transition(label='Part Sourcing'))
root.order.add_edge(Transition(label='Part Sourcing'), Transition(label='Component Fabric'))
root.order.add_edge(Transition(label='Component Fabric'), Transition(label='Circuit Assembly'))
root.order.add_edge(Transition(label='Circuit Assembly'), Transition(label='Software Upload'))
root.order.add_edge(Transition(label='Software Upload'), Transition(label='Initial Testing'))
root.order.add_edge(Transition(label='Initial Testing'), Transition(label='Flight Calibrate'))
root.order.add_edge(Transition(label='Flight Calibrate'), Transition(label='Payload Mount'))
root.order.add_edge(Transition(label='Payload Mount'), Transition(label='Stress Testing'))
root.order.add_edge(Transition(label='Stress Testing'), Transition(label='Feedback Loop'))
root.order.add_edge(Transition(label='Feedback Loop'), Transition(label='Quality Check'))
root.order.add_edge(Transition(label='Quality Check'), Transition(label='Certification'))
root.order.add_edge(Transition(label='Certification'), Transition(label='Packaging'))
root.order.add_edge(Transition(label='Packaging'), Transition(label='Delivery Plan'))
root.order.add_edge(Transition(label='Delivery Plan'), Transition(label='Post Support'))