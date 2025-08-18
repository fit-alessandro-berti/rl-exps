root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Permit Review'),
    Transition(label='Design Layout'),
    Transition(label='System Assembly'),
    Transition(label='Climate Setup'),
    Transition(label='Nutrient Prep'),
    Transition(label='Irrigation Test'),
    Transition(label='Lighting Config'),
    Transition(label='Energy Install'),
    Transition(label='Sensor Setup'),
    Transition(label='Automation Deploy'),
    Transition(label='Crop Seeding'),
    Transition(label='Waste Plan'),
    Transition(label='Staff Training'),
    Transition(label='Community Outreach'),
    Transition(label='Yield Monitor'),
    Transition(label='Maintenance Check')
])

root.order.add_edge(Transition(label='Site Survey'), Transition(label='Permit Review'))
root.order.add_edge(Transition(label='Permit Review'), Transition(label='Design Layout'))
root.order.add_edge(Transition(label='Design Layout'), Transition(label='System Assembly'))
root.order.add_edge(Transition(label='System Assembly'), Transition(label='Climate Setup'))
root.order.add_edge(Transition(label='Climate Setup'), Transition(label='Nutrient Prep'))
root.order.add_edge(Transition(label='Nutrient Prep'), Transition(label='Irrigation Test'))
root.order.add_edge(Transition(label='Irrigation Test'), Transition(label='Lighting Config'))
root.order.add_edge(Transition(label='Lighting Config'), Transition(label='Energy Install'))
root.order.add_edge(Transition(label='Energy Install'), Transition(label='Sensor Setup'))
root.order.add_edge(Transition(label='Sensor Setup'), Transition(label='Automation Deploy'))
root.order.add_edge(Transition(label='Automation Deploy'), Transition(label='Crop Seeding'))
root.order.add_edge(Transition(label='Crop Seeding'), Transition(label='Waste Plan'))
root.order.add_edge(Transition(label='Waste Plan'), Transition(label='Staff Training'))
root.order.add_edge(Transition(label='Staff Training'), Transition(label='Community Outreach'))
root.order.add_edge(Transition(label='Community Outreach'), Transition(label='Yield Monitor'))
root.order.add_edge(Transition(label='Yield Monitor'), Transition(label='Maintenance Check'))