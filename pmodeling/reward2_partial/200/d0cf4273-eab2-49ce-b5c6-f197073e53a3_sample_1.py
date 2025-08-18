from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
sourcing = Transition(label='Material Sourcing')
verify = Transition(label='Cultural Verify')
transport = Transition(label='Eco Transport')
storytelling = Transition(label='Batch Storytelling')
crafting = Transition(label='Craftsman Assignment')
product = Transition(label='Product Creation')
catalog = Transition(label='Provenance Catalog')
market = Transition(label='Community Marketing')
target = Transition(label='Collector Targeting')
package = Transition(label='Package Assembly')
cooperatives = Transition(label='Local Cooperatives')
audit = Transition(label='Environmental Audit')
logistics = Transition(label='Ethical Logistics')
shipping = Transition(label='Global Shipping')
feedback = Transition(label='Feedback Collection')

# Define the process using a StrictPartialOrder
root = StrictPartialOrder(nodes=[sourcing, verify, transport, storytelling, crafting, product, catalog, market, target, package, cooperatives, audit, logistics, shipping, feedback])

# Define the partial order dependencies
root.order.add_edge(sourcing, verify)
root.order.add_edge(verify, transport)
root.order.add_edge(transport, storytelling)
root.order.add_edge(storytelling, crafting)
root.order.add_edge(crafting, product)
root.order.add_edge(product, catalog)
root.order.add_edge(catalog, market)
root.order.add_edge(market, target)
root.order.add_edge(target, package)
root.order.add_edge(package, cooperatives)
root.order.add_edge(cooperatives, audit)
root.order.add_edge(audit, logistics)
root.order.add_edge(logistics, shipping)
root.order.add_edge(shipping, feedback)

# Print the root POWL model
print(root)