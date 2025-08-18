from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Structural Audit'),
    Transition(label='System Design'),
    Transition(label='Permit Filing'),
    Transition(label='Foundation Prep'),
    Transition(label='Frame Build'),
    Transition(label='Irrigation Setup'),
    Transition(label='Lighting Install'),
    Transition(label='Climate Control'),
    Transition(label='Nutrient Mix'),
    Transition(label='Crop Planting'),
    Transition(label='Pest Scouting'),
    Transition(label='Data Monitoring'),
    Transition(label='Waste Sorting'),
    Transition(label='Energy Audit'),
    Transition(label='Community Meet'),
    Transition(label='Yield Analysis')
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

# Print the POWL model
print(root)