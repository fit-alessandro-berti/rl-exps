import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the artisan cheese production process
root = StrictPartialOrder(nodes=[
    Transition(label='Milk Collection'),
    Transition(label='Culture Prep'),
    Transition(label='Curd Formation'),
    Transition(label='Whey Separation'),
    Transition(label='Molding Cheese'),
    Transition(label='Salting Process'),
    Transition(label='Initial Aging'),
    Transition(label='Humidity Control'),
    Transition(label='Temperature Check'),
    Transition(label='Flavor Testing'),
    Transition(label='Final Aging'),
    Transition(label='Packaging Artisanal'),
    Transition(label='Label Printing'),
    Transition(label='Inventory Audit'),
    Transition(label='Order Fulfillment'),
    Transition(label='Subscription Setup'),
    Transition(label='Event Marketing')
])

# Define the order of execution for the activities
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

# Print the final POWL model
print(root)