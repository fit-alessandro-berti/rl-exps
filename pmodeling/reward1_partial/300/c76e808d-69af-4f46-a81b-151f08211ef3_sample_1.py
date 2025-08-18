from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define loops and choices
milk_source_loop = OperatorPOWL(operator=Operator.LOOP, children=[milk_sourcing, culture_selection, milk_testing])
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_setup, env_monitoring, flavor_profiling])
packaging_loop = OperatorPOWL(operator=Operator.LOOP, children=[packaging_design, blockchain_entry, quality_audit])
retail_loop = OperatorPOWL(operator=Operator.LOOP, children=[retail_sync, transport_prep, delivery_tracking])
customer_loop = OperatorPOWL(operator=Operator.LOOP, children=[customer_feedback])

# Define partial order
root = StrictPartialOrder(nodes=[milk_source_loop, aging_loop, packaging_loop, retail_loop, customer_loop])

# Define dependencies
root.order.add_edge(milk_source_loop, aging_loop)
root.order.add_edge(aging_loop, packaging_loop)
root.order.add_edge(packaging_loop, retail_loop)
root.order.add_edge(retail_loop, customer_loop)

# Print the model
print(root)