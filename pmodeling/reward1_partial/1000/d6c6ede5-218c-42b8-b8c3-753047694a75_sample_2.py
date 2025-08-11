import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with exact names
activities = {
    'Site Survey': Transition(label='Site Survey'),
    'Load Test': Transition(label='Load Test'),
    'Climate Study': Transition(label='Climate Study'),
    'Permit Check': Transition(label='Permit Check'),
    'System Design': Transition(label='System Design'),
    'Equipment Buy': Transition(label='Equipment Buy'),
    'Sensor Setup': Transition(label='Sensor Setup'),
    'Irrigation Fit': Transition(label='Irrigation Fit'),
    'Solar Install': Transition(label='Solar Install'),
    'Staff Train': Transition(label='Staff Train'),
    'Pilot Plant': Transition(label='Pilot Plant'),
    'Data Monitor': Transition(label='Data Monitor'),
    'Crop Harvest': Transition(label='Crop Harvest'),
    'Maintenance Plan': Transition(label='Maintenance Plan'),
    'Community Meet': Transition(label='Community Meet')
}

# Define the partial order structure
root = StrictPartialOrder(nodes=list(activities.values()))

# Define the dependencies between activities
root.order.add_edge(activities['Site Survey'], activities['Load Test'])
root.order.add_edge(activities['Load Test'], activities['Climate Study'])
root.order.add_edge(activities['Climate Study'], activities['Permit Check'])
root.order.add_edge(activities['Permit Check'], activities['System Design'])
root.order.add_edge(activities['System Design'], activities['Equipment Buy'])
root.order.add_edge(activities['Equipment Buy'], activities['Sensor Setup'])
root.order.add_edge(activities['Sensor Setup'], activities['Irrigation Fit'])
root.order.add_edge(activities['Irrigation Fit'], activities['Solar Install'])
root.order.add_edge(activities['Solar Install'], activities['Staff Train'])
root.order.add_edge(activities['Staff Train'], activities['Pilot Plant'])
root.order.add_edge(activities['Pilot Plant'], activities['Data Monitor'])
root.order.add_edge(activities['Data Monitor'], activities['Crop Harvest'])
root.order.add_edge(activities['Crop Harvest'], activities['Maintenance Plan'])
root.order.add_edge(activities['Maintenance Plan'], activities['Community Meet'])

print(root)