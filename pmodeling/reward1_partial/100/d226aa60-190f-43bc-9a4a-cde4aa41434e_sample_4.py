import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the nodes and edges for the POWL model
nodes = [
    activities['Seed Select'],
    activities['Trend Analyze'],
    activities['Nutrient Mix'],
    activities['Auto Plant'],
    activities['Sensor Check'],
    activities['Data Analyze'],
    activities['Water Adjust'],
    activities['Light Control'],
    activities['Humidity Monitor'],
    activities['Pest Inspect'],
    activities['Growth Forecast'],
    activities['Harvest Plan'],
    activities['Rapid Cool'],
    activities['Quality Grade'],
    activities['Eco Package'],
    activities['Logistics Prep'],
    activities['Feedback Collect'],
    activities['System Maintain']
]

# Define the dependencies between nodes
order = {
    ('Seed Select', 'Trend Analyze'): True,
    ('Trend Analyze', 'Nutrient Mix'): True,
    ('Nutrient Mix', 'Auto Plant'): True,
    ('Auto Plant', 'Sensor Check'): True,
    ('Sensor Check', 'Data Analyze'): True,
    ('Data Analyze', 'Water Adjust'): True,
    ('Data Analyze', 'Light Control'): True,
    ('Data Analyze', 'Humidity Monitor'): True,
    ('Data Analyze', 'Pest Inspect'): True,
    ('Data Analyze', 'Growth Forecast'): True,
    ('Data Analyze', 'Harvest Plan'): True,
    ('Water Adjust', 'Rapid Cool'): True,
    ('Light Control', 'Rapid Cool'): True,
    ('Humidity Monitor', 'Rapid Cool'): True,
    ('Pest Inspect', 'Rapid Cool'): True,
    ('Growth Forecast', 'Rapid Cool'): True,
    ('Harvest Plan', 'Rapid Cool'): True,
    ('Rapid Cool', 'Quality Grade'): True,
    ('Quality Grade', 'Eco Package'): True,
    ('Eco Package', 'Logistics Prep'): True,
    ('Logistics Prep', 'Feedback Collect'): True,
    ('Feedback Collect', 'System Maintain'): True
}

# Create the POWL model
root = StrictPartialOrder(nodes=nodes, order=order)

# Add the dependencies between nodes
root.order.add_edge('Seed Select', 'Trend Analyze')
root.order.add_edge('Trend Analyze', 'Nutrient Mix')
root.order.add_edge('Nutrient Mix', 'Auto Plant')
root.order.add_edge('Auto Plant', 'Sensor Check')
root.order.add_edge('Sensor Check', 'Data Analyze')
root.order.add_edge('Data Analyze', 'Water Adjust')
root.order.add_edge('Data Analyze', 'Light Control')
root.order.add_edge('Data Analyze', 'Humidity Monitor')
root.order.add_edge('Data Analyze', 'Pest Inspect')
root.order.add_edge('Data Analyze', 'Growth Forecast')
root.order.add_edge('Data Analyze', 'Harvest Plan')
root.order.add_edge('Water Adjust', 'Rapid Cool')
root.order.add_edge('Light Control', 'Rapid Cool')
root.order.add_edge('Humidity Monitor', 'Rapid Cool')
root.order.add_edge('Pest Inspect', 'Rapid Cool')
root.order.add_edge('Growth Forecast', 'Rapid Cool')
root.order.add_edge('Harvest Plan', 'Rapid Cool')
root.order.add_edge('Rapid Cool', 'Quality Grade')
root.order.add_edge('Quality Grade', 'Eco Package')
root.order.add_edge('Eco Package', 'Logistics Prep')
root.order.add_edge('Logistics Prep', 'Feedback Collect')
root.order.add_edge('Feedback Collect', 'System Maintain')

print(root)