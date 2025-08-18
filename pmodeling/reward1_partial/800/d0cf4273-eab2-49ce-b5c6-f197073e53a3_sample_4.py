from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) in the POWL model
sourcing = Transition(label='Material Sourcing')
verify = Transition(label='Cultural Verify')
transport = Transition(label='Eco Transport')
storytelling = Transition(label='Batch Storytelling')
crafting = Transition(label='Craftsman Assignment')
creation = Transition(label='Product Creation')
catalog = Transition(label='Provenance Catalog')
marketing = Transition(label='Community Marketing')
targeting = Transition(label='Collector Targeting')
assembly = Transition(label='Package Assembly')
cooperatives = Transition(label='Local Cooperatives')
audit = Transition(label='Environmental Audit')
logistics = Transition(label='Ethical Logistics')
shipping = Transition(label='Global Shipping')
feedback = Transition(label='Feedback Collection')

# Create the POWL model
root = StrictPartialOrder(nodes=[sourcing, verify, transport, storytelling, crafting, creation, catalog, marketing, targeting, assembly, cooperatives, audit, logistics, shipping, feedback])

# Define the order (dependencies) between the activities
root.order.add_edge(sourcing, verify)
root.order.add_edge(verify, transport)
root.order.add_edge(transport, storytelling)
root.order.add_edge(storytelling, crafting)
root.order.add_edge(crafting, creation)
root.order.add_edge(creation, catalog)
root.order.add_edge(catalog, marketing)
root.order.add_edge(marketing, targeting)
root.order.add_edge(targeting, assembly)
root.order.add_edge(assembly, cooperatives)
root.order.add_edge(cooperatives, audit)
root.order.add_edge(audit, logistics)
root.order.add_edge(logistics, shipping)
root.order.add_edge(shipping, feedback)

# Print the root of the POWL model
print(root)