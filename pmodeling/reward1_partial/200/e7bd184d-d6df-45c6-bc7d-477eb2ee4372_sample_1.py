root = StrictPartialOrder(nodes=[
    Transition(label='Site Analysis'),
    Transition(label='Structure Check'),
    Transition(label='Enviro Design'),
    Transition(label='Hydro Setup'),
    Transition(label='Aeroponics Add'),
    Transition(label='Lighting Procure'),
    Transition(label='Water Recycle'),
    Transition(label='Rack Install'),
    Transition(label='Seed Select'),
    Transition(label='Germinate Seeds'),
    Transition(label='Nutrient Mix'),
    Transition(label='Staff Train'),
    Transition(label='Pest Control'),
    Transition(label='Pilot Crop'),
    Transition(label='Data Gather'),
    Transition(label='Yield Optimize')
])

root.order.add_edge(Transition(label='Site Analysis'), Transition(label='Structure Check'))
root.order.add_edge(Transition(label='Structure Check'), Transition(label='Enviro Design'))
root.order.add_edge(Transition(label='Enviro Design'), Transition(label='Hydro Setup'))
root.order.add_edge(Transition(label='Enviro Design'), Transition(label='Aeroponics Add'))
root.order.add_edge(Transition(label='Hydro Setup'), Transition(label='Lighting Procure'))
root.order.add_edge(Transition(label='Aeroponics Add'), Transition(label='Lighting Procure'))
root.order.add_edge(Transition(label='Lighting Procure'), Transition(label='Water Recycle'))
root.order.add_edge(Transition(label='Water Recycle'), Transition(label='Rack Install'))
root.order.add_edge(Transition(label='Rack Install'), Transition(label='Seed Select'))
root.order.add_edge(Transition(label='Seed Select'), Transition(label='Germinate Seeds'))
root.order.add_edge(Transition(label='Germinate Seeds'), Transition(label='Nutrient Mix'))
root.order.add_edge(Transition(label='Nutrient Mix'), Transition(label='Staff Train'))
root.order.add_edge(Transition(label='Staff Train'), Transition(label='Pest Control'))
root.order.add_edge(Transition(label='Pest Control'), Transition(label='Pilot Crop'))
root.order.add_edge(Transition(label='Pilot Crop'), Transition(label='Data Gather'))
root.order.add_edge(Transition(label='Data Gather'), Transition(label='Yield Optimize'))