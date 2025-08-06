root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Regulation Check'),
    Transition(label='Modular Design'),
    Transition(label='Material Sourcing'),
    Transition(label='Energy Integration'),
    Transition(label='Climate Setup'),
    Transition(label='Nutrient Mix'),
    Transition(label='System Assembly'),
    Transition(label='Automation Config'),
    Transition(label='Crop Seeding'),
    Transition(label='Growth Monitoring'),
    Transition(label='Waste Handling'),
    Transition(label='Community Meet'),
    Transition(label='Data Analysis'),
    Transition(label='Feedback Loop'),
    Transition(label='Yield Forecast')
])

root.order.add_edge(Transition(label='Site Survey'), Transition(label='Regulation Check'))
root.order.add_edge(Transition(label='Site Survey'), Transition(label='Modular Design'))
root.order.add_edge(Transition(label='Site Survey'), Transition(label='Material Sourcing'))
root.order.add_edge(Transition(label='Site Survey'), Transition(label='Energy Integration'))
root.order.add_edge(Transition(label='Site Survey'), Transition(label='Climate Setup'))
root.order.add_edge(Transition(label='Site Survey'), Transition(label='Nutrient Mix'))
root.order.add_edge(Transition(label='Site Survey'), Transition(label='System Assembly'))
root.order.add_edge(Transition(label='Site Survey'), Transition(label='Automation Config'))
root.order.add_edge(Transition(label='Site Survey'), Transition(label='Crop Seeding'))
root.order.add_edge(Transition(label='Site Survey'), Transition(label='Growth Monitoring'))
root.order.add_edge(Transition(label='Site Survey'), Transition(label='Waste Handling'))
root.order.add_edge(Transition(label='Site Survey'), Transition(label='Community Meet'))
root.order.add_edge(Transition(label='Site Survey'), Transition(label='Data Analysis'))
root.order.add_edge(Transition(label='Site Survey'), Transition(label='Feedback Loop'))
root.order.add_edge(Transition(label='Site Survey'), Transition(label='Yield Forecast'))

root.order.add_edge(Transition(label='Regulation Check'), Transition(label='Modular Design'))
root.order.add_edge(Transition(label='Regulation Check'), Transition(label='Material Sourcing'))
root.order.add_edge(Transition(label='Regulation Check'), Transition(label='Energy Integration'))
root.order.add_edge(Transition(label='Regulation Check'), Transition(label='Climate Setup'))
root.order.add_edge(Transition(label='Regulation Check'), Transition(label='Nutrient Mix'))
root.order.add_edge(Transition(label='Regulation Check'), Transition(label='System Assembly'))
root.order.add_edge(Transition(label='Regulation Check'), Transition(label='Automation Config'))
root.order.add_edge(Transition(label='Regulation Check'), Transition(label='Crop Seeding'))
root.order.add_edge(Transition(label='Regulation Check'), Transition(label='Growth Monitoring'))
root.order.add_edge(Transition(label='Regulation Check'), Transition(label='Waste Handling'))
root.order.add_edge(Transition(label='Regulation Check'), Transition(label='Community Meet'))
root.order.add_edge(Transition(label='Regulation Check'), Transition(label='Data Analysis'))
root.order.add_edge(Transition(label='Regulation Check'), Transition(label='Feedback Loop'))
root.order.add_edge(Transition(label='Regulation Check'), Transition(label='Yield Forecast'))

root.order.add_edge(Transition(label='Modular Design'), Transition(label='Material Sourcing'))
root.order.add_edge(Transition(label='Modular Design'), Transition(label='Energy Integration'))
root.order.add_edge(Transition(label='Modular Design'), Transition(label='Climate Setup'))
root.order.add_edge(Transition(label='Modular Design'), Transition(label='Nutrient Mix'))
root.order.add_edge(Transition(label='Modular Design'), Transition(label='System Assembly'))
root.order.add_edge(Transition(label='Modular Design'), Transition(label='Automation Config'))
root.order.add_edge(Transition(label='Modular Design'), Transition(label='Crop Seeding'))
root.order.add_edge(Transition(label='Modular Design'), Transition(label='Growth Monitoring'))
root.order.add_edge(Transition(label='Modular Design'), Transition(label='Waste Handling'))
root.order.add_edge(Transition(label='Modular Design'), Transition(label='Community Meet'))
root.order.add_edge(Transition(label='Modular Design'), Transition(label='Data Analysis'))
root.order.add_edge(Transition(label='Modular Design'), Transition(label='Feedback Loop'))
root.order.add_edge(Transition(label='Modular Design'), Transition(label='Yield Forecast'))

