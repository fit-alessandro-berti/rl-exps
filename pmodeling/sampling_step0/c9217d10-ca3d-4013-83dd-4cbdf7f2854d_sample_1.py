root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Climate Study'),
    Transition(label='Design Layout'),
    Transition(label='System Install'),
    Transition(label='Crop Select'),
    Transition(label='Nutrient Plan'),
    Transition(label='Sensor Setup'),
    Transition(label='Automation Test'),
    Transition(label='Staff Train'),
    Transition(label='Compliance Check'),
    Transition(label='Marketing Sync'),
    Transition(label='Data Monitor'),
    Transition(label='Yield Analyze'),
    Transition(label='Supply Chain'),
    Transition(label='Customer Engage')
])

root.order.add_edge(Transition(label='Site Survey'), Transition(label='Climate Study'))
root.order.add_edge(Transition(label='Climate Study'), Transition(label='Design Layout'))
root.order.add_edge(Transition(label='Design Layout'), Transition(label='System Install'))
root.order.add_edge(Transition(label='System Install'), Transition(label='Crop Select'))
root.order.add_edge(Transition(label='Crop Select'), Transition(label='Nutrient Plan'))
root.order.add_edge(Transition(label='Nutrient Plan'), Transition(label='Sensor Setup'))
root.order.add_edge(Transition(label='Sensor Setup'), Transition(label='Automation Test'))
root.order.add_edge(Transition(label='Automation Test'), Transition(label='Staff Train'))
root.order.add_edge(Transition(label='Staff Train'), Transition(label='Compliance Check'))
root.order.add_edge(Transition(label='Compliance Check'), Transition(label='Marketing Sync'))
root.order.add_edge(Transition(label='Marketing Sync'), Transition(label='Data Monitor'))
root.order.add_edge(Transition(label='Data Monitor'), Transition(label='Yield Analyze'))
root.order.add_edge(Transition(label='Yield Analyze'), Transition(label='Supply Chain'))
root.order.add_edge(Transition(label='Supply Chain'), Transition(label='Customer Engage'))