root = StrictPartialOrder(nodes=[
    Transition(label='Site Prep'),
    Transition(label='Seed Select'),
    Transition(label='Nutrient Mix'),
    Transition(label='Planting Rows'),
    Transition(label='Env Monitor'),
    Transition(label='Water Adjust'),
    Transition(label='Pest Control'),
    Transition(label='Growth Check'),
    Transition(label='Light Calibrate'),
    Transition(label='Energy Manage'),
    Transition(label='Harvest Crop'),
    Transition(label='Quality Sort'),
    Transition(label='Pack Goods'),
    Transition(label='Cold Store'),
    Transition(label='Market Ship'),
    Transition(label='Data Analyze')
])

root.order.add_edge(Transition(label='Site Prep'), Transition(label='Seed Select'))
root.order.add_edge(Transition(label='Seed Select'), Transition(label='Nutrient Mix'))
root.order.add_edge(Transition(label='Nutrient Mix'), Transition(label='Planting Rows'))
root.order.add_edge(Transition(label='Planting Rows'), Transition(label='Env Monitor'))
root.order.add_edge(Transition(label='Env Monitor'), Transition(label='Water Adjust'))
root.order.add_edge(Transition(label='Water Adjust'), Transition(label='Pest Control'))
root.order.add_edge(Transition(label='Pest Control'), Transition(label='Growth Check'))
root.order.add_edge(Transition(label='Growth Check'), Transition(label='Light Calibrate'))
root.order.add_edge(Transition(label='Light Calibrate'), Transition(label='Energy Manage'))
root.order.add_edge(Transition(label='Energy Manage'), Transition(label='Harvest Crop'))
root.order.add_edge(Transition(label='Harvest Crop'), Transition(label='Quality Sort'))
root.order.add_edge(Transition(label='Quality Sort'), Transition(label='Pack Goods'))
root.order.add_edge(Transition(label='Pack Goods'), Transition(label='Cold Store'))
root.order.add_edge(Transition(label='Cold Store'), Transition(label='Market Ship'))
root.order.add_edge(Transition(label='Market Ship'), Transition(label='Data Analyze'))

root.order.add_edge(Transition(label='Site Prep'), Transition(label='Data Analyze'))
root.order.add_edge(Transition(label='Seed Select'), Transition(label='Data Analyze'))
root.order.add_edge(Transition(label='Nutrient Mix'), Transition(label='Data Analyze'))
root.order.add_edge(Transition(label='Planting Rows'), Transition(label='Data Analyze'))
root.order.add_edge(Transition(label='Env Monitor'), Transition(label='Data Analyze'))
root.order.add_edge(Transition(label='Water Adjust'), Transition(label='Data Analyze'))
root.order.add_edge(Transition(label='Pest Control'), Transition(label='Data Analyze'))
root.order.add_edge(Transition(label='Growth Check'), Transition(label='Data Analyze'))
root.order.add_edge(Transition(label='Light Calibrate'), Transition(label='Data Analyze'))
root.order.add_edge(Transition(label='Energy Manage'), Transition(label='Data Analyze'))
root.order.add_edge(Transition(label='Harvest Crop'), Transition(label='Data Analyze'))
root.order.add_edge(Transition(label='Quality Sort'), Transition(label='Data Analyze'))
root.order.add_edge(Transition(label='Pack Goods'), Transition(label='Data Analyze'))
root.order.add_edge(Transition(label='Cold Store'), Transition(label='Data Analyze'))
root.order.add_edge(Transition(label='Market Ship'), Transition(label='Data Analyze'))