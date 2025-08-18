root = StrictPartialOrder(nodes=[
    Transition(label='Seed Select'),
    Transition(label='Trend Analyze'),
    Transition(label='Nutrient Mix'),
    Transition(label='Auto Plant'),
    Transition(label='Sensor Check'),
    Transition(label='Data Analyze'),
    Transition(label='Water Adjust'),
    Transition(label='Light Control'),
    Transition(label='Humidity Monitor'),
    Transition(label='Pest Inspect'),
    Transition(label='Growth Forecast'),
    Transition(label='Harvest Plan'),
    Transition(label='Rapid Cool'),
    Transition(label='Quality Grade'),
    Transition(label='Eco Package'),
    Transition(label='Logistics Prep'),
    Transition(label='Feedback Collect'),
    Transition(label='System Maintain')
])

root.order.add_edge(Transition(label='Seed Select'), Transition(label='Trend Analyze'))
root.order.add_edge(Transition(label='Trend Analyze'), Transition(label='Nutrient Mix'))
root.order.add_edge(Transition(label='Nutrient Mix'), Transition(label='Auto Plant'))
root.order.add_edge(Transition(label='Auto Plant'), Transition(label='Sensor Check'))
root.order.add_edge(Transition(label='Sensor Check'), Transition(label='Data Analyze'))
root.order.add_edge(Transition(label='Data Analyze'), Transition(label='Water Adjust'))
root.order.add_edge(Transition(label='Data Analyze'), Transition(label='Light Control'))
root.order.add_edge(Transition(label='Data Analyze'), Transition(label='Humidity Monitor'))
root.order.add_edge(Transition(label='Data Analyze'), Transition(label='Pest Inspect'))
root.order.add_edge(Transition(label='Data Analyze'), Transition(label='Growth Forecast'))
root.order.add_edge(Transition(label='Growth Forecast'), Transition(label='Harvest Plan'))
root.order.add_edge(Transition(label='Sensor Check'), Transition(label='Rapid Cool'))
root.order.add_edge(Transition(label='Rapid Cool'), Transition(label='Quality Grade'))
root.order.add_edge(Transition(label='Quality Grade'), Transition(label='Eco Package'))
root.order.add_edge(Transition(label='Eco Package'), Transition(label='Logistics Prep'))
root.order.add_edge(Transition(label='Logistics Prep'), Transition(label='Feedback Collect'))
root.order.add_edge(Transition(label='Feedback Collect'), Transition(label='System Maintain'))