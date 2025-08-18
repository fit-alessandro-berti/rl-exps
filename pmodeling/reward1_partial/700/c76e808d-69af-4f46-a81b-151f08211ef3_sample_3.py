import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
milk_sourcing = Transition(label='Milk Sourcing')
culture_selection = Transition(label='Culture Selection')
milk_testing = Transition(label='Milk Testing')
curd_formation = Transition(label='Curd Formation')
whey_separation = Transition(label='Whey Separation')
molding_cheese = Transition(label='Molding Cheese')
salting_process = Transition(label='Salting Process')
aging_setup = Transition(label='Aging Setup')
env_monitoring = Transition(label='Env Monitoring')
flavor_profiling = Transition(label='Flavor Profiling')
packaging_design = Transition(label='Packaging Design')
blockchain_entry = Transition(label='Blockchain Entry')
quality_audit = Transition(label='Quality Audit')
retail_sync = Transition(label='Retail Sync')
transport_prep = Transition(label='Transport Prep')
delivery_tracking = Transition(label='Delivery Tracking')
customer_feedback = Transition(label='Customer Feedback')

# Define the process tree
tree = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, culture_selection])
tree.children[0].children = [milk_testing, curd_formation, whey_separation]
tree.children[0].children[0].children = [molding_cheese, salting_process]
tree.children[0].children[0].children[0].children = [aging_setup, env_monitoring]
tree.children[0].children[0].children[0].children[0].children = [flavor_profiling, packaging_design]
tree.children[0].children[0].children[0].children[0].children[0].children = [blockchain_entry, quality_audit]
tree.children[0].children[0].children[0].children[0].children[0].children[0].children = [retail_sync, transport_prep]
tree.children[0].children[0].children[0].children[0].children[0].children[0].children[0].children = [delivery_tracking, customer_feedback]

# Create the root of the POWL model
root = StrictPartialOrder(nodes=[tree])
root.order.add_edge(tree, tree.children[0])
root.order.add_edge(tree, tree.children[1])

# Print the root
print(root)