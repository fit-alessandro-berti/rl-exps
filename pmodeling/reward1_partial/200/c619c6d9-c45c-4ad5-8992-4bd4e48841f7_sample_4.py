root = StrictPartialOrder(nodes=[
    Transition(label='Design Consult'),
    Transition(label='Component Sourcing'),
    Transition(label='Sensor Calibrate'),
    Transition(label='Firmware Integrate'),
    Transition(label='Payload Configure'),
    Transition(label='Assembly Setup'),
    Transition(label='Wiring Connect'),
    Transition(label='Chassis Build'),
    Transition(label='Software Load'),
    Transition(label='Flight Testing'),
    Transition(label='Data Analyze'),
    Transition(label='Regulation Check'),
    Transition(label='Quality Inspect'),
    Transition(label='Packaging Prep'),
    Transition(label='Logistics Plan'),
    Transition(label='Client Review')
])

root.order.add_edge(Transition(label='Design Consult'), Transition(label='Component Sourcing'))
root.order.add_edge(Transition(label='Component Sourcing'), Transition(label='Sensor Calibrate'))
root.order.add_edge(Transition(label='Sensor Calibrate'), Transition(label='Firmware Integrate'))
root.order.add_edge(Transition(label='Firmware Integrate'), Transition(label='Payload Configure'))
root.order.add_edge(Transition(label='Payload Configure'), Transition(label='Assembly Setup'))
root.order.add_edge(Transition(label='Assembly Setup'), Transition(label='Wiring Connect'))
root.order.add_edge(Transition(label='Wiring Connect'), Transition(label='Chassis Build'))
root.order.add_edge(Transition(label='Chassis Build'), Transition(label='Software Load'))
root.order.add_edge(Transition(label='Software Load'), Transition(label='Flight Testing'))
root.order.add_edge(Transition(label='Flight Testing'), Transition(label='Data Analyze'))
root.order.add_edge(Transition(label='Data Analyze'), Transition(label='Regulation Check'))
root.order.add_edge(Transition(label='Regulation Check'), Transition(label='Quality Inspect'))
root.order.add_edge(Transition(label='Quality Inspect'), Transition(label='Packaging Prep'))
root.order.add_edge(Transition(label='Packaging Prep'), Transition(label='Logistics Plan'))
root.order.add_edge(Transition(label='Logistics Plan'), Transition(label='Client Review'))