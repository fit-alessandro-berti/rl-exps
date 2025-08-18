import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a transition in the POWL graph
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

# Define the POWL model structure
root = StrictPartialOrder(nodes=[
    milk_sourcing, culture_selection, milk_testing, curd_formation, whey_separation, molding_cheese,
    salting_process, aging_setup, env_monitoring, flavor_profiling, packaging_design, blockchain_entry,
    quality_audit, retail_sync, transport_prep, delivery_tracking, customer_feedback
])

# Establish exclusive choices and loops
# Milk Sourcing -> Culture Selection
root.order.add_edge(milk_sourcing, culture_selection)

# Culture Selection -> Milk Testing
root.order.add_edge(culture_selection, milk_testing)

# Milk Testing -> Curd Formation
root.order.add_edge(milk_testing, curd_formation)

# Curd Formation -> Whey Separation
root.order.add_edge(curd_formation, whey_separation)

# Whey Separation -> Molding Cheese
root.order.add_edge(whey_separation, molding_cheese)

# Molding Cheese -> Salting Process
root.order.add_edge(molding_cheese, salting_process)

# Salting Process -> Aging Setup
root.order.add_edge(salting_process, aging_setup)

# Aging Setup -> Env Monitoring
root.order.add_edge(aging_setup, env_monitoring)

# Env Monitoring -> Flavor Profiling
root.order.add_edge(env_monitoring, flavor_profiling)

# Flavor Profiling -> Packaging Design
root.order.add_edge(flavor_profiling, packaging_design)

# Packaging Design -> Blockchain Entry
root.order.add_edge(packaging_design, blockchain_entry)

# Blockchain Entry -> Quality Audit
root.order.add_edge(blockchain_entry, quality_audit)

# Quality Audit -> Retail Sync
root.order.add_edge(quality_audit, retail_sync)

# Retail Sync -> Transport Prep
root.order.add_edge(retail_sync, transport_prep)

# Transport Prep -> Delivery Tracking
root.order.add_edge(transport_prep, delivery_tracking)

# Delivery Tracking -> Customer Feedback
root.order.add_edge(delivery_tracking, customer_feedback)

print("POWL model generated successfully.")