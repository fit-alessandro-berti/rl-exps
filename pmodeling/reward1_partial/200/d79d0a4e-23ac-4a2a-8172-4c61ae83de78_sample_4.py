root = StrictPartialOrder(nodes=[
    Transition(label='Spec Review'),
    Transition(label='Component Pick'),
    Transition(label='Frame Build'),
    Transition(label='Motor Mount'),
    Transition(label='Sensor Fit'),
    Transition(label='Wiring Setup'),
    Transition(label='Software Load'),
    Transition(label='Calibration Test'),
    Transition(label='Stress Check'),
    Transition(label='Firmware Flash'),
    Transition(label='Feedback Loop'),
    Transition(label='Package Prep'),
    Transition(label='Doc Compile'),
    Transition(label='Ship Arrange'),
    Transition(label='Remote Setup')
])

# Define the order of execution
root.order.add_edge(Transition(label='Spec Review'), Transition(label='Component Pick'))
root.order.add_edge(Transition(label='Component Pick'), Transition(label='Frame Build'))
root.order.add_edge(Transition(label='Frame Build'), Transition(label='Motor Mount'))
root.order.add_edge(Transition(label='Motor Mount'), Transition(label='Sensor Fit'))
root.order.add_edge(Transition(label='Sensor Fit'), Transition(label='Wiring Setup'))
root.order.add_edge(Transition(label='Wiring Setup'), Transition(label='Software Load'))
root.order.add_edge(Transition(label='Software Load'), Transition(label='Calibration Test'))
root.order.add_edge(Transition(label='Calibration Test'), Transition(label='Stress Check'))
root.order.add_edge(Transition(label='Stress Check'), Transition(label='Firmware Flash'))
root.order.add_edge(Transition(label='Firmware Flash'), Transition(label='Feedback Loop'))
root.order.add_edge(Transition(label='Feedback Loop'), Transition(label='Package Prep'))
root.order.add_edge(Transition(label='Package Prep'), Transition(label='Doc Compile'))
root.order.add_edge(Transition(label='Doc Compile'), Transition(label='Ship Arrange'))
root.order.add_edge(Transition(label='Ship Arrange'), Transition(label='Remote Setup'))