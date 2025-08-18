import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
sourcing = Transition(label='Material Sourcing')
verify = Transition(label='Cultural Verify')
transport = Transition(label='Eco Transport')
storytelling = Transition(label='Batch Storytelling')
craftsman = Transition(label='Craftsman Assignment')
creation = Transition(label='Product Creation')
catalog = Transition(label='Provenance Catalog')
market = Transition(label='Community Marketing')
target = Transition(label='Collector Targeting')
package = Transition(label='Package Assembly')
coop = Transition(label='Local Cooperatives')
audit = Transition(label='Environmental Audit')
logistics = Transition(label='Ethical Logistics')
shipping = Transition(label='Global Shipping')
feedback = Transition(label='Feedback Collection')

# Define partial order
root = StrictPartialOrder(nodes=[sourcing, verify, transport, storytelling, craftsman, creation, catalog, market, target, package, coop, audit, logistics, shipping, feedback])

# Define dependencies
root.order.add_edge(sourcing, verify)
root.order.add_edge(verify, transport)
root.order.add_edge(transport, storytelling)
root.order.add_edge(storytelling, craftsman)
root.order.add_edge(craftsman, creation)
root.order.add_edge(creation, catalog)
root.order.add_edge(catalog, market)
root.order.add_edge(market, target)
root.order.add_edge(target, package)
root.order.add_edge(package, coop)
root.order.add_edge(coop, audit)
root.order.add_edge(audit, logistics)
root.order.add_edge(logistics, shipping)
root.order.add_edge(shipping, feedback)