from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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
milk_flow = StrictPartialOrder(nodes=[milk_sourcing, culture_selection, milk_testing, curd_formation, whey_separation, molding_cheese, salting_process, aging_setup, env_monitoring, flavor_profiling, packaging_design, blockchain_entry, quality_audit, retail_sync])
milk_flow.order.add_edge(milk_sourcing, culture_selection)
milk_flow.order.add_edge(culture_selection, milk_testing)
milk_flow.order.add_edge(milk_testing, curd_formation)
milk_flow.order.add_edge(curd_formation, whey_separation)
milk_flow.order.add_edge(whey_separation, molding_cheese)
milk_flow.order.add_edge(molding_cheese, salting_process)
milk_flow.order.add_edge(salting_process, aging_setup)
milk_flow.order.add_edge(aging_setup, env_monitoring)
milk_flow.order.add_edge(env_monitoring, flavor_profiling)
milk_flow.order.add_edge(flavor_profiling, packaging_design)
milk_flow.order.add_edge(packaging_design, blockchain_entry)
milk_flow.order.add_edge(blockchain_entry, quality_audit)
milk_flow.order.add_edge(quality_audit, retail_sync)

transport_flow = StrictPartialOrder(nodes=[transport_prep, delivery_tracking, customer_feedback])
transport_flow.order.add_edge(transport_prep, delivery_tracking)
transport_flow.order.add_edge(delivery_tracking, customer_feedback)

root = StrictPartialOrder(nodes=[milk_flow, transport_flow])

# Add dependencies between nodes if necessary
root.order.add_edge(milk_flow, transport_flow)

print(root)