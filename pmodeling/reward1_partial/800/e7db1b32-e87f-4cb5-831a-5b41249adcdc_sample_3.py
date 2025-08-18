import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their labels
activities = {
    'Seed Selection': Transition(label='Seed Selection'),
    'AI Prediction': Transition(label='AI Prediction'),
    'Automated Planting': Transition(label='Automated Planting'),
    'Sensor Calibration': Transition(label='Sensor Calibration'),
    'Environment Adjust': Transition(label='Environment Adjust'),
    'Nutrient Dosing': Transition(label='Nutrient Dosing'),
    'Hydroponic Flow': Transition(label='Hydroponic Flow'),
    'Robotic Pruning': Transition(label='Robotic Pruning'),
    'Health Monitor': Transition(label='Health Monitor'),
    'Harvesting Ops': Transition(label='Harvesting Ops'),
    'Data Analysis': Transition(label='Data Analysis'),
    'Predictive Check': Transition(label='Predictive Check'),
    'Waste Composting': Transition(label='Waste Composting'),
    'Water Recycling': Transition(label='Water Recycling'),
    'Eco Packaging': Transition(label='Eco Packaging'),
    'Carbon Tracking': Transition(label='Carbon Tracking'),
    'Logistics Dispatch': Transition(label='Logistics Dispatch')
}

# Create the POWL model
root = StrictPartialOrder(nodes=list(activities.values()))

# Define the dependencies (order) between activities
root.order.add_edge(activities['Seed Selection'], activities['AI Prediction'])
root.order.add_edge(activities['AI Prediction'], activities['Automated Planting'])
root.order.add_edge(activities['Automated Planting'], activities['Sensor Calibration'])
root.order.add_edge(activities['Sensor Calibration'], activities['Environment Adjust'])
root.order.add_edge(activities['Environment Adjust'], activities['Nutrient Dosing'])
root.order.add_edge(activities['Nutrient Dosing'], activities['Hydroponic Flow'])
root.order.add_edge(activities['Hydroponic Flow'], activities['Robotic Pruning'])
root.order.add_edge(activities['Robotic Pruning'], activities['Health Monitor'])
root.order.add_edge(activities['Health Monitor'], activities['Harvesting Ops'])
root.order.add_edge(activities['Harvesting Ops'], activities['Data Analysis'])
root.order.add_edge(activities['Data Analysis'], activities['Predictive Check'])
root.order.add_edge(activities['Predictive Check'], activities['Waste Composting'])
root.order.add_edge(activities['Waste Composting'], activities['Water Recycling'])
root.order.add_edge(activities['Water Recycling'], activities['Eco Packaging'])
root.order.add_edge(activities['Eco Packaging'], activities['Carbon Tracking'])
root.order.add_edge(activities['Carbon Tracking'], activities['Logistics Dispatch'])

# Print the root POWL model
print(root)