from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their exact names
activities = {
    'Seed Select': Transition(label='Seed Select'),
    'Trend Analyze': Transition(label='Trend Analyze'),
    'Nutrient Mix': Transition(label='Nutrient Mix'),
    'Auto Plant': Transition(label='Auto Plant'),
    'Sensor Check': Transition(label='Sensor Check'),
    'Data Analyze': Transition(label='Data Analyze'),
    'Water Adjust': Transition(label='Water Adjust'),
    'Light Control': Transition(label='Light Control'),
    'Humidity Monitor': Transition(label='Humidity Monitor'),
    'Pest Inspect': Transition(label='Pest Inspect'),
    'Growth Forecast': Transition(label='Growth Forecast'),
    'Harvest Plan': Transition(label='Harvest Plan'),
    'Rapid Cool': Transition(label='Rapid Cool'),
    'Quality Grade': Transition(label='Quality Grade'),
    'Eco Package': Transition(label='Eco Package'),
    'Logistics Prep': Transition(label='Logistics Prep'),
    'Feedback Collect': Transition(label='Feedback Collect'),
    'System Maintain': Transition(label='System Maintain')
}

# Create the POWL model
root = StrictPartialOrder(nodes=list(activities.values()))

# Define the dependencies between activities
root.order.add_edge(activities['Seed Select'], activities['Trend Analyze'])
root.order.add_edge(activities['Trend Analyze'], activities['Nutrient Mix'])
root.order.add_edge(activities['Nutrient Mix'], activities['Auto Plant'])
root.order.add_edge(activities['Auto Plant'], activities['Sensor Check'])
root.order.add_edge(activities['Sensor Check'], activities['Data Analyze'])
root.order.add_edge(activities['Data Analyze'], activities['Water Adjust'])
root.order.add_edge(activities['Data Analyze'], activities['Light Control'])
root.order.add_edge(activities['Data Analyze'], activities['Humidity Monitor'])
root.order.add_edge(activities['Data Analyze'], activities['Pest Inspect'])
root.order.add_edge(activities['Water Adjust'], activities['Growth Forecast'])
root.order.add_edge(activities['Growth Forecast'], activities['Harvest Plan'])
root.order.add_edge(activities['Harvest Plan'], activities['Rapid Cool'])
root.order.add_edge(activities['Rapid Cool'], activities['Quality Grade'])
root.order.add_edge(activities['Quality Grade'], activities['Eco Package'])
root.order.add_edge(activities['Eco Package'], activities['Logistics Prep'])
root.order.add_edge(activities['Logistics Prep'], activities['Feedback Collect'])
root.order.add_edge(activities['Feedback Collect'], activities['System Maintain'])

print(root)