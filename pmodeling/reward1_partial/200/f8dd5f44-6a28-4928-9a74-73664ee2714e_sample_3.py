root = StrictPartialOrder(nodes=[
    Transition(label='Seed Selection'),
    Transition(label='Nutrient Mix'),
    Transition(label='Environment Setup'),
    Transition(label='Sensor Deployment'),
    Transition(label='Growth Monitoring'),
    Transition(label='Pest Detection'),
    Transition(label='Automated Harvest'),
    Transition(label='Quality Check'),
    Transition(label='Packaging Prep'),
    Transition(label='Biodegradable Pack'),
    Transition(label='Inventory Sync'),
    Transition(label='Demand Forecast'),
    Transition(label='Micro Fulfillment'),
    Transition(label='Local Dispatch'),
    Transition(label='Consumer Feedback'),
    Transition(label='Crop Adjustment')
])

root.order.add_edge(Transition(label='Seed Selection'), Transition(label='Nutrient Mix'))
root.order.add_edge(Transition(label='Nutrient Mix'), Transition(label='Environment Setup'))
root.order.add_edge(Transition(label='Environment Setup'), Transition(label='Sensor Deployment'))
root.order.add_edge(Transition(label='Sensor Deployment'), Transition(label='Growth Monitoring'))
root.order.add_edge(Transition(label='Growth Monitoring'), Transition(label='Pest Detection'))
root.order.add_edge(Transition(label='Pest Detection'), Transition(label='Automated Harvest'))
root.order.add_edge(Transition(label='Automated Harvest'), Transition(label='Quality Check'))
root.order.add_edge(Transition(label='Quality Check'), Transition(label='Packaging Prep'))
root.order.add_edge(Transition(label='Packaging Prep'), Transition(label='Biodegradable Pack'))
root.order.add_edge(Transition(label='Biodegradable Pack'), Transition(label='Inventory Sync'))
root.order.add_edge(Transition(label='Inventory Sync'), Transition(label='Demand Forecast'))
root.order.add_edge(Transition(label='Demand Forecast'), Transition(label='Micro Fulfillment'))
root.order.add_edge(Transition(label='Micro Fulfillment'), Transition(label='Local Dispatch'))
root.order.add_edge(Transition(label='Local Dispatch'), Transition(label='Consumer Feedback'))
root.order.add_edge(Transition(label='Consumer Feedback'), Transition(label='Crop Adjustment'))