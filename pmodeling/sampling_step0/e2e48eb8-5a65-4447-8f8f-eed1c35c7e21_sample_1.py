root = StrictPartialOrder(nodes=[
    Transition('Site Survey'),
    Transition('Structural Check'),
    Transition('Climate Study'),
    Transition('Soil Prep'),
    Transition('Seed Selection'),
    Transition('Irrigation Setup'),
    Transition('Nutrient Mix'),
    Transition('Sensor Install'),
    Transition('Pest Monitor'),
    Transition('Data Analysis'),
    Transition('Regulation Review'),
    Transition('Community Meet'),
    Transition('Harvest Plan'),
    Transition('Packaging Design'),
    Transition('Distribution Map'),
    Transition('Feedback Loop'),
    Transition('Maintenance Schedule')
])

root.order.add_edge('Site Survey', 'Structural Check')
root.order.add_edge('Site Survey', 'Climate Study')
root.order.add_edge('Structural Check', 'Soil Prep')
root.order.add_edge('Climate Study', 'Soil Prep')
root.order.add_edge('Soil Prep', 'Seed Selection')
root.order.add_edge('Soil Prep', 'Irrigation Setup')
root.order.add_edge('Irrigation Setup', 'Nutrient Mix')
root.order.add_edge('Nutrient Mix', 'Sensor Install')
root.order.add_edge('Sensor Install', 'Pest Monitor')
root.order.add_edge('Pest Monitor', 'Data Analysis')
root.order.add_edge('Data Analysis', 'Regulation Review')
root.order.add_edge('Regulation Review', 'Community Meet')
root.order.add_edge('Community Meet', 'Harvest Plan')
root.order.add_edge('Harvest Plan', 'Packaging Design')
root.order.add_edge('Packaging Design', 'Distribution Map')
root.order.add_edge('Distribution Map', 'Feedback Loop')
root.order.add_edge('Feedback Loop', 'Maintenance Schedule')