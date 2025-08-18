import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with exact names
activities = {
    'Seed Selection': Transition(label='Seed Selection'),
    'Nutrient Setup': Transition(label='Nutrient Setup'),
    'Growth Monitoring': Transition(label='Growth Monitoring'),
    'Climate Adjust': Transition(label='Climate Adjust'),
    'Pest Control': Transition(label='Pest Control'),
    'Water Recirculate': Transition(label='Water Recirculate'),
    'Light Calibration': Transition(label='Light Calibration'),
    'Robotic Harvest': Transition(label='Robotic Harvest'),
    'Quality Inspect': Transition(label='Quality Inspect'),
    'Waste Process': Transition(label='Waste Process'),
    'Energy Reuse': Transition(label='Energy Reuse'),
    'Inventory Update': Transition(label='Inventory Update'),
    'Demand Forecast': Transition(label='Demand Forecast'),
    'Order Dispatch': Transition(label='Order Dispatch'),
    'Community Event': Transition(label='Community Event'),
    'Feedback Collect': Transition(label='Feedback Collect'),
    'Data Analyze': Transition(label='Data Analyze')
}

# Define the POWL model
root = StrictPartialOrder(nodes=[activities['Seed Selection'], activities['Nutrient Setup'], activities['Growth Monitoring'], activities['Climate Adjust'], activities['Pest Control'], activities['Water Recirculate'], activities['Light Calibration'], activities['Robotic Harvest'], activities['Quality Inspect'], activities['Waste Process'], activities['Energy Reuse'], activities['Inventory Update'], activities['Demand Forecast'], activities['Order Dispatch'], activities['Community Event'], activities['Feedback Collect'], activities['Data Analyze']])

# Define the dependencies
root.order.add_edge(activities['Seed Selection'], activities['Nutrient Setup'])
root.order.add_edge(activities['Nutrient Setup'], activities['Growth Monitoring'])
root.order.add_edge(activities['Growth Monitoring'], activities['Climate Adjust'])
root.order.add_edge(activities['Climate Adjust'], activities['Pest Control'])
root.order.add_edge(activities['Pest Control'], activities['Water Recirculate'])
root.order.add_edge(activities['Water Recirculate'], activities['Light Calibration'])
root.order.add_edge(activities['Light Calibration'], activities['Robotic Harvest'])
root.order.add_edge(activities['Robotic Harvest'], activities['Quality Inspect'])
root.order.add_edge(activities['Quality Inspect'], activities['Waste Process'])
root.order.add_edge(activities['Waste Process'], activities['Energy Reuse'])
root.order.add_edge(activities['Energy Reuse'], activities['Inventory Update'])
root.order.add_edge(activities['Inventory Update'], activities['Demand Forecast'])
root.order.add_edge(activities['Demand Forecast'], activities['Order Dispatch'])
root.order.add_edge(activities['Order Dispatch'], activities['Community Event'])
root.order.add_edge(activities['Community Event'], activities['Feedback Collect'])
root.order.add_edge(activities['Feedback Collect'], activities['Data Analyze'])

# Print the result
print(root)