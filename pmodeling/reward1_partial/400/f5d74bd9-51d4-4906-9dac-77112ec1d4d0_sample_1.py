import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their labels
activities = {
    'Site Review': Transition(label='Site Review'),
    'Impact Study': Transition(label='Impact Study'),
    'Design Plan': Transition(label='Design Plan'),
    'Structure Mod': Transition(label='Structure Mod'),
    'Hydroponics Setup': Transition(label='Hydroponics Setup'),
    'Crop Select': Transition(label='Crop Select'),
    'Nutrient Mix': Transition(label='Nutrient Mix'),
    'Pest Control': Transition(label='Pest Control'),
    'Sensor Install': Transition(label='Sensor Install'),
    'Staff Train': Transition(label='Staff Train'),
    'Compliance Audit': Transition(label='Compliance Audit'),
    'Packaging Dev': Transition(label='Packaging Dev'),
    'Logistics Plan': Transition(label='Logistics Plan'),
    'Community Engage': Transition(label='Community Engage'),
    'Sustainability Check': Transition(label='Sustainability Check')
}

# Define the POWL model
root = StrictPartialOrder()

# Define the dependencies between activities
root.order.add_edge(activities['Site Review'], activities['Impact Study'])
root.order.add_edge(activities['Impact Study'], activities['Design Plan'])
root.order.add_edge(activities['Design Plan'], activities['Structure Mod'])
root.order.add_edge(activities['Structure Mod'], activities['Hydroponics Setup'])
root.order.add_edge(activities['Hydroponics Setup'], activities['Crop Select'])
root.order.add_edge(activities['Crop Select'], activities['Nutrient Mix'])
root.order.add_edge(activities['Nutrient Mix'], activities['Pest Control'])
root.order.add_edge(activities['Pest Control'], activities['Sensor Install'])
root.order.add_edge(activities['Sensor Install'], activities['Staff Train'])
root.order.add_edge(activities['Staff Train'], activities['Compliance Audit'])
root.order.add_edge(activities['Compliance Audit'], activities['Packaging Dev'])
root.order.add_edge(activities['Packaging Dev'], activities['Logistics Plan'])
root.order.add_edge(activities['Logistics Plan'], activities['Community Engage'])
root.order.add_edge(activities['Community Engage'], activities['Sustainability Check'])

# Print the root model
print(root)