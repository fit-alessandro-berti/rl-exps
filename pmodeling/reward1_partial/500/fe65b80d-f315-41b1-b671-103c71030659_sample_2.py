from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
root = StrictPartialOrder(nodes=[
    Transition(label='Ingredient Sourcing'),
    Transition(label='Quality Testing'),
    Transition(label='Scent Blending'),
    Transition(label='Micro Batch'),
    Transition(label='Sensory Panel'),
    Transition(label='Formula Adjust'),
    Transition(label='Safety Review'),
    Transition(label='Sustainability Check'),
    Transition(label='Packaging Design'),
    Transition(label='Prototype Creation'),
    Transition(label='Client Feedback'),
    Transition(label='Label Approval'),
    Transition(label='Final Production'),
    Transition(label='Marketing Plan'),
    Transition(label='Distribution Prep'),
    Transition(label='Sales Launch')
])

# Add edges to represent the workflow
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