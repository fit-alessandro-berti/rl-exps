import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
material_sourcing = Transition(label='Material Sourcing')
cultural_verify = Transition(label='Cultural Verify')
eco_transport = Transition(label='Eco Transport')
batch_storytelling = Transition(label='Batch Storytelling')
craftsman_assignment = Transition(label='Craftsman Assignment')
product_creation = Transition(label='Product Creation')
provenance_catalog = Transition(label='Provenance Catalog')
community_marketing = Transition(label='Community Marketing')
collector_targeting = Transition(label='Collector Targeting')
package_assembly = Transition(label='Package Assembly')
local_cooperatives = Transition(label='Local Cooperatives')
environmental_audit = Transition(label='Environmental Audit')
ethical_logistics = Transition(label='Ethical Logistics')
global_shipping = Transition(label='Global Shipping')
feedback_collection = Transition(label='Feedback Collection')

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    material_sourcing, cultural_verify, eco_transport, batch_storytelling, craftsman_assignment,
    product_creation, provenance_catalog, community_marketing, collector_targeting, package_assembly,
    local_cooperatives, environmental_audit, ethical_logistics, global_shipping, feedback_collection
])

# Define the partial order dependencies
root.order.add_edge(material_sourcing, cultural_verify)
root.order.add_edge(material_sourcing, eco_transport)
root.order.add_edge(cultural_verify, batch_storytelling)
root.order.add_edge(eco_transport, batch_storytelling)
root.order.add_edge(batch_storytelling, craftsman_assignment)
root.order.add_edge(batch_storytelling, product_creation)
root.order.add_edge(batch_storytelling, provenance_catalog)
root.order.add_edge(batch_storytelling, community_marketing)
root.order.add_edge(batch_storytelling, collector_targeting)
root.order.add_edge(batch_storytelling, package_assembly)
root.order.add_edge(batch_storytelling, local_cooperatives)
root.order.add_edge(batch_storytelling, environmental_audit)
root.order.add_edge(batch_storytelling, ethical_logistics)
root.order.add_edge(batch_storytelling, global_shipping)
root.order.add_edge(batch_storytelling, feedback_collection)

# Print the root POWL model
print(root)