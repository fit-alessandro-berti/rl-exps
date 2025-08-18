from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
root = StrictPartialOrder(nodes=[
    Transition(label='Sensor Setup'),
    Transition(label='Data Collection'),
    Transition(label='Weather Check'),
    Transition(label='Soil Testing'),
    Transition(label='Crop Selection'),
    Transition(label='Resource Assign'),
    Transition(label='Irrigation Adjust'),
    Transition(label='Pest Scan'),
    Transition(label='Nutrient Mix'),
    Transition(label='Growth Monitor'),
    Transition(label='Community Poll'),
    Transition(label='Schedule Update'),
    Transition(label='Harvest Plan'),
    Transition(label='Waste Sort'),
    Transition(label='Yield Report')
])

# Define the partial order dependencies
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

print(root)