import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
transitions = {
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

# Define the partial order with dependencies
root = StrictPartialOrder(nodes=[transitions['Regulatory Check'], transitions['Path Design'], transitions['Weather Sync'], transitions['Traffic Align'], transitions['Package Secure'], transitions['Customer Alert'], transitions['Drone Assemble'], transitions['Flight Test'], transitions['Data Monitor'], transitions['Safety Audit'], transitions['Emergency Plan'], transitions['Maintenance Plan'], transitions['Battery Cycle'], transitions['Route Update'], transitions['Performance Review'], transitions['Impact Study'], transitions['Compliance Review']])

# Define dependencies between activities
root.order.add_edge(transitions['Regulatory Check'], transitions['Path Design'])
root.order.add_edge(transitions['Regulatory Check'], transitions['Weather Sync'])
root.order.add_edge(transitions['Regulatory Check'], transitions['Traffic Align'])
root.order.add_edge(transitions['Regulatory Check'], transitions['Package Secure'])
root.order.add_edge(transitions['Regulatory Check'], transitions['Customer Alert'])
root.order.add_edge(transitions['Regulatory Check'], transitions['Drone Assemble'])
root.order.add_edge(transitions['Regulatory Check'], transitions['Flight Test'])
root.order.add_edge(transitions['Regulatory Check'], transitions['Data Monitor'])
root.order.add_edge(transitions['Regulatory Check'], transitions['Safety Audit'])
root.order.add_edge(transitions['Regulatory Check'], transitions['Emergency Plan'])
root.order.add_edge(transitions['Regulatory Check'], transitions['Maintenance Plan'])
root.order.add_edge(transitions['Regulatory Check'], transitions['Battery Cycle'])
root.order.add_edge(transitions['Regulatory Check'], transitions['Route Update'])
root.order.add_edge(transitions['Regulatory Check'], transitions['Performance Review'])
root.order.add_edge(transitions['Regulatory Check'], transitions['Impact Study'])
root.order.add_edge(transitions['Regulatory Check'], transitions['Compliance Review'])

root.order.add_edge(transitions['Path Design'], transitions['Weather Sync'])
root.order.add_edge(transitions['Path Design'], transitions['Traffic Align'])
root.order.add_edge(transitions['Path Design'], transitions['Package Secure'])
root.order.add_edge(transitions['Path Design'], transitions['Customer Alert'])
root.order.add_edge(transitions['Path Design'], transitions['Drone Assemble'])
root.order.add_edge(transitions['Path Design'], transitions['Flight Test'])
root.order.add_edge(transitions['Path Design'], transitions['Data Monitor'])
root.order.add_edge(transitions['Path Design'], transitions['Safety Audit'])
root.order.add_edge(transitions['Path Design'], transitions['Emergency Plan'])
root.order.add_edge(transitions['Path Design'], transitions['Maintenance Plan'])
root.order.add_edge(transitions['Path Design'], transitions['Battery Cycle'])
root.order.add_edge(transitions['Path Design'], transitions['Route Update'])
root.order.add_edge(transitions['Path Design'], transitions['Performance Review'])
root.order.add_edge(transitions['Path Design'], transitions['Impact Study'])
root.order.add_edge(transitions['Path Design'], transitions['Compliance Review'])

root.order.add_edge(transitions['Weather Sync'], transitions['Traffic Align'])
root.order.add_edge(transitions['Weather Sync'], transitions['Package Secure'])
root.order.add_edge(transitions['Weather Sync'], transitions['Customer Alert'])
root.order.add_edge(transitions['Weather Sync'], transitions['Drone Assemble'])
root.order.add_edge(transitions['Weather Sync'], transitions['Flight Test'])
root.order.add_edge(transitions['Weather Sync'], transitions['Data Monitor'])
root.order.add_edge(transitions['Weather Sync'], transitions['Safety Audit'])
root.order.add_edge(transitions['Weather Sync'], transitions['Emergency Plan'])
root.order.add_edge(transitions['Weather Sync'], transitions['Maintenance Plan'])
root.order.add_edge(transitions['Weather Sync'], transitions['Battery Cycle'])
root.order.add_edge(transitions['Weather Sync'], transitions['Route Update'])
root.order.add_edge(transitions['Weather Sync'], transitions['Performance Review'])
root.order.add_edge(transitions['Weather Sync'], transitions['Impact Study'])
root.order.add_edge(transitions['Weather Sync'], transitions['Compliance Review'])

root.order.add_edge(transitions['Traffic Align'], transitions['Package Secure'])
root.order.add_edge(transitions['Traffic Align'], transitions['Customer Alert'])
root.order.add_edge(transitions['Traffic Align'], transitions['Drone Assemble'])
root.order.add_edge(transitions['Traffic Align'], transitions['Flight Test'])
root.order.add_edge(transitions['Traffic Align'], transitions['Data Monitor'])
root.order.add_edge(transitions['Traffic Align'], transitions['Safety Audit'])
root.order.add_edge(transitions['Traffic Align'], transitions['Emergency Plan'])
root.order.add_edge(transitions['Traffic Align'], transitions['Maintenance Plan'])
root.order.add_edge(transitions['Traffic Align'], transitions['Battery Cycle'])
root.order.add_edge(transitions['Traffic Align'], transitions['Route Update'])
root.order.add_edge(transitions['Traffic Align'], transitions['Performance Review'])
root.order.add_edge(transitions['Traffic Align'], transitions['Impact Study'])
root.order.add_edge(transitions['Traffic Align'], transitions['Compliance Review'])

root.order.add_edge(transitions['Package Secure'], transitions['Customer Alert'])
root.order.add_edge(transitions['Package Secure'], transitions['Drone Assemble'])
root.order.add_edge(transitions['Package Secure'], transitions['Flight Test'])
root.order.add_edge(transitions['Package Secure'], transitions['Data Monitor'])
root.order.add_edge(transitions['Package Secure'], transitions['Safety Audit'])
root.order.add_edge(transitions['Package Secure'], transitions['Emergency Plan'])
root.order.add_edge(transitions['Package Secure'], transitions['Maintenance Plan'])
root.order.add_edge(transitions['Package Secure'], transitions['Battery Cycle'])
root.order.add_edge(transitions['Package Secure'], transitions['Route Update'])
root.order.add_edge(transitions['Package Secure'], transitions['Performance Review'])
root.order.add_edge(transitions['Package Secure'], transitions['Impact Study'])
root.order.add_edge(transitions['Package Secure'], transitions['Compliance Review'])

root.order.add_edge(transitions['Customer Alert'], transitions['Drone Assemble'])
root.order.add_edge(transitions['Customer Alert'], transitions['Flight Test'])
root.order.add_edge(transitions['Customer Alert'], transitions['Data Monitor'])
root.order.add_edge(transitions['Customer Alert'], transitions['Safety Audit'])
root.order.add_edge(transitions['Customer Alert'], transitions['Emergency Plan'])
root.order.add_edge(transitions['Customer Alert'], transitions['Maintenance Plan'])
root.order.add_edge(transitions['Customer Alert'], transitions['Battery Cycle'])
root.order.add_edge(transitions['Customer Alert'], transitions['Route Update'])
root.order.add_edge(transitions['Customer Alert'], transitions['Performance Review'])
root.order.add_edge(transitions['Customer Alert'], transitions['Impact Study'])
root.order.add_edge(transitions['Customer Alert'], transitions['Compliance Review'])

root.order.add_edge(transitions['Drone Assemble'], transitions['Flight Test'])
root.order.add_edge(transitions['Drone Assemble'], transitions['Data Monitor'])
root.order.add_edge(transitions['Drone Assemble'], transitions['Safety Audit'])
root.order.add_edge(transitions['Drone Assemble'], transitions['Emergency Plan'])
root.order.add_edge(transitions['Drone Assemble'], transitions['Maintenance Plan'])
root.order.add_edge(transitions['Drone Assemble'], transitions['Battery Cycle'])
root.order.add_edge(transitions['Drone Assemble'], transitions['Route Update'])
root.order.add_edge(transitions['Drone Assemble'], transitions['Performance Review'])
root.order.add_edge(transitions['Drone Assemble'], transitions['Impact Study'])
root.order.add_edge(transitions['Drone Assemble'], transitions['Compliance Review'])

root.order.add_edge(transitions['Flight Test'], transitions['Data Monitor'])
root.order.add_edge(transitions['Flight Test'], transitions['Safety Audit'])
root.order.add_edge(transitions['Flight Test'], transitions['Emergency Plan'])
root.order.add_edge(transitions['Flight Test'], transitions['Maintenance Plan'])
root.order.add_edge(transitions['Flight Test'], transitions['Battery Cycle'])
root.order.add_edge(transitions['Flight Test'], transitions['Route Update'])
root.order.add_edge(transitions['Flight Test'], transitions['Performance Review'])
root.order.add_edge(transitions['Flight Test'], transitions['Impact Study'])
root.order.add_edge(transitions['Flight Test'], transitions['Compliance Review'])

root.order.add_edge(transitions['Data Monitor'], transitions['Safety Audit'])
root.order.add_edge(transitions['Data Monitor'], transitions['Emergency Plan'])
root.order.add_edge(transitions['Data Monitor'], transitions['Maintenance Plan'])
root.order.add_edge(transitions['Data Monitor'], transitions['Battery Cycle'])
root.order.add_edge(transitions['Data Monitor'], transitions['Route Update'])
root.order.add_edge(transitions['Data Monitor'], transitions['Performance Review'])
root.order.add_edge(transitions['Data Monitor'], transitions['Impact Study'])
root.order.add_edge(transitions['Data Monitor'], transitions['Compliance Review'])

root.order.add_edge(transitions['Safety Audit'], transitions['Emergency Plan'])
root.order.add_edge(transitions['Safety Audit'], transitions['Maintenance Plan'])
root.order.add_edge(transitions['Safety Audit'], transitions['Battery Cycle'])
root.order.add_edge(transitions['Safety Audit'], transitions['Route Update'])
root.order.add_edge(transitions['Safety Audit'], transitions['Performance Review'])
root.order.add_edge(transitions['Safety Audit'], transitions['Impact Study'])
root.order.add_edge(transitions['Safety Audit'], transitions['Compliance Review'])

root.order.add_edge(transitions['Emergency Plan'], transitions['Maintenance Plan'])
root.order.add_edge(transitions['Emergency Plan'], transitions['Battery Cycle'])
root.order.add_edge(transitions['Emergency Plan'], transitions['Route Update'])
root.order.add_edge(transitions['Emergency Plan'], transitions['Performance Review'])
root.order.add_edge(transitions['Emergency Plan'], transitions['Impact Study'])
root.order.add_edge(transitions['Emergency Plan'], transitions['Compliance Review'])

root.order.add_edge(transitions['Maintenance Plan'], transitions['Battery Cycle'])
root.order.add_edge(transitions['Maintenance Plan'], transitions['Route Update'])
root.order.add_edge(transitions['Maintenance Plan'], transitions['Performance Review'])
root.order.add_edge(transitions['Maintenance Plan'], transitions['Impact Study'])
root.order.add_edge(transitions['Maintenance Plan'], transitions['Compliance Review'])

root.order.add_edge(transitions['Battery Cycle'], transitions['Route Update'])
root.order.add_edge(transitions['Battery Cycle'], transitions['Performance Review'])
root.order.add_edge(transitions['Battery Cycle'], transitions['Impact Study'])
root.order.add_edge(transitions['Battery Cycle'], transitions['Compliance Review'])

root.order.add_edge(transitions['Route Update'], transitions['Performance Review'])
root.order.add_edge(transitions['Route Update'], transitions['Impact Study'])
root.order.add_edge(transitions['Route Update'], transitions['Compliance Review'])

root.order.add_edge(transitions['Performance Review'], transitions['Impact Study'])
root.order.add_edge(transitions['Performance Review'], transitions['Compliance Review'])

root.order.add_edge(transitions['Impact Study'], transitions['Compliance Review'])

print(root)