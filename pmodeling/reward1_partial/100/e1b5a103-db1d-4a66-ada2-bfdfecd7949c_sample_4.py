from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the POWL model
root = StrictPartialOrder(nodes=[
    Transition(label='Site Analysis'),
    Transition(label='Structure Check'),
    Transition(label='Climate Setup'),
    Transition(label='Hydroponics Install'),
    Transition(label='Nutrient Mix'),
    Transition(label='Seed Select'),
    Transition(label='Light Schedule'),
    Transition(label='Irrigation Plan'),
    Transition(label='Health Monitor'),
    Transition(label='Pest Control'),
    Transition(label='Robotic Harvest'),
    Transition(label='Clean Packaging'),
    Transition(label='Distribution Plan'),
    Transition(label='Data Collection'),
    Transition(label='Cycle Feedback')
])

# Define the partial order structure
root.order.add_edge(Transition(label='Site Analysis'), Transition(label='Structure Check'))
root.order.add_edge(Transition(label='Structure Check'), Transition(label='Climate Setup'))
root.order.add_edge(Transition(label='Climate Setup'), Transition(label='Hydroponics Install'))
root.order.add_edge(Transition(label='Hydroponics Install'), Transition(label='Nutrient Mix'))
root.order.add_edge(Transition(label='Nutrient Mix'), Transition(label='Seed Select'))
root.order.add_edge(Transition(label='Seed Select'), Transition(label='Light Schedule'))
root.order.add_edge(Transition(label='Light Schedule'), Transition(label='Irrigation Plan'))
root.order.add_edge(Transition(label='Irrigation Plan'), Transition(label='Health Monitor'))
root.order.add_edge(Transition(label='Health Monitor'), Transition(label='Pest Control'))
root.order.add_edge(Transition(label='Pest Control'), Transition(label='Robotic Harvest'))
root.order.add_edge(Transition(label='Robotic Harvest'), Transition(label='Clean Packaging'))
root.order.add_edge(Transition(label='Clean Packaging'), Transition(label='Distribution Plan'))
root.order.add_edge(Transition(label='Distribution Plan'), Transition(label='Data Collection'))
root.order.add_edge(Transition(label='Data Collection'), Transition(label='Cycle Feedback'))

# Print the root model
print(root)