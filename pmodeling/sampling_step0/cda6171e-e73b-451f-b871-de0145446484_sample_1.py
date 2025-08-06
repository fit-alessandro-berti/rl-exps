root = StrictPartialOrder(nodes=[
    Transition(label='Site Analysis'),
    Transition(label='Structure Check'),
    Transition(label='Modify Layout'),
    Transition(label='Install HVAC'),
    Transition(label='Setup Hydroponics'),
    Transition(label='Prepare Nutrients'),
    Transition(label='Select Seeds'),
    Transition(label='Automate Planting'),
    Transition(label='Deploy Sensors'),
    Transition(label='Pest Control'),
    Transition(label='Optimize Energy'),
    Transition(label='Recycle Water'),
    Transition(label='Automate Harvest'),
    Transition(label='Package Crops'),
    Transition(label='Coordinate Delivery'),
    Transition(label='Analyze Data')
])

root.order.add_edge(Transition(label='Site Analysis'), Transition(label='Structure Check'))
root.order.add_edge(Transition(label='Structure Check'), Transition(label='Modify Layout'))
root.order.add_edge(Transition(label='Modify Layout'), Transition(label='Install HVAC'))
root.order.add_edge(Transition(label='Install HVAC'), Transition(label='Setup Hydroponics'))
root.order.add_edge(Transition(label='Setup Hydroponics'), Transition(label='Prepare Nutrients'))
root.order.add_edge(Transition(label='Prepare Nutrients'), Transition(label='Select Seeds'))
root.order.add_edge(Transition(label='Select Seeds'), Transition(label='Automate Planting'))
root.order.add_edge(Transition(label='Automate Planting'), Transition(label='Deploy Sensors'))
root.order.add_edge(Transition(label='Deploy Sensors'), Transition(label='Pest Control'))
root.order.add_edge(Transition(label='Pest Control'), Transition(label='Optimize Energy'))
root.order.add_edge(Transition(label='Optimize Energy'), Transition(label='Recycle Water'))
root.order.add_edge(Transition(label='Recycle Water'), Transition(label='Automate Harvest'))
root.order.add_edge(Transition(label='Automate Harvest'), Transition(label='Package Crops'))
root.order.add_edge(Transition(label='Package Crops'), Transition(label='Coordinate Delivery'))
root.order.add_edge(Transition(label='Coordinate Delivery'), Transition(label='Analyze Data'))