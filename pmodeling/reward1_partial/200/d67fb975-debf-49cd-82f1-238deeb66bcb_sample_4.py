from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
root = StrictPartialOrder(nodes=[
    Transition(label='Site Analyze'),
    Transition(label='Soil Enhance'),
    Transition(label='Seed Select'),
    Transition(label='Plant Precise'),
    Transition(label='Sensor Deploy'),
    Transition(label='Climate Monitor'),
    Transition(label='Irrigate Adjust'),
    Transition(label='Nutrient Feed'),
    Transition(label='Pest Control'),
    Transition(label='Community Engage'),
    Transition(label='Feedback Collect'),
    Transition(label='Yield Harvest'),
    Transition(label='Waste Sort'),
    Transition(label='Compost Create'),
    Transition(label='Data Analyze'),
    Transition(label='Network Distribute')
])

# Define the order dependencies
root.order.add_edge('Site Analyze', 'Soil Enhance')
root.order.add_edge('Site Analyze', 'Seed Select')
root.order.add_edge('Soil Enhance', 'Plant Precise')
root.order.add_edge('Plant Precise', 'Sensor Deploy')
root.order.add_edge('Sensor Deploy', 'Climate Monitor')
root.order.add_edge('Climate Monitor', 'Irrigate Adjust')
root.order.add_edge('Climate Monitor', 'Nutrient Feed')
root.order.add_edge('Irrigate Adjust', 'Pest Control')
root.order.add_edge('Nutrient Feed', 'Pest Control')
root.order.add_edge('Pest Control', 'Community Engage')
root.order.add_edge('Community Engage', 'Feedback Collect')
root.order.add_edge('Feedback Collect', 'Yield Harvest')
root.order.add_edge('Yield Harvest', 'Waste Sort')
root.order.add_edge('Waste Sort', 'Compost Create')
root.order.add_edge('Compost Create', 'Data Analyze')
root.order.add_edge('Data Analyze', 'Network Distribute')

# Print the final result
print(root)