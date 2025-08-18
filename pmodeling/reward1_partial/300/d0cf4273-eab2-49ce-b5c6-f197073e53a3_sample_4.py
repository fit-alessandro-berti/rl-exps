import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define the loops and choices
sourcing_loop = OperatorPOWL(operator=Operator.LOOP, children=[material_sourcing, cultural_verify, eco_transport])
storytelling_loop = OperatorPOWL(operator=Operator.LOOP, children=[batch_storytelling, craftsman_assignment, product_creation])
catalog_loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_catalog, community_marketing, collector_targeting])
assembly_loop = OperatorPOWL(operator=Operator.LOOP, children=[package_assembly, local_cooperatives, environmental_audit, ethical_logistics])
shipping_loop = OperatorPOWL(operator=Operator.LOOP, children=[global_shipping, feedback_collection])

# Define the root model
root = StrictPartialOrder(nodes=[sourcing_loop, storytelling_loop, catalog_loop, assembly_loop, shipping_loop])
root.order.add_edge(sourcing_loop, storytelling_loop)
root.order.add_edge(storytelling_loop, catalog_loop)
root.order.add_edge(catalog_loop, assembly_loop)
root.order.add_edge(assembly_loop, shipping_loop)

print(root)