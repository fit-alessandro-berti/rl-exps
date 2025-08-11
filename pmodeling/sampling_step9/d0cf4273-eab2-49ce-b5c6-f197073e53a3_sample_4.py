import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the silent transitions
skip = SilentTransition()

# Define the loop and choice structures
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[material_sourcing, cultural_verify, eco_transport, batch_storytelling, craftsman_assignment, product_creation, provenance_catalog, community_marketing, collector_targeting, package_assembly, local_cooperatives, environmental_audit, ethical_logistics, global_shipping, feedback_collection])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[loop1])

xor1 = OperatorPOWL(operator=Operator.XOR, children=[loop2, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[loop2, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[xor1, xor2])
root.order.add_edge(xor1, loop1)
root.order.add_edge(xor2, loop2)

# Print the final result
print(root)