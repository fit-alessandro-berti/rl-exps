import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
activities = {
    'Regulatory Check': Transition(label='Regulatory Check'),
    'Path Design': Transition(label='Path Design'),
    'Weather Sync': Transition(label='Weather Sync'),
    'Traffic Align': Transition(label='Traffic Align'),
    'Package Secure': Transition(label='Package Secure'),
    'Customer Alert': Transition(label='Customer Alert'),
    'Drone Assemble': Transition(label='Drone Assemble'),
    'Flight Test': Transition(label='Flight Test'),
    'Data Monitor': Transition(label='Data Monitor'),
    'Safety Audit': Transition(label='Safety Audit'),
    'Emergency Plan': Transition(label='Emergency Plan'),
    'Maintenance Plan': Transition(label='Maintenance Plan'),
    'Battery Cycle': Transition(label='Battery Cycle'),
    'Route Update': Transition(label='Route Update'),
    'Performance Review': Transition(label='Performance Review'),
    'Impact Study': Transition(label='Impact Study'),
    'Compliance Review': Transition(label='Compliance Review')
}

# Define the POWL model
root = StrictPartialOrder(nodes=[activities['Regulatory Check'], activities['Path Design'], activities['Weather Sync'], activities['Traffic Align'], activities['Package Secure'], activities['Customer Alert'], activities['Drone Assemble'], activities['Flight Test'], activities['Data Monitor'], activities['Safety Audit'], activities['Emergency Plan'], activities['Maintenance Plan'], activities['Battery Cycle'], activities['Route Update'], activities['Performance Review'], activities['Impact Study'], activities['Compliance Review']])

# Define the partial order dependencies
root.order.add_edge(activities['Regulatory Check'], activities['Path Design'])
root.order.add_edge(activities['Path Design'], activities['Weather Sync'])
root.order.add_edge(activities['Weather Sync'], activities['Traffic Align'])
root.order.add_edge(activities['Traffic Align'], activities['Package Secure'])
root.order.add_edge(activities['Package Secure'], activities['Customer Alert'])
root.order.add_edge(activities['Customer Alert'], activities['Drone Assemble'])
root.order.add_edge(activities['Drone Assemble'], activities['Flight Test'])
root.order.add_edge(activities['Flight Test'], activities['Data Monitor'])
root.order.add_edge(activities['Data Monitor'], activities['Safety Audit'])
root.order.add_edge(activities['Safety Audit'], activities['Emergency Plan'])
root.order.add_edge(activities['Emergency Plan'], activities['Maintenance Plan'])
root.order.add_edge(activities['Maintenance Plan'], activities['Battery Cycle'])
root.order.add_edge(activities['Battery Cycle'], activities['Route Update'])
root.order.add_edge(activities['Route Update'], activities['Performance Review'])
root.order.add_edge(activities['Performance Review'], activities['Impact Study'])
root.order.add_edge(activities['Impact Study'], activities['Compliance Review'])

# Print the root of the POWL model
print(root)