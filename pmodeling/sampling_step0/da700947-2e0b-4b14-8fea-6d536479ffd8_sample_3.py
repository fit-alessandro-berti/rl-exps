root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Structural Audit'),
    Transition(label='Climate Design'),
    Transition(label='Lighting Setup'),
    Transition(label='Irrigation Plan'),
    Transition(label='Nutrient Mix'),
    Transition(label='Sensor Install'),
    Transition(label='AI Calibration'),
    Transition(label='Pest Scan'),
    Transition(label='Energy Audit'),
    Transition(label='Renewable Sync'),
    Transition(label='Data Modeling'),
    Transition(label='Staff Briefing'),
    Transition(label='Compliance Check'),
    Transition(label='Community Meet'),
    Transition(label='Yield Review'),
    Transition(label='Feedback Loop')
])
root.order.add_edge(Transition(label='Site Survey'), Transition(label='Structural Audit'))
root.order.add_edge(Transition(label='Structural Audit'), Transition(label='Climate Design'))
root.order.add_edge(Transition(label='Climate Design'), Transition(label='Lighting Setup'))
root.order.add_edge(Transition(label='Lighting Setup'), Transition(label='Irrigation Plan'))
root.order.add_edge(Transition(label='Irrigation Plan'), Transition(label='Nutrient Mix'))
root.order.add_edge(Transition(label='Nutrient Mix'), Transition(label='Sensor Install'))
root.order.add_edge(Transition(label='Sensor Install'), Transition(label='AI Calibration'))
root.order.add_edge(Transition(label='AI Calibration'), Transition(label='Pest Scan'))
root.order.add_edge(Transition(label='Pest Scan'), Transition(label='Energy Audit'))
root.order.add_edge(Transition(label='Energy Audit'), Transition(label='Renewable Sync'))
root.order.add_edge(Transition(label='Renewable Sync'), Transition(label='Data Modeling'))
root.order.add_edge(Transition(label='Data Modeling'), Transition(label='Staff Briefing'))
root.order.add_edge(Transition(label='Staff Briefing'), Transition(label='Compliance Check'))
root.order.add_edge(Transition(label='Compliance Check'), Transition(label='Community Meet'))
root.order.add_edge(Transition(label='Community Meet'), Transition(label='Yield Review'))
root.order.add_edge(Transition(label='Yield Review'), Transition(label='Feedback Loop'))