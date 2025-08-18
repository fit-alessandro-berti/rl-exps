import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their labels
activities = {
    'Site Survey': Transition(label='Site Survey'),
    'Load Test': Transition(label='Load Test'),
    'Soil Sample': Transition(label='Soil Sample'),
    'Water Check': Transition(label='Water Check'),
    'Design Plan': Transition(label='Design Plan'),
    'Bed Setup': Transition(label='Bed Setup'),
    'Irrigation Install': Transition(label='Irrigation Install'),
    'Climate Setup': Transition(label='Climate Setup'),
    'Seed Selection': Transition(label='Seed Selection'),
    'Planting Phase': Transition(label='Planting Phase'),
    'Pest Control': Transition(label='Pest Control'),
    'Growth Monitor': Transition(label='Growth Monitor'),
    'Harvest Prep': Transition(label='Harvest Prep'),
    'Community Meet': Transition(label='Community Meet'),
    'Waste Manage': Transition(label='Waste Manage'),
    'Yield Report': Transition(label='Yield Report')
}

# Create the POWL model
root = StrictPartialOrder()

# Add activities to the model
root.nodes.extend(activities.values())

# Define the partial order dependencies
root.order.add_edge(activities['Site Survey'], activities['Load Test'])
root.order.add_edge(activities['Site Survey'], activities['Soil Sample'])
root.order.add_edge(activities['Site Survey'], activities['Water Check'])
root.order.add_edge(activities['Load Test'], activities['Design Plan'])
root.order.add_edge(activities['Soil Sample'], activities['Design Plan'])
root.order.add_edge(activities['Water Check'], activities['Design Plan'])
root.order.add_edge(activities['Design Plan'], activities['Bed Setup'])
root.order.add_edge(activities['Bed Setup'], activities['Irrigation Install'])
root.order.add_edge(activities['Irrigation Install'], activities['Climate Setup'])
root.order.add_edge(activities['Climate Setup'], activities['Seed Selection'])
root.order.add_edge(activities['Seed Selection'], activities['Planting Phase'])
root.order.add_edge(activities['Planting Phase'], activities['Pest Control'])
root.order.add_edge(activities['Pest Control'], activities['Growth Monitor'])
root.order.add_edge(activities['Growth Monitor'], activities['Harvest Prep'])
root.order.add_edge(activities['Harvest Prep'], activities['Community Meet'])
root.order.add_edge(activities['Community Meet'], activities['Waste Manage'])
root.order.add_edge(activities['Waste Manage'], activities['Yield Report'])

# Print the model for verification
print(root)