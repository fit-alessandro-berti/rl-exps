root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Structural Check'),
    Transition(label='Climate Study'),
    Transition(label='Soil Prep'),
    Transition(label='Seed Selection'),
    Transition(label='Irrigation Setup'),
    Transition(label='Nutrient Mix'),
    Transition(label='Sensor Install'),
    Transition(label='Pest Monitor'),
    Transition(label='Data Analysis'),
    Transition(label='Regulation Review'),
    Transition(label='Community Meet'),
    Transition(label='Harvest Plan'),
    Transition(label='Packaging Design'),
    Transition(label='Distribution Map'),
    Transition(label='Feedback Loop'),
    Transition(label='Maintenance Schedule')
])

# Define the dependencies between activities
root.order.add_edge(Transition(label='Site Survey'), Transition(label='Structural Check'))
root.order.add_edge(Transition(label='Site Survey'), Transition(label='Climate Study'))
root.order.add_edge(Transition(label='Site Survey'), Transition(label='Soil Prep'))
root.order.add_edge(Transition(label='Site Survey'), Transition(label='Seed Selection'))
root.order.add_edge(Transition(label='Site Survey'), Transition(label='Irrigation Setup'))
root.order.add_edge(Transition(label='Site Survey'), Transition(label='Nutrient Mix'))
root.order.add_edge(Transition(label='Site Survey'), Transition(label='Sensor Install'))
root.order.add_edge(Transition(label='Site Survey'), Transition(label='Pest Monitor'))
root.order.add_edge(Transition(label='Site Survey'), Transition(label='Data Analysis'))
root.order.add_edge(Transition(label='Site Survey'), Transition(label='Regulation Review'))
root.order.add_edge(Transition(label='Site Survey'), Transition(label='Community Meet'))
root.order.add_edge(Transition(label='Site Survey'), Transition(label='Harvest Plan'))
root.order.add_edge(Transition(label='Site Survey'), Transition(label='Packaging Design'))
root.order.add_edge(Transition(label='Site Survey'), Transition(label='Distribution Map'))
root.order.add_edge(Transition(label='Site Survey'), Transition(label='Feedback Loop'))
root.order.add_edge(Transition(label='Site Survey'), Transition(label='Maintenance Schedule'))

root.order.add_edge(Transition(label='Structural Check'), Transition(label='Climate Study'))
root.order.add_edge(Transition(label='Structural Check'), Transition(label='Soil Prep'))
root.order.add_edge(Transition(label='Structural Check'), Transition(label='Seed Selection'))
root.order.add_edge(Transition(label='Structural Check'), Transition(label='Irrigation Setup'))
root.order.add_edge(Transition(label='Structural Check'), Transition(label='Nutrient Mix'))
root.order.add_edge(Transition(label='Structural Check'), Transition(label='Sensor Install'))
root.order.add_edge(Transition(label='Structural Check'), Transition(label='Pest Monitor'))
root.order.add_edge(Transition(label='Structural Check'), Transition(label='Data Analysis'))
root.order.add_edge(Transition(label='Structural Check'), Transition(label='Regulation Review'))
root.order.add_edge(Transition(label='Structural Check'), Transition(label='Community Meet'))
root.order.add_edge(Transition(label='Structural Check'), Transition(label='Harvest Plan'))
root.order.add_edge(Transition(label='Structural Check'), Transition(label='Packaging Design'))
root.order.add_edge(Transition(label='Structural Check'), Transition(label='Distribution Map'))
root.order.add_edge(Transition(label='Structural Check'), Transition(label='Feedback Loop'))
root.order.add_edge(Transition(label='Structural Check'), Transition(label='Maintenance Schedule'))

root.order.add_edge(Transition(label='Climate Study'), Transition(label='Soil Prep'))
root.order.add_edge(Transition(label='Climate Study'), Transition(label='Seed Selection'))
root.order.add_edge(Transition(label='Climate Study'), Transition(label='Irrigation Setup'))
root.order.add_edge(Transition(label='Climate Study'), Transition(label='Nutrient Mix'))
root.order.add_edge(Transition(label='Climate Study'), Transition(label='Sensor Install'))
root.order.add_edge(Transition(label='Climate Study'), Transition(label='Pest Monitor'))
root.order.add_edge(Transition(label='Climate Study'), Transition(label='Data Analysis'))
root.order.add_edge(Transition(label='Climate Study'), Transition(label='Regulation Review'))
root.order.add_edge(Transition(label='Climate Study'), Transition(label='Community Meet'))
root.order.add_edge(Transition(label='Climate Study'), Transition(label='Harvest Plan'))
root.order.add_edge(Transition(label='Climate Study'), Transition(label='Packaging Design'))
root.order.add_edge(Transition(label='Climate Study'), Transition(label='Distribution Map'))
root.order.add_edge(Transition(label='Climate Study'), Transition(label='Feedback Loop'))
root.order.add_edge(Transition(label='Climate Study'), Transition(label='Maintenance Schedule'))

