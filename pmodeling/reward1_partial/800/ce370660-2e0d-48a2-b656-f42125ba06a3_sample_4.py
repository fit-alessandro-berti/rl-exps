import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their exact names
activities = {
    'Structural Check': Transition(label='Structural Check'),
    'Permit Apply': Transition(label='Permit Apply'),
    'Design Layout': Transition(label='Design Layout'),
    'Soil Prep': Transition(label='Soil Prep'),
    'Bed Install': Transition(label='Bed Install'),
    'Irrigation Setup': Transition(label='Irrigation Setup'),
    'Sensor Mount': Transition(label='Sensor Mount'),
    'Solar Connect': Transition(label='Solar Connect'),
    'Seed Order': Transition(label='Seed Order'),
    'Nutrient Mix': Transition(label='Nutrient Mix'),
    'Community Meet': Transition(label='Community Meet'),
    'Staff Train': Transition(label='Staff Train'),
    'Plant Crop': Transition(label='Plant Crop'),
    'Maintenance Plan': Transition(label='Maintenance Plan'),
    'Harvest Schedule': Transition(label='Harvest Schedule'),
    'Waste Manage': Transition(label='Waste Manage')
}

# Create a StrictPartialOrder model
root = StrictPartialOrder()

# Add nodes to the root model
for activity in activities.values():
    root.nodes.append(activity)

# Define the dependencies between activities
root.order.add_edge(activities['Structural Check'], activities['Permit Apply'])
root.order.add_edge(activities['Permit Apply'], activities['Design Layout'])
root.order.add_edge(activities['Design Layout'], activities['Soil Prep'])
root.order.add_edge(activities['Soil Prep'], activities['Bed Install'])
root.order.add_edge(activities['Bed Install'], activities['Irrigation Setup'])
root.order.add_edge(activities['Irrigation Setup'], activities['Sensor Mount'])
root.order.add_edge(activities['Sensor Mount'], activities['Solar Connect'])
root.order.add_edge(activities['Solar Connect'], activities['Seed Order'])
root.order.add_edge(activities['Seed Order'], activities['Nutrient Mix'])
root.order.add_edge(activities['Nutrient Mix'], activities['Community Meet'])
root.order.add_edge(activities['Community Meet'], activities['Staff Train'])
root.order.add_edge(activities['Staff Train'], activities['Plant Crop'])
root.order.add_edge(activities['Plant Crop'], activities['Maintenance Plan'])
root.order.add_edge(activities['Maintenance Plan'], activities['Harvest Schedule'])
root.order.add_edge(activities['Harvest Schedule'], activities['Waste Manage'])

# Print the root model
print(root)