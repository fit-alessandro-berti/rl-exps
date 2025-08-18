import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
sourcing = Transition(label='Material Sourcing')
verify = Transition(label='Cultural Verify')
transport = Transition(label='Eco Transport')
storytelling = Transition(label='Batch Storytelling')
craft_assignment = Transition(label='Craftsman Assignment')
product_creation = Transition(label='Product Creation')
catalog = Transition(label='Provenance Catalog')
marketing = Transition(label='Community Marketing')
targeting = Transition(label='Collector Targeting')
package_assembly = Transition(label='Package Assembly')
cooperation = Transition(label='Local Cooperatives')
environmental_audit = Transition(label='Environmental Audit')
logistics = Transition(label='Ethical Logistics')
shipping = Transition(label='Global Shipping')
feedback = Transition(label='Feedback Collection')

# Define the POWL model
root = StrictPartialOrder(nodes=[sourcing, verify, transport, storytelling, craft_assignment, product_creation, catalog, marketing, targeting, package_assembly, cooperation, environmental_audit, logistics, shipping, feedback])

# Define the dependencies
root.order.add_edge(sourcing, verify)
root.order.add_edge(verify, transport)
root.order.add_edge(transport, storytelling)
root.order.add_edge(storytelling, craft_assignment)
root.order.add_edge(craft_assignment, product_creation)
root.order.add_edge(product_creation, catalog)
root.order.add_edge(catalog, marketing)
root.order.add_edge(marketing, targeting)
root.order.add_edge(targeting, package_assembly)
root.order.add_edge(package_assembly, cooperation)
root.order.add_edge(cooperation, environmental_audit)
root.order.add_edge(environmental_audit, logistics)
root.order.add_edge(logistics, shipping)
root.order.add_edge(shipping, feedback)

print(root)