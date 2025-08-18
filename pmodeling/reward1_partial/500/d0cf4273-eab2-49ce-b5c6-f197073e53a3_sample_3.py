from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define the process
root = StrictPartialOrder(
    nodes=[
        material_sourcing,
        cultural_verify,
        eco_transport,
        batch_storytelling,
        craftsman_assignment,
        product_creation,
        provenance_catalog,
        community_marketing,
        collector_targeting,
        package_assembly,
        local_cooperatives,
        environmental_audit,
        ethical_logistics,
        global_shipping,
        feedback_collection
    ],
    order={
        material_sourcing: [cultural_verify],
        cultural_verify: [eco_transport],
        eco_transport: [batch_storytelling],
        batch_storytelling: [craftsman_assignment],
        craftsman_assignment: [product_creation],
        product_creation: [provenance_catalog],
        provenance_catalog: [community_marketing],
        community_marketing: [collector_targeting],
        collector_targeting: [package_assembly],
        package_assembly: [local_cooperatives],
        local_cooperatives: [environmental_audit],
        environmental_audit: [ethical_logistics],
        ethical_logistics: [global_shipping],
        global_shipping: [feedback_collection]
    }
)

# Add edges to the process
root.order.add_edge(material_sourcing, cultural_verify)
root.order.add_edge(cultural_verify, eco_transport)
root.order.add_edge(eco_transport, batch_storytelling)
root.order.add_edge(batch_storytelling, craftsman_assignment)
root.order.add_edge(craftsman_assignment, product_creation)
root.order.add_edge(product_creation, provenance_catalog)
root.order.add_edge(provenance_catalog, community_marketing)
root.order.add_edge(community_marketing, collector_targeting)
root.order.add_edge(collector_targeting, package_assembly)
root.order.add_edge(package_assembly, local_cooperatives)
root.order.add_edge(local_cooperatives, environmental_audit)
root.order.add_edge(environmental_audit, ethical_logistics)
root.order.add_edge(ethical_logistics, global_shipping)
root.order.add_edge(global_shipping, feedback_collection)

# Print the root
print(root)