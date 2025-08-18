root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Light Mapping'),
    Transition(label='Water Testing'),
    Transition(label='Design Modules'),
    Transition(label='IoT Setup'),
    Transition(label='Sensor Calibration'),
    Transition(label='Nutrient Mix'),
    Transition(label='Climate Control'),
    Transition(label='Regulatory Check'),
    Transition(label='Community Meet'),
    Transition(label='Energy Audit'),
    Transition(label='Staff Training'),
    Transition(label='Installation'),
    Transition(label='System Testing'),
    Transition(label='Yield Analysis'),
    Transition(label='Resource Audit'),
    Transition(label='Impact Review')
])

root.order.add_edge(Transition(label='Site Survey'), Transition(label='Light Mapping'))
root.order.add_edge(Transition(label='Site Survey'), Transition(label='Water Testing'))
root.order.add_edge(Transition(label='Light Mapping'), Transition(label='Design Modules'))
root.order.add_edge(Transition(label='Water Testing'), Transition(label='Design Modules'))
root.order.add_edge(Transition(label='Design Modules'), Transition(label='IoT Setup'))
root.order.add_edge(Transition(label='IoT Setup'), Transition(label='Sensor Calibration'))
root.order.add_edge(Transition(label='Sensor Calibration'), Transition(label='Nutrient Mix'))
root.order.add_edge(Transition(label='Nutrient Mix'), Transition(label='Climate Control'))
root.order.add_edge(Transition(label='Climate Control'), Transition(label='Regulatory Check'))
root.order.add_edge(Transition(label='Regulatory Check'), Transition(label='Community Meet'))
root.order.add_edge(Transition(label='Community Meet'), Transition(label='Energy Audit'))
root.order.add_edge(Transition(label='Energy Audit'), Transition(label='Staff Training'))
root.order.add_edge(Transition(label='Staff Training'), Transition(label='Installation'))
root.order.add_edge(Transition(label='Installation'), Transition(label='System Testing'))
root.order.add_edge(Transition(label='System Testing'), Transition(label='Yield Analysis'))
root.order.add_edge(Transition(label='Yield Analysis'), Transition(label='Resource Audit'))
root.order.add_edge(Transition(label='Resource Audit'), Transition(label='Impact Review'))