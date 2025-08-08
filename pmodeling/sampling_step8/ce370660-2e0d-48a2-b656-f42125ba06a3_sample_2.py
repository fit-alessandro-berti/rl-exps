import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the process
root = StrictPartialOrder(nodes=[
    Transition(label='Structural Check'),
    Transition(label='Permit Apply'),
    Transition(label='Design Layout'),
    Transition(label='Soil Prep'),
    Transition(label='Bed Install'),
    Transition(label='Irrigation Setup'),
    Transition(label='Sensor Mount'),
    Transition(label='Solar Connect'),
    Transition(label='Seed Order'),
    Transition(label='Nutrient Mix'),
    Transition(label='Community Meet'),
    Transition(label='Staff Train'),
    Transition(label='Plant Crop'),
    Transition(label='Maintenance Plan'),
    Transition(label='Harvest Schedule'),
    Transition(label='Waste Manage')
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

# Print the final POWL model
print(root)