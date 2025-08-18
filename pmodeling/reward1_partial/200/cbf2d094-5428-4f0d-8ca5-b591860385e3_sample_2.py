root = StrictPartialOrder(nodes=[
    Transition(label='Seed Select'),
    Transition(label='Nutrient Mix'),
    Transition(label='Climate Adjust'),
    Transition(label='Planting Robotic'),
    Transition(label='Growth Monitor'),
    Transition(label='Pest Control'),
    Transition(label='Water Recycle'),
    Transition(label='Light Optimize'),
    Transition(label='Growth Analyze'),
    Transition(label='Harvest Sync'),
    Transition(label='Sterilize Crop'),
    Transition(label='Package Fresh'),
    Transition(label='Demand Forecast'),
    Transition(label='Delivery Plan'),
    Transition(label='Data Feedback')
])

root.order.add_edge(Transition(label='Seed Select'), Transition(label='Nutrient Mix'))
root.order.add_edge(Transition(label='Nutrient Mix'), Transition(label='Climate Adjust'))
root.order.add_edge(Transition(label='Climate Adjust'), Transition(label='Planting Robotic'))
root.order.add_edge(Transition(label='Planting Robotic'), Transition(label='Growth Monitor'))
root.order.add_edge(Transition(label='Growth Monitor'), Transition(label='Pest Control'))
root.order.add_edge(Transition(label='Pest Control'), Transition(label='Water Recycle'))
root.order.add_edge(Transition(label='Water Recycle'), Transition(label='Light Optimize'))
root.order.add_edge(Transition(label='Light Optimize'), Transition(label='Growth Analyze'))
root.order.add_edge(Transition(label='Growth Analyze'), Transition(label='Harvest Sync'))
root.order.add_edge(Transition(label='Harvest Sync'), Transition(label='Sterilize Crop'))
root.order.add_edge(Transition(label='Sterilize Crop'), Transition(label='Package Fresh'))
root.order.add_edge(Transition(label='Package Fresh'), Transition(label='Demand Forecast'))
root.order.add_edge(Transition(label='Demand Forecast'), Transition(label='Delivery Plan'))
root.order.add_edge(Transition(label='Delivery Plan'), Transition(label='Data Feedback'))