root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Rack Design'),
    Transition(label='System Setup'),
    Transition(label='Climate Calibrate'),
    Transition(label='Nutrient Prep'),
    Transition(label='Crop Select'),
    Transition(label='Seed Germinate'),
    Transition(label='Sensor Deploy'),
    Transition(label='Pest Control'),
    Transition(label='Harvest Automate'),
    Transition(label='Quality Check'),
    Transition(label='Pack Produce'),
    Transition(label='Data Analyze'),
    Transition(label='Engage Community'),
    Transition(label='Logistics Plan')
])

root.order.add_edge(Transition(label='Site Survey'), Transition(label='Rack Design'))
root.order.add_edge(Transition(label='Rack Design'), Transition(label='System Setup'))
root.order.add_edge(Transition(label='System Setup'), Transition(label='Climate Calibrate'))
root.order.add_edge(Transition(label='Climate Calibrate'), Transition(label='Nutrient Prep'))
root.order.add_edge(Transition(label='Nutrient Prep'), Transition(label='Crop Select'))
root.order.add_edge(Transition(label='Crop Select'), Transition(label='Seed Germinate'))
root.order.add_edge(Transition(label='Seed Germinate'), Transition(label='Sensor Deploy'))
root.order.add_edge(Transition(label='Sensor Deploy'), Transition(label='Pest Control'))
root.order.add_edge(Transition(label='Pest Control'), Transition(label='Harvest Automate'))
root.order.add_edge(Transition(label='Harvest Automate'), Transition(label='Quality Check'))
root.order.add_edge(Transition(label='Quality Check'), Transition(label='Pack Produce'))
root.order.add_edge(Transition(label='Pack Produce'), Transition(label='Data Analyze'))
root.order.add_edge(Transition(label='Data Analyze'), Transition(label='Engage Community'))
root.order.add_edge(Transition(label='Engage Community'), Transition(label='Logistics Plan'))