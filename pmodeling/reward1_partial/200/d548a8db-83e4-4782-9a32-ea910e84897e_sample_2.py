import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
activities = ['Seed Selection', 'Nutrient Setup', 'Growth Monitoring', 'Climate Adjust', 'Pest Control', 'Water Recirculate', 'Light Calibration', 'Robotic Harvest', 'Quality Inspect', 'Waste Process', 'Energy Reuse', 'Inventory Update', 'Demand Forecast', 'Order Dispatch', 'Community Event', 'Feedback Collect', 'Data Analyze']

# Create transitions for each activity
transitions = {activity: Transition(label=activity) for activity in activities}

# Define the control flow
root = StrictPartialOrder(nodes=[transitions['Seed Selection'], transitions['Nutrient Setup'], transitions['Growth Monitoring'], transitions['Climate Adjust'], transitions['Pest Control'], transitions['Water Recirculate'], transitions['Light Calibration'], transitions['Robotic Harvest'], transitions['Quality Inspect'], transitions['Waste Process'], transitions['Energy Reuse'], transitions['Inventory Update'], transitions['Demand Forecast'], transitions['Order Dispatch'], transitions['Community Event'], transitions['Feedback Collect'], transitions['Data Analyze']])
root.order.add_edge(transitions['Seed Selection'], transitions['Nutrient Setup'])
root.order.add_edge(transitions['Nutrient Setup'], transitions['Growth Monitoring'])
root.order.add_edge(transitions['Growth Monitoring'], transitions['Climate Adjust'])
root.order.add_edge(transitions['Climate Adjust'], transitions['Pest Control'])
root.order.add_edge(transitions['Pest Control'], transitions['Water Recirculate'])
root.order.add_edge(transitions['Water Recirculate'], transitions['Light Calibration'])
root.order.add_edge(transitions['Light Calibration'], transitions['Robotic Harvest'])
root.order.add_edge(transitions['Robotic Harvest'], transitions['Quality Inspect'])
root.order.add_edge(transitions['Quality Inspect'], transitions['Waste Process'])
root.order.add_edge(transitions['Waste Process'], transitions['Energy Reuse'])
root.order.add_edge(transitions['Energy Reuse'], transitions['Inventory Update'])
root.order.add_edge(transitions['Inventory Update'], transitions['Demand Forecast'])
root.order.add_edge(transitions['Demand Forecast'], transitions['Order Dispatch'])
root.order.add_edge(transitions['Order Dispatch'], transitions['Community Event'])
root.order.add_edge(transitions['Community Event'], transitions['Feedback Collect'])
root.order.add_edge(transitions['Feedback Collect'], transitions['Data Analyze'])

print(root)