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

# Define the workflow
loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[material_sourcing, cultural_verify, eco_transport, batch_storytelling, craftsman_assignment, product_creation, provenance_catalog])
xor_1 = OperatorPOWL(operator=Operator.XOR, children=[community_marketing, collector_targeting])
loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[package_assembly, local_cooperatives, environmental_audit, ethical_logistics, global_shipping])
xor_2 = OperatorPOWL(operator=Operator.XOR, children=[feedback_collection])

# Define the root
root = StrictPartialOrder(nodes=[loop_1, xor_1, loop_2, xor_2])
root.order.add_edge(loop_1, xor_1)
root.order.add_edge(loop_2, xor_2)
root.order.add_edge(xor_1, loop_2)
root.order.add_edge(xor_2, loop_1)

print(root)