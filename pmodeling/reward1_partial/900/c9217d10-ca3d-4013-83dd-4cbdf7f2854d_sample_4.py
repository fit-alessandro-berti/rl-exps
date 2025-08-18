import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
root = StrictPartialOrder(
    nodes=[
        Transition(label='Site Survey'),
        Transition(label='Climate Study'),
        Transition(label='Design Layout'),
        Transition(label='System Install'),
        Transition(label='Crop Select'),
        Transition(label='Nutrient Plan'),
        Transition(label='Sensor Setup'),
        Transition(label='Automation Test'),
        Transition(label='Staff Train'),
        Transition(label='Compliance Check'),
        Transition(label='Marketing Sync'),
        Transition(label='Data Monitor'),
        Transition(label='Yield Analyze'),
        Transition(label='Supply Chain'),
        Transition(label='Customer Engage')
    ]
)

# Define the dependencies between the nodes
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