from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

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

# Define the loop for eco-friendly transportation
loop = OperatorPOWL(operator=Operator.LOOP, children=[eco_transport, batch_storytelling, product_creation, provenance_catalog, community_marketing, collector_targeting, package_assembly, local_cooperatives, environmental_audit, ethical_logistics, global_shipping, feedback_collection])

# Define the XOR for eco-friendly transportation and local cooperatives
xor = OperatorPOWL(operator=Operator.XOR, children=[local_cooperatives, loop])

# Define the root model
root = StrictPartialOrder(nodes=[loop, xor])

# Add the dependencies
root.order.add_edge(loop, xor)

# Print the root model
print(root)