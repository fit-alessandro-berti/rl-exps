root = StrictPartialOrder(nodes=[
    Transition(label='Client Brief'),
    Transition(label='Design Draft'),
    Transition(label='Component Order'),
    Transition(label='Firmware Build'),
    Transition(label='PCB Assembly'),
    Transition(label='Sensor Install'),
    Transition(label='Motor Mount'),
    Transition(label='Battery Test'),
    Transition(label='AI Module'),
    Transition(label='System Integrate'),
    Transition(label='Flight Simulate'),
    Transition(label='Stress Test'),
    Transition(label='Compliance Check'),
    Transition(label='Quality Audit'),
    Transition(label='Package Drone'),
    Transition(label='Delivery Plan')
])
root.order.add_edge(Transition(label='Client Brief'), Transition(label='Design Draft'))
root.order.add_edge(Transition(label='Design Draft'), Transition(label='Component Order'))
root.order.add_edge(Transition(label='Component Order'), Transition(label='Firmware Build'))
root.order.add_edge(Transition(label='Firmware Build'), Transition(label='PCB Assembly'))
root.order.add_edge(Transition(label='PCB Assembly'), Transition(label='Sensor Install'))
root.order.add_edge(Transition(label='Sensor Install'), Transition(label='Motor Mount'))
root.order.add_edge(Transition(label='Motor Mount'), Transition(label='Battery Test'))
root.order.add_edge(Transition(label='Battery Test'), Transition(label='AI Module'))
root.order.add_edge(Transition(label='AI Module'), Transition(label='System Integrate'))
root.order.add_edge(Transition(label='System Integrate'), Transition(label='Flight Simulate'))
root.order.add_edge(Transition(label='Flight Simulate'), Transition(label='Stress Test'))
root.order.add_edge(Transition(label='Stress Test'), Transition(label='Compliance Check'))
root.order.add_edge(Transition(label='Compliance Check'), Transition(label='Quality Audit'))
root.order.add_edge(Transition(label='Quality Audit'), Transition(label='Package Drone'))
root.order.add_edge(Transition(label='Package Drone'), Transition(label='Delivery Plan'))