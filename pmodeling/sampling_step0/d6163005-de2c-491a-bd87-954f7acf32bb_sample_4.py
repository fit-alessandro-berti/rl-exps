root = StrictPartialOrder(nodes=[
    Transition(label='Requirement Analysis'),
    Transition(label='Component Sourcing'),
    Transition(label='Quality Check'),
    Transition(label='Frame Assembly'),
    Transition(label='Motor Installation'),
    Transition(label='Sensor Setup'),
    Transition(label='Control Unit'),
    Transition(label='Firmware Upload'),
    Transition(label='System Calibration'),
    Transition(label='Flight Testing'),
    Transition(label='Error Correction'),
    Transition(label='Cosmetic Finish'),
    Transition(label='Packaging Prep'),
    Transition(label='User Manual'),
    Transition(label='Client Training'),
    Transition(label='Support Scheduling')
])

# Define transitions
root.order.add_edge(Transition(label='Requirement Analysis'), Transition(label='Component Sourcing'))
root.order.add_edge(Transition(label='Component Sourcing'), Transition(label='Quality Check'))
root.order.add_edge(Transition(label='Quality Check'), Transition(label='Frame Assembly'))
root.order.add_edge(Transition(label='Frame Assembly'), Transition(label='Motor Installation'))
root.order.add_edge(Transition(label='Motor Installation'), Transition(label='Sensor Setup'))
root.order.add_edge(Transition(label='Sensor Setup'), Transition(label='Control Unit'))
root.order.add_edge(Transition(label='Control Unit'), Transition(label='Firmware Upload'))
root.order.add_edge(Transition(label='Firmware Upload'), Transition(label='System Calibration'))
root.order.add_edge(Transition(label='System Calibration'), Transition(label='Flight Testing'))
root.order.add_edge(Transition(label='Flight Testing'), Transition(label='Error Correction'))
root.order.add_edge(Transition(label='Error Correction'), Transition(label='Cosmetic Finish'))
root.order.add_edge(Transition(label='Cosmetic Finish'), Transition(label='Packaging Prep'))
root.order.add_edge(Transition(label='Packaging Prep'), Transition(label='User Manual'))
root.order.add_edge(Transition(label='User Manual'), Transition(label='Client Training'))
root.order.add_edge(Transition(label='Client Training'), Transition(label='Support Scheduling'))