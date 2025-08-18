import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
root = StrictPartialOrder(nodes=[
    Transition(label='Requirement Analysis'),
    Transition(label='Component Sourcing'),
    Transition(label='Quality Check'),
    Transition(label='Frame Assembly'),
    Transition(label='Motor Installation'),
    Transition(label='Sensor Setup'),
    Transition(label='Control Unit'),
    Transition(label='Firmware Upload'),
    Transition(label='System Calibration'),
    Transition(label='Flight Testing'),
    Transition(label='Error Correction'),
    Transition(label='Cosmetic Finish'),
    Transition(label='Packaging Prep'),
    Transition(label='User Manual'),
    Transition(label='Client Training'),
    Transition(label='Support Scheduling')
])

# Define the dependencies between activities
root.order.add_edge(root.nodes[0], root.nodes[1])
root.order.add_edge(root.nodes[1], root.nodes[2])
root.order.add_edge(root.nodes[2], root.nodes[3])
root.order.add_edge(root.nodes[3], root.nodes[4])
root.order.add_edge(root.nodes[3], root.nodes[5])
root.order.add_edge(root.nodes[3], root.nodes[6])
root.order.add_edge(root.nodes[4], root.nodes[7])
root.order.add_edge(root.nodes[5], root.nodes[7])
root.order.add_edge(root.nodes[6], root.nodes[7])
root.order.add_edge(root.nodes[7], root.nodes[8])
root.order.add_edge(root.nodes[8], root.nodes[9])
root.order.add_edge(root.nodes[9], root.nodes[10])
root.order.add_edge(root.nodes[10], root.nodes[11])
root.order.add_edge(root.nodes[11], root.nodes[12])
root.order.add_edge(root.nodes[12], root.nodes[13])
root.order.add_edge(root.nodes[13], root.nodes[14])
root.order.add_edge(root.nodes[14], root.nodes[15])
root.order.add_edge(root.nodes[15], root.nodes[16])
root.order.add_edge(root.nodes[16], root.nodes[17])

# Print the result
print(root)