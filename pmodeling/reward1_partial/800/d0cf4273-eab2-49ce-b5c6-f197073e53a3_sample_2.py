import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL nodes
sourcing = Transition(label='Material Sourcing')
verify = Transition(label='Cultural Verify')
transport = Transition(label='Eco Transport')
storytelling = Transition(label='Batch Storytelling')
craft = Transition(label='Craftsman Assignment')
creation = Transition(label='Product Creation')
catalog = Transition(label='Provenance Catalog')
market = Transition(label='Community Marketing')
targeting = Transition(label='Collector Targeting')
package = Transition(label='Package Assembly')
cooperatives = Transition(label='Local Cooperatives')
audit = Transition(label='Environmental Audit')
logistics = Transition(label='Ethical Logistics')
shipping = Transition(label='Global Shipping')
feedback = Transition(label='Feedback Collection')

# Define the partial order
root = StrictPartialOrder(nodes=[
    sourcing,
    verify,
    transport,
    storytelling,
    craft,
    creation,
    catalog,
    market,
    targeting,
    package,
    cooperatives,
    audit,
    logistics,
    shipping,
    feedback
])

# Define the partial order structure
root.order.add_edge(sourcing, verify)
root.order.add_edge(verify, transport)
root.order.add_edge(transport, storytelling)
root.order.add_edge(storytelling, craft)
root.order.add_edge(craft, creation)
root.order.add_edge(creation, catalog)
root.order.add_edge(catalog, market)
root.order.add_edge(market, targeting)
root.order.add_edge(targeting, package)
root.order.add_edge(package, cooperatives)
root.order.add_edge(cooperatives, audit)
root.order.add_edge(audit, logistics)
root.order.add_edge(logistics, shipping)
root.order.add_edge(shipping, feedback)

# Print the POWL model
print(root)