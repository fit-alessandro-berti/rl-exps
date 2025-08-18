from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the process
root = StrictPartialOrder(nodes=[
    Transition(label='Seed Selection'),
    Transition(label='Nutrient Mix'),
    Transition(label='Environment Check'),
    Transition(label='Planting Setup'),
    Transition(label='Growth Monitoring'),
    Transition(label='Pest Control'),
    Transition(label='Automated Harvest'),
    Transition(label='Quality Inspect'),
    Transition(label='Packaging Prep'),
    Transition(label='Order Fulfill'),
    Transition(label='Local Delivery'),
    Transition(label='Waste Collect'),
    Transition(label='Biomass Process'),
    Transition(label='Compost Create'),
    Transition(label='Energy Recover'),
    Transition(label='Regulation Review'),
    Transition(label='Community Engage')
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

# Print the root node
print(root)