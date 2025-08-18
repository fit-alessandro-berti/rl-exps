from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities as transitions
activities = {
    'Site Survey': Transition(label='Site Survey'),
    'Permit Review': Transition(label='Permit Review'),
    'Design Layout': Transition(label='Design Layout'),
    'Material Sourcing': Transition(label='Material Sourcing'),
    'Irrigation Setup': Transition(label='Irrigation Setup'),
    'Sensor Install': Transition(label='Sensor Install'),
    'Structural Test': Transition(label='Structural Test'),
    'Recruit Farmers': Transition(label='Recruit Farmers'),
    'Trial Planting': Transition(label='Trial Planting'),
    'Pest Control': Transition(label='Pest Control'),
    'Soilless Prep': Transition(label='Soilless Prep'),
    'System Calibrate': Transition(label='System Calibrate'),
    'Data Monitor': Transition(label='Data Monitor'),
    'Harvest Plan': Transition(label='Harvest Plan'),
    'Community Outreach': Transition(label='Community Outreach')
}

# Create a strict partial order model
root = StrictPartialOrder()

# Add the activities to the root model
for activity in activities.values():
    root.add_node(activity)

# Define the dependencies (partial order)
root.order.add_edge(activities['Site Survey'], activities['Permit Review'])
root.order.add_edge(activities['Permit Review'], activities['Design Layout'])
root.order.add_edge(activities['Design Layout'], activities['Material Sourcing'])
root.order.add_edge(activities['Material Sourcing'], activities['Irrigation Setup'])
root.order.add_edge(activities['Irrigation Setup'], activities['Sensor Install'])
root.order.add_edge(activities['Sensor Install'], activities['Structural Test'])
root.order.add_edge(activities['Structural Test'], activities['Recruit Farmers'])
root.order.add_edge(activities['Recruit Farmers'], activities['Trial Planting'])
root.order.add_edge(activities['Trial Planting'], activities['Pest Control'])
root.order.add_edge(activities['Pest Control'], activities['Soilless Prep'])
root.order.add_edge(activities['Soilless Prep'], activities['System Calibrate'])
root.order.add_edge(activities['System Calibrate'], activities['Data Monitor'])
root.order.add_edge(activities['Data Monitor'], activities['Harvest Plan'])
root.order.add_edge(activities['Harvest Plan'], activities['Community Outreach'])

print(root)