root.order.add_edge(Transition(label='Soil Prep'), Transition(label='Seed Selection'))
root.order.add_edge(Transition(label='Soil Prep'), Transition(label='Irrigation Setup'))
root.order.add_edge(Transition(label='Soil Prep'), Transition(label='Nutrient Mix'))
root.order.add_edge(Transition(label='Soil Prep'), Transition(label='Sensor Install'))
root.order.add_edge(Transition(label='Soil Prep'), Transition(label='Pest Monitor'))
root.order.add_edge(Transition(label='Soil Prep'), Transition(label='Data Analysis'))
root.order.add_edge(Transition(label='Soil Prep'), Transition(label='Regulation Review'))
root.order.add_edge(Transition(label='Soil Prep'), Transition(label='Community Meet'))
root.order.add_edge(Transition(label='Soil Prep'), Transition(label='Harvest Plan'))
root.order.add_edge(Transition(label='Soil Prep'), Transition(label='Packaging Design'))
root.order.add_edge(Transition(label='Soil Prep'), Transition(label='Distribution Map'))
root.order.add_edge(Transition(label='Soil Prep'), Transition(label='Feedback Loop'))
root.order.add_edge(Transition(label='Soil Prep'), Transition(label='Maintenance Schedule'))

root.order.add_edge(Transition(label='Seed Selection'), Transition(label='Irrigation Setup'))
root.order.add_edge(Transition(label='Seed Selection'), Transition(label='Nutrient Mix'))
root.order.add_edge(Transition(label='Seed Selection'), Transition(label='Sensor Install'))
root.order.add_edge(Transition(label='Seed Selection'), Transition(label='Pest Monitor'))
root.order.add_edge(Transition(label='Seed Selection'), Transition(label='Data Analysis'))
root.order.add_edge(Transition(label='Seed Selection'), Transition(label='Regulation Review'))
root.order.add_edge(Transition(label='Seed Selection'), Transition(label='Community Meet'))
root.order.add_edge(Transition(label='Seed Selection'), Transition(label='Harvest Plan'))
root.order.add_edge(Transition(label='Seed Selection'), Transition(label='Packaging Design'))
root.order.add_edge(Transition(label='Seed Selection'), Transition(label='Distribution Map'))
root.order.add_edge(Transition(label='Seed Selection'), Transition(label='Feedback Loop'))
root.order.add_edge(Transition(label='Seed Selection'), Transition(label='Maintenance Schedule'))

root.order.add_edge(Transition(label='Irrigation Setup'), Transition(label='Nutrient Mix'))
root.order.add_edge(Transition(label='Irrigation Setup'), Transition(label='Sensor Install'))
root.order.add_edge(Transition(label='Irrigation Setup'), Transition(label='Pest Monitor'))
root.order.add_edge(Transition(label='Irrigation Setup'), Transition(label='Data Analysis'))
root.order.add_edge(Transition(label='Irrigation Setup'), Transition(label='Regulation Review'))
root.order.add_edge(Transition(label='Irrigation Setup'), Transition(label='Community Meet'))
root.order.add_edge(Transition(label='Irrigation Setup'), Transition(label='Harvest Plan'))
root.order.add_edge(Transition(label='Irrigation Setup'), Transition(label='Packaging Design'))
root.order.add_edge(Transition(label='Irrigation Setup'), Transition(label='Distribution Map'))
root.order.add_edge(Transition(label='Irrigation Setup'), Transition(label='Feedback Loop'))
root.order.add_edge(Transition(label='Irrigation Setup'), Transition(label='Maintenance Schedule'))

root.order.add_edge(Transition(label='Nutrient Mix'), Transition(label='Sensor Install'))
root.order.add_edge(Transition(label='Nutrient Mix'), Transition(label='Pest Monitor'))
root.order.add_edge(Transition(label='Nutrient Mix'), Transition(label='Data Analysis'))
root.order.add_edge(Transition(label='Nutrient Mix'), Transition(label='Regulation Review'))
root.order.add_edge(Transition(label='Nutrient Mix'), Transition(label='Community Meet'))
root.order.add_edge(Transition(label='Nutrient Mix'), Transition(label='Harvest Plan'))
root.order.add_edge(Transition(label='Nutrient Mix'), Transition(label='Packaging Design'))
root.order.add_edge(Transition(label='Nutrient Mix'), Transition(label='Distribution Map'))
root.order.add_edge(Transition(label='Nutrient Mix'), Transition(label='Feedback Loop'))
root.order.add_edge(Transition(label='Nutrient Mix'), Transition(label='Maintenance Schedule'))

