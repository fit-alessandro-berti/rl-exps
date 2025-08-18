import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the process
root = StrictPartialOrder(nodes=[
    Transition(label='Component Check'),
    Transition(label='Spec Review'),
    Transition(label='Parts Sorting'),
    Transition(label='Mechanical Fit'),
    Transition(label='Firmware Load'),
    Transition(label='Calibration Run'),
    Transition(label='Stress Test'),
    Transition(label='Software Patch'),
    Transition(label='Algorithm Tune'),
    Transition(label='Comms Setup'),
    Transition(label='Validation Pass'),
    Transition(label='Data Link'),
    Transition(label='Onsite Deploy'),
    Transition(label='Live Monitor'),
    Transition(label='Update Push'),
    Transition(label='Recovery Plan'),
    Transition(label='Maintenance Log')
])

# Define the dependencies between activities
root.order.add_edge('Component Check', 'Spec Review')
root.order.add_edge('Spec Review', 'Parts Sorting')
root.order.add_edge('Parts Sorting', 'Mechanical Fit')
root.order.add_edge('Mechanical Fit', 'Firmware Load')
root.order.add_edge('Firmware Load', 'Calibration Run')
root.order.add_edge('Calibration Run', 'Stress Test')
root.order.add_edge('Stress Test', 'Software Patch')
root.order.add_edge('Software Patch', 'Algorithm Tune')
root.order.add_edge('Algorithm Tune', 'Comms Setup')
root.order.add_edge('Comms Setup', 'Validation Pass')
root.order.add_edge('Validation Pass', 'Data Link')
root.order.add_edge('Data Link', 'Onsite Deploy')
root.order.add_edge('Onsite Deploy', 'Live Monitor')
root.order.add_edge('Live Monitor', 'Update Push')
root.order.add_edge('Update Push', 'Recovery Plan')
root.order.add_edge('Recovery Plan', 'Maintenance Log')

print(root)