root.order.add_edge(Transition(label='Material Sourcing'), Transition(label='Energy Integration'))
root.order.add_edge(Transition(label='Material Sourcing'), Transition(label='Climate Setup'))
root.order.add_edge(Transition(label='Material Sourcing'), Transition(label='Nutrient Mix'))
root.order.add_edge(Transition(label='Material Sourcing'), Transition(label='System Assembly'))
root.order.add_edge(Transition(label='Material Sourcing'), Transition(label='Automation Config'))
root.order.add_edge(Transition(label='Material Sourcing'), Transition(label='Crop Seeding'))
root.order.add_edge(Transition(label='Material Sourcing'), Transition(label='Growth Monitoring'))
root.order.add_edge(Transition(label='Material Sourcing'), Transition(label='Waste Handling'))
root.order.add_edge(Transition(label='Material Sourcing'), Transition(label='Community Meet'))
root.order.add_edge(Transition(label='Material Sourcing'), Transition(label='Data Analysis'))
root.order.add_edge(Transition(label='Material Sourcing'), Transition(label='Feedback Loop'))
root.order.add_edge(Transition(label='Material Sourcing'), Transition(label='Yield Forecast'))

root.order.add_edge(Transition(label='Energy Integration'), Transition(label='Climate Setup'))
root.order.add_edge(Transition(label='Energy Integration'), Transition(label='Nutrient Mix'))
root.order.add_edge(Transition(label='Energy Integration'), Transition(label='System Assembly'))
root.order.add_edge(Transition(label='Energy Integration'), Transition(label='Automation Config'))
root.order.add_edge(Transition(label='Energy Integration'), Transition(label='Crop Seeding'))
root.order.add_edge(Transition(label='Energy Integration'), Transition(label='Growth Monitoring'))
root.order.add_edge(Transition(label='Energy Integration'), Transition(label='Waste Handling'))
root.order.add_edge(Transition(label='Energy Integration'), Transition(label='Community Meet'))
root.order.add_edge(Transition(label='Energy Integration'), Transition(label='Data Analysis'))
root.order.add_edge(Transition(label='Energy Integration'), Transition(label='Feedback Loop'))
root.order.add_edge(Transition(label='Energy Integration'), Transition(label='Yield Forecast'))

root.order.add_edge(Transition(label='Climate Setup'), Transition(label='Nutrient Mix'))
root.order.add_edge(Transition(label='Climate Setup'), Transition(label='System Assembly'))
root.order.add_edge(Transition(label='Climate Setup'), Transition(label='Automation Config'))
root.order.add_edge(Transition(label='Climate Setup'), Transition(label='Crop Seeding'))
root.order.add_edge(Transition(label='Climate Setup'), Transition(label='Growth Monitoring'))
root.order.add_edge(Transition(label='Climate Setup'), Transition(label='Waste Handling'))
root.order.add_edge(Transition(label='Climate Setup'), Transition(label='Community Meet'))
root.order.add_edge(Transition(label='Climate Setup'), Transition(label='Data Analysis'))
root.order.add_edge(Transition(label='Climate Setup'), Transition(label='Feedback Loop'))
root.order.add_edge(Transition(label='Climate Setup'), Transition(label='Yield Forecast'))