root.order.add_edge(Transition(label='Sensor Install'), Transition(label='Pest Monitor'))
root.order.add_edge(Transition(label='Sensor Install'), Transition(label='Data Analysis'))
root.order.add_edge(Transition(label='Sensor Install'), Transition(label='Regulation Review'))
root.order.add_edge(Transition(label='Sensor Install'), Transition(label='Community Meet'))
root.order.add_edge(Transition(label='Sensor Install'), Transition(label='Harvest Plan'))
root.order.add_edge(Transition(label='Sensor Install'), Transition(label='Packaging Design'))
root.order.add_edge(Transition(label='Sensor Install'), Transition(label='Distribution Map'))
root.order.add_edge(Transition(label='Sensor Install'), Transition(label='Feedback Loop'))
root.order.add_edge(Transition(label='Sensor Install'), Transition(label='Maintenance Schedule'))

root.order.add_edge(Transition(label='Pest Monitor'), Transition(label='Data Analysis'))
root.order.add_edge(Transition(label='Pest Monitor'), Transition(label='Regulation Review'))
root.order.add_edge(Transition(label='Pest Monitor'), Transition(label='Community Meet'))
root.order.add_edge(Transition(label='Pest Monitor'), Transition(label='Harvest Plan'))
root.order.add_edge(Transition(label='Pest Monitor'), Transition(label='Packaging Design'))
root.order.add_edge(Transition(label='Pest Monitor'), Transition(label='Distribution Map'))
root.order.add_edge(Transition(label='Pest Monitor'), Transition(label='Feedback Loop'))
root.order.add_edge(Transition(label='Pest Monitor'), Transition(label='Maintenance Schedule'))

root.order.add_edge(Transition(label='Data Analysis'), Transition(label='Regulation Review'))
root.order.add_edge(Transition(label='Data Analysis'), Transition(label='Community Meet'))
root.order.add_edge(Transition(label='Data Analysis'), Transition(label='Harvest Plan'))
root.order.add_edge(Transition(label='Data Analysis'), Transition(label='Packaging Design'))
root.order.add_edge(Transition(label='Data Analysis'), Transition(label='Distribution Map'))
root.order.add_edge(Transition(label='Data Analysis'), Transition(label='Feedback Loop'))
root.order.add_edge(Transition(label='Data Analysis'), Transition(label='Maintenance Schedule'))

root.order.add_edge(Transition(label='Regulation Review'), Transition(label='Community Meet'))
root.order.add_edge(Transition(label='Regulation Review'), Transition(label='Harvest Plan'))
root.order.add_edge(Transition(label='Regulation Review'), Transition(label='Packaging Design'))
root.order.add_edge(Transition(label='Regulation Review'), Transition(label='Distribution Map'))
root.order.add_edge(Transition(label='Regulation Review'), Transition(label='Feedback Loop'))
root.order.add_edge(Transition(label='Regulation Review'), Transition(label='Maintenance Schedule'))

root.order.add_edge(Transition(label='Community Meet'), Transition(label='Harvest Plan'))
root.order.add_edge(Transition(label='Community Meet'), Transition(label='Packaging Design'))
root.order.add_edge(Transition(label='Community Meet'), Transition(label='Distribution Map'))
root.order.add_edge(Transition(label='Community Meet'), Transition(label='Feedback Loop'))
root.order.add_edge(Transition(label='Community Meet'), Transition(label='Maintenance Schedule'))

root.order.add_edge(Transition(label='Harvest Plan'), Transition(label='Packaging Design'))
root.order.add_edge(Transition(label='Harvest Plan'), Transition(label='Distribution Map'))
root.order.add_edge(Transition(label='Harvest Plan'), Transition(label='Feedback Loop'))
root.order.add_edge(Transition(label='Harvest Plan'), Transition(label='Maintenance Schedule'))

root.order.add_edge(Transition(label='Packaging Design'), Transition(label='Distribution Map'))
root.order.add_edge(Transition(label='Packaging Design'), Transition(label='Feedback Loop'))
root.order.add_edge(Transition(label='Packaging Design'), Transition(label='Maintenance Schedule'))

root.order.add_edge(Transition(label='Distribution Map'), Transition(label='Feedback Loop'))
root.order.add_edge(Transition(label='Distribution Map'), Transition(label='Maintenance Schedule'))

root.order.add_edge(Transition(label='Feedback Loop'), Transition(label='Maintenance Schedule'))