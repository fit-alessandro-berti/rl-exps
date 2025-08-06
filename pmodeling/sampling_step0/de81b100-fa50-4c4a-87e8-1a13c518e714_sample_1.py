root = StrictPartialOrder(nodes=[
    Transition('Site Survey'),
    Transition('Permit Acquire'),
    Transition('Rack Design'),
    Transition('Seed Selection'),
    Transition('Nutrient Mix'),
    Transition('Lighting Setup'),
    Transition('Sensor Install'),
    Transition('System Test'),
    Transition('Staff Hire'),
    Transition('Training Lead'),
    Transition('Waste Manage'),
    Transition('Supply Chain'),
    Transition('Crop Cycle'),
    Transition('Data Monitor'),
    Transition('Harvest Plan'),
    Transition('Distribution')
])

root.order.add_edge('Site Survey', 'Permit Acquire')
root.order.add_edge('Permit Acquire', 'Rack Design')
root.order.add_edge('Rack Design', 'Seed Selection')
root.order.add_edge('Seed Selection', 'Nutrient Mix')
root.order.add_edge('Nutrient Mix', 'Lighting Setup')
root.order.add_edge('Lighting Setup', 'Sensor Install')
root.order.add_edge('Sensor Install', 'System Test')
root.order.add_edge('System Test', 'Staff Hire')
root.order.add_edge('Staff Hire', 'Training Lead')
root.order.add_edge('Training Lead', 'Waste Manage')
root.order.add_edge('Waste Manage', 'Supply Chain')
root.order.add_edge('Supply Chain', 'Crop Cycle')
root.order.add_edge('Crop Cycle', 'Data Monitor')
root.order.add_edge('Data Monitor', 'Harvest Plan')
root.order.add_edge('Harvest Plan', 'Distribution')