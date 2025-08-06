import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
root = StrictPartialOrder()

# Milk Collection
root.nodes.append(Transition('Milk Collection'))
root.order.add_edge(None, root.nodes[0])

# Culture Prep
root.nodes.append(Transition('Culture Prep'))
root.order.add_edge(root.nodes[0], root.nodes[1])

# Curd Formation
root.nodes.append(Transition('Curd Formation'))
root.order.add_edge(root.nodes[1], root.nodes[2])

# Whey Separation
root.nodes.append(Transition('Whey Separation'))
root.order.add_edge(root.nodes[2], root.nodes[3])

# Molding Cheese
root.nodes.append(Transition('Molding Cheese'))
root.order.add_edge(root.nodes[3], root.nodes[4])

# Salting Process
root.nodes.append(Transition('Salting Process'))
root.order.add_edge(root.nodes[4], root.nodes[5])

# Initial Aging
root.nodes.append(Transition('Initial Aging'))
root.order.add_edge(root.nodes[5], root.nodes[6])

# Humidity Control
root.nodes.append(Transition('Humidity Control'))
root.order.add_edge(root.nodes[6], root.nodes[7])

# Temperature Check
root.nodes.append(Transition('Temperature Check'))
root.order.add_edge(root.nodes[7], root.nodes[8])

# Flavor Testing
root.nodes.append(Transition('Flavor Testing'))
root.order.add_edge(root.nodes[8], root.nodes[9])

# Final Aging
root.nodes.append(Transition('Final Aging'))
root.order.add_edge(root.nodes[9], root.nodes[10])

# Packaging Artisanal
root.nodes.append(Transition('Packaging Artisanal'))
root.order.add_edge(root.nodes[10], root.nodes[11])

# Label Printing
root.nodes.append(Transition('Label Printing'))
root.order.add_edge(root.nodes[11], root.nodes[12])

# Inventory Audit
root.nodes.append(Transition('Inventory Audit'))
root.order.add_edge(root.nodes[12], root.nodes[13])

# Order Fulfillment
root.nodes.append(Transition('Order Fulfillment'))
root.order.add_edge(root.nodes[13], root.nodes[14])

# Subscription Setup
root.nodes.append(Transition('Subscription Setup'))
root.order.add_edge(root.nodes[14], root.nodes[15])

# Event Marketing
root.nodes.append(Transition('Event Marketing'))
root.order.add_edge(root.nodes[15], root.nodes[16])

# Return the root of the POWL model
print(root)