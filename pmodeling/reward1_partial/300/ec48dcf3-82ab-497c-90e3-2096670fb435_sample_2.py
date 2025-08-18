root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Design Layout'),
    Transition(label='Structure Build'),
    Transition(label='System Install'),
    Transition(label='Climate Setup'),
    Transition(label='Nutrient Prep'),
    Transition(label='Seed Germinate'),
    Transition(label='Planting Phase'),
    Transition(label='Sensor Deploy'),
    Transition(label='Pest Control'),
    Transition(label='Water Monitor'),
    Transition(label='Data Analyze'),
    Transition(label='Staff Train'),
    Transition(label='Yield Forecast'),
    Transition(label='Community Meet')
])

root.order.add_edge(Transition(label='Site Survey'), Transition(label='Design Layout'))
root.order.add_edge(Transition(label='Design Layout'), Transition(label='Structure Build'))
root.order.add_edge(Transition(label='Structure Build'), Transition(label='System Install'))
root.order.add_edge(Transition(label='System Install'), Transition(label='Climate Setup'))
root.order.add_edge(Transition(label='Climate Setup'), Transition(label='Nutrient Prep'))
root.order.add_edge(Transition(label='Nutrient Prep'), Transition(label='Seed Germinate'))
root.order.add_edge(Transition(label='Seed Germinate'), Transition(label='Planting Phase'))
root.order.add_edge(Transition(label='Planting Phase'), Transition(label='Sensor Deploy'))
root.order.add_edge(Transition(label='Sensor Deploy'), Transition(label='Pest Control'))
root.order.add_edge(Transition(label='Pest Control'), Transition(label='Water Monitor'))
root.order.add_edge(Transition(label='Water Monitor'), Transition(label='Data Analyze'))
root.order.add_edge(Transition(label='Data Analyze'), Transition(label='Staff Train'))
root.order.add_edge(Transition(label='Staff Train'), Transition(label='Yield Forecast'))
root.order.add_edge(Transition(label='Yield Forecast'), Transition(label='Community Meet'))