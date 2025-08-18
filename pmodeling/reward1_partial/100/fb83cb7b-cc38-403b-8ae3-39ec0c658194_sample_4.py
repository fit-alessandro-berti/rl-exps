root = StrictPartialOrder(nodes=[
    Transition(label='Site Assess'),
    Transition(label='Structure Check'),
    Transition(label='Permit Obtain'),
    Transition(label='Material Source'),
    Transition(label='Soil Prepare'),
    Transition(label='Waterproof Roof'),
    Transition(label='Irrigation Setup'),
    Transition(label='Bed Assemble'),
    Transition(label='Crop Plan'),
    Transition(label='Pest Monitor'),
    Transition(label='Nutrient Calibrate'),
    Transition(label='Harvest Schedule'),
    Transition(label='Community Train'),
    Transition(label='Yield Record'),
    Transition(label='Impact Review')
])

# Define the partial order relationships
root.order.add_edge(Transition(label='Site Assess'), Transition(label='Structure Check'))
root.order.add_edge(Transition(label='Structure Check'), Transition(label='Permit Obtain'))
root.order.add_edge(Transition(label='Permit Obtain'), Transition(label='Material Source'))
root.order.add_edge(Transition(label='Material Source'), Transition(label='Soil Prepare'))
root.order.add_edge(Transition(label='Soil Prepare'), Transition(label='Waterproof Roof'))
root.order.add_edge(Transition(label='Waterproof Roof'), Transition(label='Irrigation Setup'))
root.order.add_edge(Transition(label='Irrigation Setup'), Transition(label='Bed Assemble'))
root.order.add_edge(Transition(label='Bed Assemble'), Transition(label='Crop Plan'))
root.order.add_edge(Transition(label='Crop Plan'), Transition(label='Pest Monitor'))
root.order.add_edge(Transition(label='Pest Monitor'), Transition(label='Nutrient Calibrate'))
root.order.add_edge(Transition(label='Nutrient Calibrate'), Transition(label='Harvest Schedule'))
root.order.add_edge(Transition(label='Harvest Schedule'), Transition(label='Community Train'))
root.order.add_edge(Transition(label='Community Train'), Transition(label='Yield Record'))
root.order.add_edge(Transition(label='Yield Record'), Transition(label='Impact Review'))