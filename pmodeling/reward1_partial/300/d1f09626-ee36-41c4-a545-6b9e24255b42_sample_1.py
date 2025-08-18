from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
activities = {
    'Site Survey': Transition(label='Site Survey'),
    'Load Test': Transition(label='Load Test'),
    'Soil Sample': Transition(label='Soil Sample'),
    'Climate Check': Transition(label='Climate Check'),
    'Crop Select': Transition(label='Crop Select'),
    'Irrigation Plan': Transition(label='Irrigation Plan'),
    'Energy Setup': Transition(label='Energy Setup'),
    'Pest Control': Transition(label='Pest Control'),
    'Permit Obtain': Transition(label='Permit Obtain'),
    'Stakeholder Meet': Transition(label='Stakeholder Meet'),
    'Bed Construction': Transition(label='Bed Construction'),
    'Seed Planting': Transition(label='Seed Planting'),
    'Water Schedule': Transition(label='Water Schedule'),
    'Growth Monitor': Transition(label='Growth Monitor'),
    'Harvest Plan': Transition(label='Harvest Plan'),
    'Waste Recycle': Transition(label='Waste Recycle'),
    'Yield Report': Transition(label='Yield Report')
}

# Create the partial order
root = StrictPartialOrder(nodes=[
    activities['Site Survey'],
    activities['Load Test'],
    activities['Soil Sample'],
    activities['Climate Check'],
    activities['Crop Select'],
    activities['Irrigation Plan'],
    activities['Energy Setup'],
    activities['Pest Control'],
    activities['Permit Obtain'],
    activities['Stakeholder Meet'],
    activities['Bed Construction'],
    activities['Seed Planting'],
    activities['Water Schedule'],
    activities['Growth Monitor'],
    activities['Harvest Plan'],
    activities['Waste Recycle'],
    activities['Yield Report']
])

# Define the dependencies
root.order.add_edge(activities['Site Survey'], activities['Load Test'])
root.order.add_edge(activities['Load Test'], activities['Soil Sample'])
root.order.add_edge(activities['Soil Sample'], activities['Climate Check'])
root.order.add_edge(activities['Climate Check'], activities['Crop Select'])
root.order.add_edge(activities['Crop Select'], activities['Irrigation Plan'])
root.order.add_edge(activities['Irrigation Plan'], activities['Energy Setup'])
root.order.add_edge(activities['Energy Setup'], activities['Pest Control'])
root.order.add_edge(activities['Pest Control'], activities['Permit Obtain'])
root.order.add_edge(activities['Permit Obtain'], activities['Stakeholder Meet'])
root.order.add_edge(activities['Stakeholder Meet'], activities['Bed Construction'])
root.order.add_edge(activities['Bed Construction'], activities['Seed Planting'])
root.order.add_edge(activities['Seed Planting'], activities['Water Schedule'])
root.order.add_edge(activities['Water Schedule'], activities['Growth Monitor'])
root.order.add_edge(activities['Growth Monitor'], activities['Harvest Plan'])
root.order.add_edge(activities['Harvest Plan'], activities['Waste Recycle'])
root.order.add_edge(activities['Waste Recycle'], activities['Yield Report'])

print(root)