root.order.add_edge(Transition(label='Nutrient Mix'), Transition(label='System Assembly'))
root.order.add_edge(Transition(label='Nutrient Mix'), Transition(label='Automation Config'))
root.order.add_edge(Transition(label='Nutrient Mix'), Transition(label='Crop Seeding'))
root.order.add_edge(Transition(label='Nutrient Mix'), Transition(label='Growth Monitoring'))
root.order.add_edge(Transition(label='Nutrient Mix'), Transition(label='Waste Handling'))
root.order.add_edge(Transition(label='Nutrient Mix'), Transition(label='Community Meet'))
root.order.add_edge(Transition(label='Nutrient Mix'), Transition(label='Data Analysis'))
root.order.add_edge(Transition(label='Nutrient Mix'), Transition(label='Feedback Loop'))
root.order.add_edge(Transition(label='Nutrient Mix'), Transition(label='Yield Forecast'))

root.order.add_edge(Transition(label='System Assembly'), Transition(label='Automation Config'))
root.order.add_edge(Transition(label='System Assembly'), Transition(label='Crop Seeding'))
root.order.add_edge(Transition(label='System Assembly'), Transition(label='Growth Monitoring'))
root.order.add_edge(Transition(label='System Assembly'), Transition(label='Waste Handling'))
root.order.add_edge(Transition(label='System Assembly'), Transition(label='Community Meet'))
root.order.add_edge(Transition(label='System Assembly'), Transition(label='Data Analysis'))
root.order.add_edge(Transition(label='System Assembly'), Transition(label='Feedback Loop'))
root.order.add_edge(Transition(label='System Assembly'), Transition(label='Yield Forecast'))

root.order.add_edge(Transition(label='Automation Config'), Transition(label='Crop Seeding'))
root.order.add_edge(Transition(label='Automation Config'), Transition(label='Growth Monitoring'))
root.order.add_edge(Transition(label='Automation Config'), Transition(label='Waste Handling'))
root.order.add_edge(Transition(label='Automation Config'), Transition(label='Community Meet'))
root.order.add_edge(Transition(label='Automation Config'), Transition(label='Data Analysis'))
root.order.add_edge(Transition(label='Automation Config'), Transition(label='Feedback Loop'))
root.order.add_edge(Transition(label='Automation Config'), Transition(label='Yield Forecast'))

root.order.add_edge(Transition(label='Crop Seeding'), Transition(label='Growth Monitoring'))
root.order.add_edge(Transition(label='Crop Seeding'), Transition(label='Waste Handling'))
root.order.add_edge(Transition(label='Crop Seeding'), Transition(label='Community Meet'))
root.order.add_edge(Transition(label='Crop Seeding'), Transition(label='Data Analysis'))
root.order.add_edge(Transition(label='Crop Seeding'), Transition(label='Feedback Loop'))
root.order.add_edge(Transition(label='Crop Seeding'), Transition(label='Yield Forecast'))

root.order.add_edge(Transition(label='Growth Monitoring'), Transition(label='Waste Handling'))
root.order.add_edge(Transition(label='Growth Monitoring'), Transition(label='Community Meet'))
root.order.add_edge(Transition(label='Growth Monitoring'), Transition(label='Data Analysis'))
root.order.add_edge(Transition(label='Growth Monitoring'), Transition(label='Feedback Loop'))
root.order.add_edge(Transition(label='Growth Monitoring'), Transition(label='Yield Forecast'))

root.order.add_edge(Transition(label='Waste Handling'), Transition(label='Community Meet'))
root.order.add_edge(Transition(label='Waste Handling'), Transition(label='Data Analysis'))
root.order.add_edge(Transition(label='Waste Handling'), Transition(label='Feedback Loop'))
root.order.add_edge(Transition(label='Waste Handling'), Transition(label='Yield Forecast'))

root.order.add_edge(Transition(label='Community Meet'), Transition(label='Data Analysis'))
root.order.add_edge(Transition(label='Community Meet'), Transition(label='Feedback Loop'))
root.order.add_edge(Transition(label='Community Meet'), Transition(label='Yield Forecast'))

root.order.add_edge(Transition(label='Data Analysis'), Transition(label='Feedback Loop'))
root.order.add_edge(Transition(label='Data Analysis'), Transition(label='Yield Forecast'))

root.order.add_edge(Transition(label='Feedback Loop'), Transition(label='Yield Forecast'))