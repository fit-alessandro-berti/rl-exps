root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Design Layout'),
    Transition(label='Permit Acquire'),
    Transition(label='Modular Build'),
    Transition(label='Climate Setup'),
    Transition(label='Nutrient Mix'),
    Transition(label='Seed Automation'),
    Transition(label='Pest Control'),
    Transition(label='Energy Audit'),
    Transition(label='Sensor Install'),
    Transition(label='Growth Monitor'),
    Transition(label='Waste Process'),
    Transition(label='Data Analysis'),
    Transition(label='Staff Train'),
    Transition(label='Community Link'),
    Transition(label='Yield Report')
])

# Define the dependencies
root.order.add_edge(Transition(label='Site Survey'), Transition(label='Design Layout'))
root.order.add_edge(Transition(label='Design Layout'), Transition(label='Permit Acquire'))
root.order.add_edge(Transition(label='Permit Acquire'), Transition(label='Modular Build'))
root.order.add_edge(Transition(label='Modular Build'), Transition(label='Climate Setup'))
root.order.add_edge(Transition(label='Climate Setup'), Transition(label='Nutrient Mix'))
root.order.add_edge(Transition(label='Nutrient Mix'), Transition(label='Seed Automation'))
root.order.add_edge(Transition(label='Seed Automation'), Transition(label='Pest Control'))
root.order.add_edge(Transition(label='Pest Control'), Transition(label='Energy Audit'))
root.order.add_edge(Transition(label='Energy Audit'), Transition(label='Sensor Install'))
root.order.add_edge(Transition(label='Sensor Install'), Transition(label='Growth Monitor'))
root.order.add_edge(Transition(label='Growth Monitor'), Transition(label='Waste Process'))
root.order.add_edge(Transition(label='Waste Process'), Transition(label='Data Analysis'))
root.order.add_edge(Transition(label='Data Analysis'), Transition(label='Staff Train'))
root.order.add_edge(Transition(label='Staff Train'), Transition(label='Community Link'))
root.order.add_edge(Transition(label='Community Link'), Transition(label='Yield Report'))