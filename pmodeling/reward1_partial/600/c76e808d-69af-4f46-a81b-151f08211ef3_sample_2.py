import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL nodes
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

# Define the POWL operators
milk_sourcing_op = OperatorPOWL(operator=Operator.CONCURRENT, children=[milk_sourcing])
culture_selection_op = OperatorPOWL(operator=Operator.CONCURRENT, children=[culture_selection])
milk_testing_op = OperatorPOWL(operator=Operator.CONCURRENT, children=[milk_testing])
curd_formation_op = OperatorPOWL(operator=Operator.CONCURRENT, children=[curd_formation])
whey_separation_op = OperatorPOWL(operator=Operator.CONCURRENT, children=[whey_separation])
molding_cheese_op = OperatorPOWL(operator=Operator.CONCURRENT, children=[molding_cheese])
salting_process_op = OperatorPOWL(operator=Operator.CONCURRENT, children=[salting_process])
aging_setup_op = OperatorPOWL(operator=Operator.CONCURRENT, children=[aging_setup])
env_monitoring_op = OperatorPOWL(operator=Operator.CONCURRENT, children=[env_monitoring])
flavor_profiling_op = OperatorPOWL(operator=Operator.CONCURRENT, children=[flavor_profiling])
packaging_design_op = OperatorPOWL(operator=Operator.CONCURRENT, children=[packaging_design])
blockchain_entry_op = OperatorPOWL(operator=Operator.CONCURRENT, children=[blockchain_entry])
quality_audit_op = OperatorPOWL(operator=Operator.CONCURRENT, children=[quality_audit])
retail_sync_op = OperatorPOWL(operator=Operator.CONCURRENT, children=[retail_sync])
transport_prep_op = OperatorPOWL(operator=Operator.CONCURRENT, children=[transport_prep])
delivery_tracking_op = OperatorPOWL(operator=Operator.CONCURRENT, children=[delivery_tracking])
customer_feedback_op = OperatorPOWL(operator=Operator.CONCURRENT, children=[customer_feedback])

# Define the POWL partial order
root = StrictPartialOrder(nodes=[milk_sourcing_op, culture_selection_op, milk_testing_op, curd_formation_op, whey_separation_op, molding_cheese_op, salting_process_op, aging_setup_op, env_monitoring_op, flavor_profiling_op, packaging_design_op, blockchain_entry_op, quality_audit_op, retail_sync_op, transport_prep_op, delivery_tracking_op, customer_feedback_op])

# Define the order of execution
root.order.add_edge(milk_sourcing_op, culture_selection_op)
root.order.add_edge(milk_sourcing_op, milk_testing_op)
root.order.add_edge(culture_selection_op, curd_formation_op)
root.order.add_edge(milk_testing_op, curd_formation_op)
root.order.add_edge(curd_formation_op, whey_separation_op)
root.order.add_edge(whey_separation_op, molding_cheese_op)
root.order.add_edge(molding_cheese_op, salting_process_op)
root.order.add_edge(salting_process_op, aging_setup_op)
root.order.add_edge(aging_setup_op, env_monitoring_op)
root.order.add_edge(env_monitoring_op, flavor_profiling_op)
root.order.add_edge(flavor_profiling_op, packaging_design_op)
root.order.add_edge(packaging_design_op, blockchain_entry_op)
root.order.add_edge(blockchain_entry_op, quality_audit_op)
root.order.add_edge(quality_audit_op, retail_sync_op)
root.order.add_edge(retail_sync_op, transport_prep_op)
root.order.add_edge(transport_prep_op, delivery_tracking_op)
root.order.add_edge(delivery_tracking_op, customer_feedback_op)

# Print the POWL model
print(root)