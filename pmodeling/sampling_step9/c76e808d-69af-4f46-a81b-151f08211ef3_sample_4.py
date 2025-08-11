import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define silent transitions
skip = SilentTransition()

# Define loops and exclusive choices
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_setup, env_monitoring])
milk_sourcing_choice = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, skip])
culture_selection_choice = OperatorPOWL(operator=Operator.XOR, children=[culture_selection, skip])
milk_testing_choice = OperatorPOWL(operator=Operator.XOR, children=[milk_testing, skip])
curd_formation_choice = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, skip])
whey_separation_choice = OperatorPOWL(operator=Operator.XOR, children=[whey_separation, skip])
molding_cheese_choice = OperatorPOWL(operator=Operator.XOR, children=[molding_cheese, skip])
salting_process_choice = OperatorPOWL(operator=Operator.XOR, children=[salting_process, skip])
flavor_profiling_choice = OperatorPOWL(operator=Operator.XOR, children=[flavor_profiling, skip])
packaging_design_choice = OperatorPOWL(operator=Operator.XOR, children=[packaging_design, skip])
blockchain_entry_choice = OperatorPOWL(operator=Operator.XOR, children=[blockchain_entry, skip])
quality_audit_choice = OperatorPOWL(operator=Operator.XOR, children=[quality_audit, skip])
retail_sync_choice = OperatorPOWL(operator=Operator.XOR, children=[retail_sync, skip])
transport_prep_choice = OperatorPOWL(operator=Operator.XOR, children=[transport_prep, skip])
delivery_tracking_choice = OperatorPOWL(operator=Operator.XOR, children=[delivery_tracking, skip])
customer_feedback_choice = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    milk_sourcing_choice,
    culture_selection_choice,
    milk_testing_choice,
    curd_formation_choice,
    whey_separation_choice,
    molding_cheese_choice,
    salting_process_choice,
    aging_loop,
    flavor_profiling_choice,
    packaging_design_choice,
    blockchain_entry_choice,
    quality_audit_choice,
    retail_sync_choice,
    transport_prep_choice,
    delivery_tracking_choice,
    customer_feedback_choice
])

# Add edges between nodes
root.order.add_edge(milk_sourcing_choice, culture_selection_choice)
root.order.add_edge(milk_sourcing_choice, milk_testing_choice)
root.order.add_edge(culture_selection_choice, curd_formation_choice)
root.order.add_edge(milk_testing_choice, curd_formation_choice)
root.order.add_edge(curd_formation_choice, whey_separation_choice)
root.order.add_edge(whey_separation_choice, molding_cheese_choice)
root.order.add_edge(molding_cheese_choice, salting_process_choice)
root.order.add_edge(salting_process_choice, aging_loop)
root.order.add_edge(aging_loop, flavor_profiling_choice)
root.order.add_edge(aging_loop, packaging_design_choice)
root.order.add_edge(packaging_design_choice, blockchain_entry_choice)
root.order.add_edge(blockchain_entry_choice, quality_audit_choice)
root.order.add_edge(quality_audit_choice, retail_sync_choice)
root.order.add_edge(retail_sync_choice, transport_prep_choice)
root.order.add_edge(transport_prep_choice, delivery_tracking_choice)
root.order.add_edge(delivery_tracking_choice, customer_feedback_choice)

# Print the POWL model
print(root)