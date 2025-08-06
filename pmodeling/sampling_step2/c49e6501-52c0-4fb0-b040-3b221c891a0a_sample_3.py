import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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
root.order.add_edge(root.nodes[0], root.nodes[1])
root.order.add_edge(root.nodes[1], root.nodes[2])
root.order.add_edge(root.nodes[2], root.nodes[3])
root.order.add_edge(root.nodes[3], root.nodes[4])
root.order.add_edge(root.nodes[4], root.nodes[5])
root.order.add_edge(root.nodes[5], root.nodes[6])
root.order.add_edge(root.nodes[6], root.nodes[7])
root.order.add_edge(root.nodes[7], root.nodes[8])
root.order.add_edge(root.nodes[8], root.nodes[9])
root.order.add_edge(root.nodes[9], root.nodes[10])
root.order.add_edge(root.nodes[10], root.nodes[11])
root.order.add_edge(root.nodes[11], root.nodes[12])
root.order.add_edge(root.nodes[12], root.nodes[13])
root.order.add_edge(root.nodes[13], root.nodes[14])
root.order.add_edge(root.nodes[14], root.nodes[15])

print(root)