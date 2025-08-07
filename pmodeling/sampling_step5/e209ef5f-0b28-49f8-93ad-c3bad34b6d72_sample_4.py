import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities with their labels
activities = {
    'Soil Analyze': Transition(label='Soil Analyze'),
    'Site Mapping': Transition(label='Site Mapping'),
    'Bed Setup': Transition(label='Bed Setup'),
    'Crop Select': Transition(label='Crop Select'),
    'Sensor Deploy': Transition(label='Sensor Deploy'),
    'Irrigation Adjust': Transition(label='Irrigation Adjust'),
    'Nutrient Feed': Transition(label='Nutrient Feed'),
    'Pest Scouting': Transition(label='Pest Scouting'),
    'Pest Predict': Transition(label='Pest Predict'),
    'Workshop Host': Transition(label='Workshop Host'),
    'Crop Rotate': Transition(label='Crop Rotate'),
    'Waste Compost': Transition(label='Waste Compost'),
    'Water Recycle': Transition(label='Water Recycle'),
    'Data Analyze': Transition(label='Data Analyze'),
    'Cycle Refine': Transition(label='Cycle Refine'),
    'Resource Share': Transition(label='Resource Share'),
    'Yield Report': Transition(label='Yield Report')
}

# Define the POWL model
root = StrictPartialOrder(nodes=list(activities.values()))

# Define the control flow
root.order.add_edge(activities['Soil Analyze'], activities['Site Mapping'])
root.order.add_edge(activities['Site Mapping'], activities['Bed Setup'])
root.order.add_edge(activities['Bed Setup'], activities['Crop Select'])
root.order.add_edge(activities['Crop Select'], activities['Sensor Deploy'])
root.order.add_edge(activities['Sensor Deploy'], activities['Irrigation Adjust'])
root.order.add_edge(activities['Irrigation Adjust'], activities['Nutrient Feed'])
root.order.add_edge(activities['Nutrient Feed'], activities['Pest Scouting'])
root.order.add_edge(activities['Pest Scouting'], activities['Pest Predict'])
root.order.add_edge(activities['Pest Predict'], activities['Workshop Host'])
root.order.add_edge(activities['Workshop Host'], activities['Crop Rotate'])
root.order.add_edge(activities['Crop Rotate'], activities['Waste Compost'])
root.order.add_edge(activities['Waste Compost'], activities['Water Recycle'])
root.order.add_edge(activities['Water Recycle'], activities['Data Analyze'])
root.order.add_edge(activities['Data Analyze'], activities['Cycle Refine'])
root.order.add_edge(activities['Cycle Refine'], activities['Resource Share'])
root.order.add_edge(activities['Resource Share'], activities['Yield Report'])

# Print the final POWL model
print(root)