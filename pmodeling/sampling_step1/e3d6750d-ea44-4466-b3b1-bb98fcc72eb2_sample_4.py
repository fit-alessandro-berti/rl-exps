import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Structural Check'),
    Transition(label='IoT Setup'),
    Transition(label='Crop Selection'),
    Transition(label='Hydroponic Install'),
    Transition(label='Water Recycling'),
    Transition(label='Energy Audit'),
    Transition(label='Plant Scheduling'),
    Transition(label='Yield Monitoring'),
    Transition(label='Regulation Review'),
    Transition(label='Staff Training'),
    Transition(label='Data Integration'),
    Transition(label='Supply Setup'),
    Transition(label='Quality Audit'),
    Transition(label='Logistics Plan')
])

# Define the dependencies between the activities
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

# Print the POWL model
print(root)