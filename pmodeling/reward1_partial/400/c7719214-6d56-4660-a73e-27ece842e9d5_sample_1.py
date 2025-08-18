from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
root = StrictPartialOrder(
    nodes=[
        Transition(label='Milk Sourcing'),
        Transition(label='Diet Monitoring'),
        Transition(label='Culture Selection'),
        Transition(label='Milk Pasteurize'),
        Transition(label='Curd Cutting'),
        Transition(label='Whey Draining'),
        Transition(label='Mold Inoculate'),
        Transition(label='Press Forming'),
        Transition(label='Salt Application'),
        Transition(label='Aging Setup'),
        Transition(label='Humidity Control'),
        Transition(label='Flavor Testing'),
        Transition(label='Packaging Design'),
        Transition(label='Order Processing'),
        Transition(label='Retail Delivery'),
        Transition(label='Event Coordination'),
        Transition(label='Feedback Review')
    ]
)

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
root.order.add_edge(root.nodes[14], root.nodes[15])

# Print the root model
print(root)