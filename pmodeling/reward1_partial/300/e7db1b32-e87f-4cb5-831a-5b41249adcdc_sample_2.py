root = StrictPartialOrder(nodes=[
    Transition(label='Seed Selection'),
    Transition(label='AI Prediction'),
    Transition(label='Automated Planting'),
    Transition(label='Sensor Calibration'),
    Transition(label='Environment Adjust'),
    Transition(label='Nutrient Dosing'),
    Transition(label='Hydroponic Flow'),
    Transition(label='Robotic Pruning'),
    Transition(label='Health Monitor'),
    Transition(label='Harvesting Ops'),
    Transition(label='Data Analysis'),
    Transition(label='Predictive Check'),
    Transition(label='Waste Composting'),
    Transition(label='Water Recycling'),
    Transition(label='Eco Packaging'),
    Transition(label='Carbon Tracking'),
    Transition(label='Logistics Dispatch')
])

root.order.add_edge(Transition(label='Seed Selection'), Transition(label='AI Prediction'))
root.order.add_edge(Transition(label='AI Prediction'), Transition(label='Automated Planting'))
root.order.add_edge(Transition(label='Automated Planting'), Transition(label='Sensor Calibration'))
root.order.add_edge(Transition(label='Sensor Calibration'), Transition(label='Environment Adjust'))
root.order.add_edge(Transition(label='Environment Adjust'), Transition(label='Nutrient Dosing'))
root.order.add_edge(Transition(label='Nutrient Dosing'), Transition(label='Hydroponic Flow'))
root.order.add_edge(Transition(label='Hydroponic Flow'), Transition(label='Robotic Pruning'))
root.order.add_edge(Transition(label='Robotic Pruning'), Transition(label='Health Monitor'))
root.order.add_edge(Transition(label='Health Monitor'), Transition(label='Harvesting Ops'))
root.order.add_edge(Transition(label='Harvesting Ops'), Transition(label='Data Analysis'))
root.order.add_edge(Transition(label='Data Analysis'), Transition(label='Predictive Check'))
root.order.add_edge(Transition(label='Predictive Check'), Transition(label='Waste Composting'))
root.order.add_edge(Transition(label='Waste Composting'), Transition(label='Water Recycling'))
root.order.add_edge(Transition(label='Water Recycling'), Transition(label='Eco Packaging'))
root.order.add_edge(Transition(label='Eco Packaging'), Transition(label='Carbon Tracking'))
root.order.add_edge(Transition(label='Carbon Tracking'), Transition(label='Logistics Dispatch'))