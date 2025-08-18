from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
root = StrictPartialOrder(nodes=[
    Transition(label='Material Sourcing'),
    Transition(label='Cultural Verify'),
    Transition(label='Eco Transport'),
    Transition(label='Batch Storytelling'),
    Transition(label='Craftsman Assignment'),
    Transition(label='Product Creation'),
    Transition(label='Provenance Catalog'),
    Transition(label='Community Marketing'),
    Transition(label='Collector Targeting'),
    Transition(label='Package Assembly'),
    Transition(label='Local Cooperatives'),
    Transition(label='Environmental Audit'),
    Transition(label='Ethical Logistics'),
    Transition(label='Global Shipping'),
    Transition(label='Feedback Collection')
])

# Define the partial order relationships
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

# Print the POWL model
print(root)