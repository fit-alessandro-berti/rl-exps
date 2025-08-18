import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their labels
activities = {
    'Site Survey': Transition(label='Site Survey'),
    'Structure Check': Transition(label='Structure Check'),
    'Hydroponic Install': Transition(label='Hydroponic Install'),
    'Lighting Setup': Transition(label='Lighting Setup'),
    'Climate Control': Transition(label='Climate Control'),
    'Seed Selection': Transition(label='Seed Selection'),
    'Nutrient Mix': Transition(label='Nutrient Mix'),
    'Water Recycling': Transition(label='Water Recycling'),
    'Sensor Deploy': Transition(label='Sensor Deploy'),
    'Pest Control': Transition(label='Pest Control'),
    'Growth Monitor': Transition(label='Growth Monitor'),
    'Harvest Plan': Transition(label='Harvest Plan'),
    'Packaging Prep': Transition(label='Packaging Prep'),
    'Delivery Route': Transition(label='Delivery Route'),
    'Data Analysis': Transition(label='Data Analysis'),
    'Yield Forecast': Transition(label='Yield Forecast')
}

# Create a StrictPartialOrder model with the defined activities
root = StrictPartialOrder(nodes=list(activities.values()))

# Define the dependencies between activities
root.order.add_edge(activities['Site Survey'], activities['Structure Check'])
root.order.add_edge(activities['Structure Check'], activities['Hydroponic Install'])
root.order.add_edge(activities['Hydroponic Install'], activities['Lighting Setup'])
root.order.add_edge(activities['Lighting Setup'], activities['Climate Control'])
root.order.add_edge(activities['Climate Control'], activities['Seed Selection'])
root.order.add_edge(activities['Seed Selection'], activities['Nutrient Mix'])
root.order.add_edge(activities['Nutrient Mix'], activities['Water Recycling'])
root.order.add_edge(activities['Water Recycling'], activities['Sensor Deploy'])
root.order.add_edge(activities['Sensor Deploy'], activities['Pest Control'])
root.order.add_edge(activities['Pest Control'], activities['Growth Monitor'])
root.order.add_edge(activities['Growth Monitor'], activities['Harvest Plan'])
root.order.add_edge(activities['Harvest Plan'], activities['Packaging Prep'])
root.order.add_edge(activities['Packaging Prep'], activities['Delivery Route'])
root.order.add_edge(activities['Delivery Route'], activities['Data Analysis'])
root.order.add_edge(activities['Data Analysis'], activities['Yield Forecast'])

# Print the model to verify
print(root)