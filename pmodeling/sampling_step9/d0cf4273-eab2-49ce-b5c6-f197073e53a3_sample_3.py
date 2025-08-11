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

# Define the silent activities
skip = SilentTransition()

# Define the loop nodes
batch_loop = OperatorPOWL(operator=Operator.LOOP, children=[material_sourcing, cultural_verify, eco_transport, batch_storytelling, craftsman_assignment, product_creation, provenance_catalog])
marketing_loop = OperatorPOWL(operator=Operator.LOOP, children=[community_marketing, collector_targeting, package_assembly, local_cooperatives, environmental_audit, ethical_logistics, global_shipping, feedback_collection])

# Define the exclusive choice nodes
exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[batch_loop, marketing_loop])

# Define the root node
root = StrictPartialOrder(nodes=[exclusive_choice])
root.order.add_edge(exclusive_choice, batch_loop)
root.order.add_edge(exclusive_choice, marketing_loop)

# Print the root node
print(root)