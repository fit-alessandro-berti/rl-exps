import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their labels
activities = {
    'Site Survey': Transition(label='Site Survey'),
    'Load Test': Transition(label='Load Test'),
    'Permit Review': Transition(label='Permit Review'),
    'Design Layout': Transition(label='Design Layout'),
    'Material Sourcing': Transition(label='Material Sourcing'),
    'Soil Prep': Transition(label='Soil Prep'),
    'Hydroponic Setup': Transition(label='Hydroponic Setup'),
    'Community Meet': Transition(label='Community Meet'),
    'Crop Select': Transition(label='Crop Select'),
    'Sensor Install': Transition(label='Sensor Install'),
    'Water Testing': Transition(label='Water Testing'),
    'Pest Control': Transition(label='Pest Control'),
    'Growth Monitor': Transition(label='Growth Monitor'),
    'Harvest Plan': Transition(label='Harvest Plan'),
    'Market Launch': Transition(label='Market Launch'),
    'Feedback Collect': Transition(label='Feedback Collect')
}

# Create the POWL model
root = StrictPartialOrder()
root.order.add_edge(activities['Site Survey'], activities['Load Test'])
root.order.add_edge(activities['Load Test'], activities['Permit Review'])
root.order.add_edge(activities['Permit Review'], activities['Design Layout'])
root.order.add_edge(activities['Design Layout'], activities['Material Sourcing'])
root.order.add_edge(activities['Material Sourcing'], activities['Soil Prep'])
root.order.add_edge(activities['Soil Prep'], activities['Hydroponic Setup'])
root.order.add_edge(activities['Hydroponic Setup'], activities['Community Meet'])
root.order.add_edge(activities['Community Meet'], activities['Crop Select'])
root.order.add_edge(activities['Crop Select'], activities['Sensor Install'])
root.order.add_edge(activities['Sensor Install'], activities['Water Testing'])
root.order.add_edge(activities['Water Testing'], activities['Pest Control'])
root.order.add_edge(activities['Pest Control'], activities['Growth Monitor'])
root.order.add_edge(activities['Growth Monitor'], activities['Harvest Plan'])
root.order.add_edge(activities['Harvest Plan'], activities['Market Launch'])
root.order.add_edge(activities['Market Launch'], activities['Feedback Collect'])

# Print the root of the POWL model
print(root)