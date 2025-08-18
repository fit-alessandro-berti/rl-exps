import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their labels
activities = {
    'Seed Select': Transition(label='Seed Select'),
    'Nutrient Mix': Transition(label='Nutrient Mix'),
    'Climate Adjust': Transition(label='Climate Adjust'),
    'Planting Robotic': Transition(label='Planting Robotic'),
    'Growth Monitor': Transition(label='Growth Monitor'),
    'Pest Control': Transition(label='Pest Control'),
    'Water Recycle': Transition(label='Water Recycle'),
    'Light Optimize': Transition(label='Light Optimize'),
    'Growth Analyze': Transition(label='Growth Analyze'),
    'Harvest Sync': Transition(label='Harvest Sync'),
    'Sterilize Crop': Transition(label='Sterilize Crop'),
    'Package Fresh': Transition(label='Package Fresh'),
    'Demand Forecast': Transition(label='Demand Forecast'),
    'Delivery Plan': Transition(label='Delivery Plan'),
    'Data Feedback': Transition(label='Data Feedback')
}

# Construct the partial order based on the described workflow
root = StrictPartialOrder()

# Add activities to the root
root.add_node(activities['Seed Select'])
root.add_node(activities['Nutrient Mix'])
root.add_node(activities['Climate Adjust'])
root.add_node(activities['Planting Robotic'])
root.add_node(activities['Growth Monitor'])
root.add_node(activities['Pest Control'])
root.add_node(activities['Water Recycle'])
root.add_node(activities['Light Optimize'])
root.add_node(activities['Growth Analyze'])
root.add_node(activities['Harvest Sync'])
root.add_node(activities['Sterilize Crop'])
root.add_node(activities['Package Fresh'])
root.add_node(activities['Demand Forecast'])
root.add_node(activities['Delivery Plan'])
root.add_node(activities['Data Feedback'])

# Define the dependencies between activities
root.add_edge(activities['Seed Select'], activities['Nutrient Mix'])
root.add_edge(activities['Nutrient Mix'], activities['Climate Adjust'])
root.add_edge(activities['Climate Adjust'], activities['Planting Robotic'])
root.add_edge(activities['Planting Robotic'], activities['Growth Monitor'])
root.add_edge(activities['Growth Monitor'], activities['Pest Control'])
root.add_edge(activities['Pest Control'], activities['Water Recycle'])
root.add_edge(activities['Water Recycle'], activities['Light Optimize'])
root.add_edge(activities['Light Optimize'], activities['Growth Analyze'])
root.add_edge(activities['Growth Analyze'], activities['Harvest Sync'])
root.add_edge(activities['Harvest Sync'], activities['Sterilize Crop'])
root.add_edge(activities['Sterilize Crop'], activities['Package Fresh'])
root.add_edge(activities['Package Fresh'], activities['Demand Forecast'])
root.add_edge(activities['Demand Forecast'], activities['Delivery Plan'])
root.add_edge(activities['Delivery Plan'], activities['Data Feedback'])

# Print the root to verify the model
print(root)