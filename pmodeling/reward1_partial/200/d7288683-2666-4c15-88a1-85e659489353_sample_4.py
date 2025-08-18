root = StrictPartialOrder(nodes=[
    Transition(label='Component Sourcing'),
    Transition(label='Frame Assembly'),
    Transition(label='Motor Installation'),
    Transition(label='Sensor Mounting'),
    Transition(label='Wiring Setup'),
    Transition(label='Firmware Upload'),
    Transition(label='AI Module'),
    Transition(label='Calibration Phase'),
    Transition(label='Stress Testing'),
    Transition(label='Flight Simulation'),
    Transition(label='Pattern Adjustment'),
    Transition(label='Quality Inspect'),
    Transition(label='Compliance Check'),
    Transition(label='Packaging Final'),
    Transition(label='Delivery Setup')
])
root.order.add_edge(Transition(label='Component Sourcing'), Transition(label='Frame Assembly'))
root.order.add_edge(Transition(label='Frame Assembly'), Transition(label='Motor Installation'))
root.order.add_edge(Transition(label='Motor Installation'), Transition(label='Sensor Mounting'))
root.order.add_edge(Transition(label='Sensor Mounting'), Transition(label='Wiring Setup'))
root.order.add_edge(Transition(label='Wiring Setup'), Transition(label='Firmware Upload'))
root.order.add_edge(Transition(label='Firmware Upload'), Transition(label='AI Module'))
root.order.add_edge(Transition(label='AI Module'), Transition(label='Calibration Phase'))
root.order.add_edge(Transition(label='Calibration Phase'), Transition(label='Stress Testing'))
root.order.add_edge(Transition(label='Stress Testing'), Transition(label='Flight Simulation'))
root.order.add_edge(Transition(label='Flight Simulation'), Transition(label='Pattern Adjustment'))
root.order.add_edge(Transition(label='Pattern Adjustment'), Transition(label='Quality Inspect'))
root.order.add_edge(Transition(label='Quality Inspect'), Transition(label='Compliance Check'))
root.order.add_edge(Transition(label='Compliance Check'), Transition(label='Packaging Final'))
root.order.add_edge(Transition(label='Packaging Final'), Transition(label='Delivery Setup'))