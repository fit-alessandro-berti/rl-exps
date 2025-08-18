from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities
milk_sourcing = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
batch_curdling = Transition(label='Batch Curdling')
whey_removal = Transition(label='Whey Removal')
mold_inoculation = Transition(label='Mold Inoculation')
humidity_control = Transition(label='Humidity Control')
temperature_aging = Transition(label='Temperature Aging')
rind_brushing = Transition(label='Rind Brushing')
flavor_sampling = Transition(label='Flavor Sampling')
label_printing = Transition(label='Label Printing')
packaging_prep = Transition(label='Packaging Prep')
cold_storage = Transition(label='Cold Storage')
order_consolidation = Transition(label='Order Consolidation')
logistics_scheduling = Transition(label='Logistics Scheduling')
customer_feedback = Transition(label='Customer Feedback')
certification_audit = Transition(label='Certification Audit')
recipe_adjustment = Transition(label='Recipe Adjustment')

# Define the process structure
sourcing_loop = OperatorPOWL(operator=Operator.LOOP, children=[milk_sourcing, quality_testing])
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[batch_curdling, whey_removal, mold_inoculation, humidity_control, temperature_aging, rind_brushing, flavor_sampling])
packing_prep_loop = OperatorPOWL(operator=Operator.LOOP, children=[label_printing, packaging_prep, cold_storage])
order_loop = OperatorPOWL(operator=Operator.LOOP, children=[order_consolidation, logistics_scheduling, customer_feedback, certification_audit, recipe_adjustment])

# Define the partial order
root = StrictPartialOrder(nodes=[sourcing_loop, aging_loop, packing_prep_loop, order_loop])

# Define the order relationships
root.order.add_edge(sourcing_loop, aging_loop)
root.order.add_edge(aging_loop, packing_prep_loop)
root.order.add_edge(packing_prep_loop, order_loop)

# Print the result
print(root)